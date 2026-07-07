# Knowledge Document: gemini_ai.py (Chunk 17/21)

## Metadata
```json
{
  "file_path": "orca-backend-main/ai-service/app/gemini_ai.py",
  "language": "py",
  "module": "app",
  "business_domain": "chat",
  "tags": [
    "chat",
    "inventory",
    "production",
    "authorization"
  ],
  "logical_type": "Generic",
  "chunk_index": 16,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
quire_equal(actual: Any, expected: Any, message: str) -> None:
    if actual != expected:
        raise GeminiReviseError(message)


def _mentions_any(text: str, keywords: list[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def _is_ambiguous_revise_instruction(instruction: str) -> bool:
    normalized = _normalize_revise_instruction(instruction).strip()
    ambiguous = [
        "lam lai cho hay hon",
        "lam hay hon",
        "sua cho hay hon",
        "toi uu hon",
        "on hon",
    ]
    return normalized in ambiguous


def _draft_text(draft: PlanDraftResponse) -> str:
    parts = [draft.goalTitle, draft.outputTarget, draft.deadline or ""]
    for task in draft.tasks:
        parts.extend([task.title, task.description, task.suggestedReason or ""])
    return " ".join(parts).lower()


def task_text_for_matching(task: TaskDraft) -> str:
    return " ".join([task.title, task.description, task.suggestedReason or ""]).lower()


def task_scope_text_for_matching(task: TaskDraft) -> str:
    return " ".join([task.title, task.description]).lower()


def _normalize_match_text(value: str) -> str:
    text = value.lower().replace("đ", "d")
    text = unicodedata.normalize("NFKD", text)
    return "".join(char for char in text if not unicodedata.combining(char))


def _normalize_revise_instruction(value: str) -> str:
    text = _normalize_match_text(value)
    replacements = {
        r"\b(taks|tas|taskk|tsk)\b": "task",
        r"\b(dedline|deadlin|dealin|dealine|dedlin)\b": "deadline",
        r"\buu\s*tin\b": "uu tien",
        r"\buu\s*tienn\b": "uu tien",
        r"\bu\s*tien\b": "uu tien",
        r"\brut\s*gon\b": "rut gon",
        r"\bcao\s*nhat\b": "cao nhat",
    }
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)
    return re.sub(r"\s+", " ", text).strip()


def _operation_scope_text(draft: PlanDraftResponse) -> str:
    parts = [draft.goalTitle, draft.outputTarget]
    for task in draft.tasks:
        parts.extend([task.title, task.description])
    return " ".join(parts).lower()


def _is_blank(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str) and not value.strip():
        return True
    return False


def _is_generic_product_name(value: Any) -> bool:
    if not isinstance(value, str):
        return False

```
