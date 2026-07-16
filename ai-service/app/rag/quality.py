"""
Document quality scoring.

Used by the indexer to persist a deterministic quality score (0..1) and
component breakdown (completeness, accuracy, freshness, relevance) for each
chunk. The RAG layer reads this back via `referenced_knowledge[].quality` so
the UI can show "stale" or "thin" warnings, and the API can deprioritise
low-quality chunks in retrieval.
"""

from __future__ import annotations

import logging
import re
import time
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


# Heuristic baseline: empty / placeholder content has zero quality.
_LOW_VALUE_PATTERNS = [
    re.compile(r"(?i)^\s*$"),
    re.compile(r"(?i)\bTODO\b"),
    re.compile(r"(?i)\bFIXME\b"),
    re.compile(r"(?i)\b(?:lorem|ipsum)\b"),
    re.compile(r"(?i)\b(?:placeholder|dummy|sample)\b"),
]

# Sources we treat as "internal / live data". Their freshness decays quickly.
_FRESH_HALF_LIFE_DAYS = {
    "inventory": 30,
    "orders": 14,
    "products": 60,
    "users": 30,
    "teams": 60,
    "policies": 180,
    "faq": 90,
    "manual": 365,
}

_DEFAULT_HALF_LIFE_DAYS = 90


@dataclass
class QualityBreakdown:
    """Per-component quality scores for a single document."""

    completeness: float = 0.0
    accuracy: float = 0.0
    freshness: float = 0.0
    relevance: float = 0.0
    overall: float = 0.0
    reasons: list = field(default_factory=list)

    def to_dict(self) -> Dict[str, float]:
        return {
            "completeness": round(self.completeness, 4),
            "accuracy": round(self.accuracy, 4),
            "freshness": round(self.freshness, 4),
            "relevance": round(self.relevance, 4),
            "overall": round(self.overall, 4),
        }


def _is_low_value(content: str) -> bool:
    for pat in _LOW_VALUE_PATTERNS:
        if pat.search(content):
            return True
    return False


def _completeness_score(content: str, metadata: Dict[str, Any]) -> float:
    """1.0 for well-formed content; penalised for short / placeholder text."""
    if _is_low_value(content):
        return 0.0
    length = len(content or "")
    if length == 0:
        return 0.0
    # Saturate at 800 characters; anything beyond that gets full marks.
    length_score = min(1.0, length / 800.0)
    # Bonus for having structured metadata (title, category).
    meta_keys = {k for k in metadata or {} if k}
    meta_bonus = 0.1 if "title" in meta_keys else 0.0
    return min(1.0, length_score + meta_bonus)


def _accuracy_score(content: str, source: str) -> float:
    """Heuristic: penalise obviously noisy / boilerplate content.

    Real "accuracy" is impossible to compute at index time without a separate
    ground-truth source, so we approximate by treating the source's trust
    level as a baseline and reducing for low-signal markers.
    """
    if _is_low_value(content):
        return 0.0
    base = {
        "manual": 0.95,
        "policies": 0.92,
        "faq": 0.9,
        "products": 0.88,
        "inventory": 0.85,
        "orders": 0.85,
        "teams": 0.8,
        "users": 0.75,
    }.get(source, 0.8)
    # Penalise excessive repetition or very short content.
    tokens = content.split()
    if len(tokens) < 5:
        return max(0.0, base - 0.3)
    unique_ratio = len(set(tokens)) / max(1, len(tokens))
    if unique_ratio < 0.2:
        return max(0.0, base - 0.2)
    return base


def _freshness_score(updated_at: Optional[str], source: str, now_epoch: float) -> float:
    """Time-decay based on the source's half-life. Missing timestamps => neutral."""
    if not updated_at:
        return 0.5
    try:
        from datetime import datetime

        ts = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
        ts_epoch = ts.timestamp()
    except (ValueError, AttributeError, TypeError):
        return 0.5
    age_days = max(0.0, (now_epoch - ts_epoch) / 86400.0)
    half_life = _FRESH_HALF_LIFE_DAYS.get(source, _DEFAULT_HALF_LIFE_DAYS)
    # Exponential decay: score = 0.5 ** (age / half_life)
    score = 0.5 ** (age_days / max(1.0, half_life))
    # Anything older than 4 half-lives is essentially stale.
    return max(0.0, min(1.0, score))


def _relevance_score(
    content: str,
    metadata: Dict[str, Any],
    source: str,
) -> float:
    """Heuristic: does the chunk look like a useful search target?"""
    if _is_low_value(content):
        return 0.0
    score = 0.7
    # Has a category / title => better metadata for retrieval.
    if (metadata or {}).get("title"):
        score += 0.1
    if (metadata or {}).get("category"):
        score += 0.05
    # A URL / anchor makes the chunk actionable from a UI perspective.
    if (metadata or {}).get("url"):
        score += 0.05
    # Short snippets with no real content score lower.
    if len(content) < 40:
        score -= 0.2
    return max(0.0, min(1.0, score))


def evaluate_quality(
    record: Dict[str, Any],
    *,
    source: str,
    now_epoch: Optional[float] = None,
) -> QualityBreakdown:
    """Compute a quality score for an indexed record.

    `record` is a dict with at least `content`. Optional `metadata`,
    `last_updated` / `original_updated_at` are used to refine the score.
    """
    content = str(record.get("content") or "")
    metadata = dict(record.get("metadata") or {})

    ts = (
        record.get("last_updated")
        or record.get("original_updated_at")
        or record.get("updated_at")
        or metadata.get("last_updated")
        or metadata.get("updated_at")
    )
    if now_epoch is None:
        now_epoch = time.time()

    completeness = _completeness_score(content, metadata)
    accuracy = _accuracy_score(content, source)
    # If the content is too thin or boilerplate to be useful, short-circuit:
    # we want a 0.0 overall, not a deceptively-positive blend driven by a
    # default freshness score.
    if completeness <= 0.0 or accuracy <= 0.0:
        return QualityBreakdown(
            completeness=completeness,
            accuracy=accuracy,
            freshness=0.0,
            relevance=_relevance_score(content, metadata, source),
            overall=0.0,
            reasons=["low_value"],
        )

    freshness = _freshness_score(ts, source, now_epoch)
    relevance = _relevance_score(content, metadata, source)

    reasons: list = []
    if completeness < 0.5:
        reasons.append("thin_content")
    if freshness < 0.4:
        reasons.append("stale")
    if relevance < 0.4:
        reasons.append("low_signal")

    # Weighted blend. The weights reflect which signal is most actionable:
    # accuracy > relevance > completeness > freshness.
    overall = (
        0.35 * accuracy
        + 0.30 * relevance
        + 0.20 * completeness
        + 0.15 * freshness
    )

    return QualityBreakdown(
        completeness=completeness,
        accuracy=accuracy,
        freshness=freshness,
        relevance=relevance,
        overall=max(0.0, min(1.0, overall)),
        reasons=reasons,
    )


def score_for_indexed_record(
    record: Dict[str, Any],
    source: str,
) -> Dict[str, Any]:
    """Convenience wrapper returning a dict ready for the indexer to persist."""
    breakdown = evaluate_quality(record, source=source)
    return {
        "quality_score": breakdown.overall,
        "quality_components": breakdown.to_dict(),
        "quality_reasons": breakdown.reasons,
    }


__all__ = [
    "QualityBreakdown",
    "evaluate_quality",
    "score_for_indexed_record",
]
