# Knowledge Document: gemini_ai.py (Chunk 19/24)

## Metadata
```json
{
  "file_path": "ai-service/app/gemini_ai.py",
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
  "chunk_index": 18,
  "total_chunks": 24
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
atch_text(task_scope_text_for_matching(task))
        if any(keyword in text for keyword in ["dong goi", "bao bi", "dan nhan", "thanh pham"]):
            return index
    return None


def _require_task_signatures_equal(draft: PlanDraftResponse, original: PlanDraftResponse) -> None:
    _require_equal(len(draft.tasks), len(original.tasks), "Gemini revise changed task count without instruction.")
    for index, original_task in enumerate(original.tasks):
        revised_task = draft.tasks[index]
        _require_equal(revised_task.title, original_task.title, f"Gemini revise changed task title at index {index}.")
        _require_equal(
            revised_task.description,
            original_task.description,
            f"Gemini revise changed task description at index {index}.",
        )
        _require_equal(
            revised_task.priority,
            original_task.priority,
            f"Gemini revise changed task priority at index {index}.",
        )
        _require_equal(
            revised_task.workload,
            original_task.workload,
            f"Gemini revise changed task workload at index {index}.",
        )


def _require_equal(actual: Any, expected: Any, message: str) -> None:
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

```
