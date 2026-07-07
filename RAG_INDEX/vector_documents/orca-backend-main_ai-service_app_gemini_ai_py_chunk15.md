# Knowledge Document: gemini_ai.py (Chunk 16/21)

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
  "chunk_index": 15,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
    if not keywords:
        return []

    title_indexes = []
    for index, task in enumerate(draft.tasks):
        text = _normalize_match_text(task.title)
        if "rang" in keywords and _mentions_any(text, ["kiem tra", "chat luong", "qc", "dong goi"]):
            continue
        if any(keyword in text for keyword in keywords):
            title_indexes.append(index)
    if title_indexes:
        return title_indexes

    indexes = []
    for index, task in enumerate(draft.tasks):
        text = _normalize_match_text(task_scope_text_for_matching(task))
        if any(keyword in text for keyword in keywords):
            indexes.append(index)
    return indexes


def _find_packaging_task_index(tasks: list[TaskDraft]) -> int | None:
    for index, task in enumerate(tasks):
        text = _normalize_match_text(task_scope_text_for_matching(task))
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

```
