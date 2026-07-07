# Knowledge Document: gemini_ai.py (Chunk 18/24)

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
  "chunk_index": 17,
  "total_chunks": 24
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
se(draft: PlanDraftResponse, original: PlanDraftResponse, instruction: str) -> None:
    target_indexes = _target_task_indexes(original, instruction)
    if not target_indexes:
        return

    if not any(draft.tasks[index].priority == 5 for index in target_indexes if index < len(draft.tasks)):
        raise GeminiReviseError("Gemini revise did not increase the requested task priority to 5.")

    for index, original_task in enumerate(original.tasks):
        if index >= len(draft.tasks) or index in target_indexes:
            continue
        revised_task = draft.tasks[index]
        if revised_task.priority != original_task.priority:
            raise GeminiReviseError(f"Gemini revise changed unrelated task priority at index {index}.")


def _target_task_indexes(draft: PlanDraftResponse, instruction: str) -> list[int]:
    if "rang" in instruction:
        keywords = ["rang"]
    elif "san xuat" in instruction:
        keywords = ["san xuat", "thuc hien"]
    elif "dong goi" in instruction:
        keywords = ["dong goi"]
    elif _has_qc_intent(instruction):
        keywords = ["qc", "kiem tra", "chat luong"]
    else:
        keywords = []

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

```
