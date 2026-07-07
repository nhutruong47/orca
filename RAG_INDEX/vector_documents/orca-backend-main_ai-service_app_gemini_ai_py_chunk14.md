# Knowledge Document: gemini_ai.py (Chunk 15/21)

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
  "chunk_index": 14,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
      return None
    if not _mentions_any(instruction, ["rut gon", "giam", "con", "chi"]):
        return None

    match = re.search(r"(\d+)\s*task", instruction)
    if not match:
        return None
    return max(1, int(match.group(1)))


def _requested_deadline(instruction: str) -> str | None:
    if not _mentions_any(instruction, ["deadline", "han", "thoi han", "doi"]):
        return None
    time_match = re.search(r"(\d{1,2})(?::|h)(\d{2})?", instruction)
    if not time_match:
        return None
    hour = int(time_match.group(1))
    minute = int(time_match.group(2) or 0)
    if hour > 23 or minute > 59:
        return None
    if "hom nay" in instruction:
        return _local_now().replace(hour=hour, minute=minute, second=0, microsecond=0).isoformat()
    return None


def _validate_priority_revise(draft: PlanDraftResponse, original: PlanDraftResponse, instruction: str) -> None:
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

```
