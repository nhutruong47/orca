"""
Prompt sanitization and prompt-injection protection.

Designed for ORCA AI (Vietnamese ERP assistant) but generic enough to be
useful elsewhere.

The module exposes:

    sanitize_user_query(text: str) -> SanitizationResult

The result contains the cleaned text and metadata about what was redacted.
Original text is NEVER mutated in place — the caller decides what to do
with the result.

Threat model covered:
    1. Instruction overrides
       "ignore previous instructions", "you are now ...",
       "system:", "new instructions:".
    2. Role escalation
       "act as admin", "developer mode", "jailbreak".
    3. Delimiter injection
       Triple backticks, <system>, [INST], JSON wrappers.
    4. Hidden control characters
       Zero-width characters, soft hyphens, RTL/LTR overrides, BOMs.
    5. Excessive repetition / length
       Pad-spam attacks that try to drown the system prompt.
    6. Unicode confusables
       Cyrillic "а" mixed into "admin" etc.
    7. Suspicious URLs / encoded payloads
       data: URIs, javascript: schemes, base64 long blobs.

Output:
    - Replaced inline with neutral placeholders (e.g. "[REDACTED:injection]")
      so the legitimate part of the query still reaches the LLM.
    - Limits applied (length cap, repetition collapse).
    - Logs all detections at WARNING level.
"""

from __future__ import annotations

import logging
import re
import unicodedata
from dataclasses import dataclass, field
from typing import List, Tuple

logger = logging.getLogger(__name__)


# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

MAX_QUERY_LENGTH = 2000            # characters
MAX_REPEATED_TOKEN_RUN = 20        # collapse runs of >N same token
CONFIDENCE_BLOCK_THRESHOLD = 4     # ≥4 detections -> block entirely


# -----------------------------------------------------------------------------
# Pattern catalogue
# -----------------------------------------------------------------------------

# Each tuple is (compiled regex, label). Order matters: longer / more specific
# patterns run first so we don't double-strip the residue of a wider pattern.
_PATTERNS: List[Tuple[re.Pattern, str]] = [
    # Instruction override attempts
    (re.compile(r"(?is)\bignore\s+(?:all\s+)?(?:previous|prior|above|earlier)\s+(?:instructions?|prompts?|rules?)\b"), "instruction_override"),
    (re.compile(r"(?is)\bdisregard\s+(?:all\s+)?(?:previous|prior|above|earlier)\s+(?:instructions?|prompts?|rules?)\b"), "instruction_override"),
    (re.compile(r"(?is)\bforget\s+(?:everything|all)\b[^.]*\b(?:instructions?|rules?|prompts?)\b"), "instruction_override"),
    (re.compile(r"(?is)\bnew\s+instructions?\s*[:\-]"), "instruction_override"),
    (re.compile(r"(?is)\boverride\s+(?:system|security|safety|guardrails?)\b"), "instruction_override"),
    (re.compile(r"(?is)\bbypass\s+(?:filter|safety|moderation|guardrails?)\b"), "instruction_override"),
    (re.compile(r"(?is)\bpretend\s+(?:to\s+be|you\s+are)\s+(?:an?\s+)?(?:admin|root|developer|god|jailbreak)\b"), "role_escalation"),
    (re.compile(r"(?is)\byou\s+are\s+now\s+(?:a|an)\s+(?:admin|developer|root|jailbroken|evil|different)\b"), "role_escalation"),
    (re.compile(r"(?is)\bact\s+as\s+(?:an?\s+)?(?:admin|developer|root|jailbroken|evil)\b"), "role_escalation"),
    (re.compile(r"(?is)\b(?:developer|admin|debug|god|sudo)\s+mode\b"), "role_escalation"),
    (re.compile(r"(?is)\bjailbreak(?:ed|ing)?\b"), "role_escalation"),
    (re.compile(r"(?is)\bDAN\b"), "role_escalation"),

    # Delimiter injection — closing/opening prompt sections
    (re.compile(r"```\s*system\b", re.IGNORECASE), "delimiter_injection"),
    (re.compile(r"```\s*instructions?\b", re.IGNORECASE), "delimiter_injection"),
    (re.compile(r"</?\s*(?:system|assistant|user|instructions?|prompt)\s*>", re.IGNORECASE), "delimiter_injection"),
    (re.compile(r"\[\s*(?:INST|SYS|SYSTEM)\s*[:\]]", re.IGNORECASE), "delimiter_injection"),
    (re.compile(r"<<\s*SYS\s*>>", re.IGNORECASE), "delimiter_injection"),
    (re.compile(r"\{\{\s*system\s*\}\}", re.IGNORECASE), "delimiter_injection"),

    # Encoded payload attempts
    (re.compile(r"(?i)\bdata:(?:text|application)/[a-z0-9.+-]+;base64,"), "encoded_payload"),
    (re.compile(r"(?i)\bjavascript\s*:"), "encoded_payload"),
    (re.compile(r"(?i)\bvbscript\s*:"), "encoded_payload"),

    # Tool / function invocation attempts that aren't part of ORCA's contract
    (re.compile(r"(?is)\bcall\s+(?:the\s+)?function\s+\w+"), "tool_injection"),
    (re.compile(r"(?is)\bexecute\s+(?:tool|function|command)\b"), "tool_injection"),

    # Prompt leak attempts
    (re.compile(r"(?is)\b(?:show|reveal|print|repeat|output)\s+(?:me\s+)?(?:the\s+)?(?:system|initial|original)\s+prompt\b"), "prompt_leak"),
    (re.compile(r"(?is)\bwhat(?:'s| is)\s+(?:the\s+)?system\s+prompt\b"), "prompt_leak"),
]

# Unicode confusable mapping (a small curated set — covers the common
# Cyrillic / Greek homoglyphs used to spell "admin", "system", etc.).
_CONFUSABLE_MAP = {
    "\u0430": "a",  # Cyrillic а
    "\u0435": "e",  # Cyrillic е
    "\u043e": "o",  # Cyrillic о
    "\u0440": "p",  # Cyrillic р
    "\u0441": "c",  # Cyrillic с
    "\u0443": "y",  # Cyrillic у (looks like y)
    "\u0445": "x",  # Cyrillic х
    "\u0456": "i",  # Cyrillic і
    "\u0458": "j",  # Cyrillic ј
    "\u0391": "A",
    "\u0392": "B",
    "\u0395": "E",
    "\u0396": "Z",
    "\u0397": "H",
    "\u0399": "I",
    "\u039A": "K",
    "\u039C": "M",
    "\u039D": "N",
    "\u039F": "O",
    "\u03A1": "P",
    "\u03A4": "T",
    "\u03A5": "Y",
    "\u03A7": "X",
    "\u03BF": "o",
    "\u03C1": "p",
}

_HIDDEN_CHARS = {
    "\u200b",  # zero-width space
    "\u200c",  # zero-width non-joiner
    "\u200d",  # zero-width joiner
    "\u2060",  # word joiner
    "\ufeff",  # BOM / zero-width no-break space
    "\u00ad",  # soft hyphen
    "\u202a",  # left-to-right embedding
    "\u202b",  # right-to-left embedding
    "\u202c",  # pop directional formatting
    "\u202d",  # left-to-right override
    "\u202e",  # right-to-left override
    "\u2066",  # left-to-right isolate
    "\u2067",  # right-to-left isolate
    "\u2068",  # first strong isolate
    "\u2069",  # pop directional isolate
}


# -----------------------------------------------------------------------------
# Result container
# -----------------------------------------------------------------------------

@dataclass
class SanitizationResult:
    text: str
    original_text: str
    is_safe: bool
    blocked: bool
    detections: List[str] = field(default_factory=list)
    redaction_count: int = 0
    notes: List[str] = field(default_factory=list)


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def _strip_hidden(text: str) -> Tuple[str, int]:
    removed = 0
    out_chars = []
    for ch in text:
        if ch in _HIDDEN_CHARS:
            removed += 1
            continue
        # Drop most C0 / C1 control characters except \n, \r, \t.
        if ord(ch) < 32 and ch not in {"\n", "\r", "\t"}:
            removed += 1
            continue
        if ord(ch) == 0x7F:  # DEL
            removed += 1
            continue
        out_chars.append(ch)
    return "".join(out_chars), removed


def _normalize_unicode(text: str) -> str:
    """NFKC then collapse common confusables."""
    text = unicodedata.normalize("NFKC", text)
    return "".join(_CONFUSABLE_MAP.get(ch, ch) for ch in text)


def _collapse_repetition(text: str) -> Tuple[str, int]:
    """Collapse any run of >MAX_REPEATED_TOKEN_RUN identical tokens."""
    reduced = 0
    pattern = re.compile(r"(\S)(\1{%d,})" % (MAX_REPEATED_TOKEN_RUN - 1))
    def _sub(m: re.Match) -> str:
        nonlocal reduced
        reduced += 1
        return m.group(1) * 3
    return pattern.sub(_sub, text), reduced


def _apply_length_cap(text: str) -> Tuple[str, bool]:
    if len(text) <= MAX_QUERY_LENGTH:
        return text, False
    return text[:MAX_QUERY_LENGTH].rstrip(), True


# -----------------------------------------------------------------------------
# Public API
# -----------------------------------------------------------------------------

def sanitize_user_query(raw_text: str) -> SanitizationResult:
    """Sanitize a user-supplied query before it enters the RAG pipeline.

    The function is conservative: when it cannot confidently decide what to
    keep, it removes the suspect fragment. It never raises on hostile input.
    """
    if not isinstance(raw_text, str):
        raw_text = str(raw_text)

    original = raw_text
    detections: List[str] = []
    notes: List[str] = []
    redactions = 0

    # 1. Strip hidden / control characters FIRST so later regexes can't be
    #    bypassed with zero-width spaces between letters.
    stripped, hidden_removed = _strip_hidden(raw_text)
    if hidden_removed:
        notes.append(f"removed_{hidden_removed}_hidden_chars")

    # 2. Unicode normalization + confusable collapse.
    normalized = _normalize_unicode(stripped)

    # 3. Run the pattern catalogue. Order matters (longest/specific first).
    cleaned = normalized
    for pattern, label in _PATTERNS:
        new_cleaned, n = pattern.subn("[REDACTED:policy]", cleaned)
        if n > 0:
            cleaned = new_cleaned
            redactions += n
            detections.append(label)
            logger.warning(
                "Prompt injection attempt detected (%s): %d occurrence(s) redacted",
                label,
                n,
            )

    # 4. Collapse repetition attacks.
    cleaned, repeats_removed = _collapse_repetition(cleaned)
    if repeats_removed:
        notes.append(f"collapsed_{repeats_removed}_repetition_spans")

    # 5. Length cap.
    cleaned, was_truncated = _apply_length_cap(cleaned.strip())
    if was_truncated:
        notes.append("truncated_to_max_length")

    # 6. Final policy: too many detections => block entirely.
    blocked = len(detections) >= CONFIDENCE_BLOCK_THRESHOLD
    is_safe = not blocked and redactions == 0

    result = SanitizationResult(
        text=cleaned,
        original_text=original,
        is_safe=is_safe,
        blocked=blocked,
        detections=detections,
        redaction_count=redactions,
        notes=notes,
    )
    return result


__all__ = [
    "sanitize_user_query",
    "SanitizationResult",
    "MAX_QUERY_LENGTH",
]