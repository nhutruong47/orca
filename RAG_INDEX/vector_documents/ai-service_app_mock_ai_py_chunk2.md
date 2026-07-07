# Knowledge Document: mock_ai.py (Chunk 3/8)

## Metadata
```json
{
  "file_path": "ai-service/app/mock_ai.py",
  "language": "py",
  "module": "app",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
?\s*(?:số)?\s*(\d+)", query)
        if number_match:
            requested_index = int(number_match.group(1)) - 1
            task_index = requested_index if 0 <= requested_index < len(draft.tasks) else None
        elif query in {"cuối", "mục cuối", "task cuối", "công việc cuối"}:
            task_index = len(draft.tasks) - 1 if draft.tasks else None
        else:
            task_index = next(
                (index for index, task in enumerate(draft.tasks) if query in f"{task.title} {task.description}".lower()),
                None,
            )
        if task_index is not None:
            draft.tasks.pop(task_index)
            return draft

    rename_task_match = re.search(
        r"\b(?:đổi tên|sửa|đổi)\s+(?:mục|task|công việc)?\s*(.+?)\s+(?:thành|sang)\s+(.+)$",
        instruction,
    )
    if rename_task_match:
        current_title = rename_task_match.group(1).strip(" .,:;-").lower()
        new_title = rename_task_match.group(2).strip(" .,:;-")
        task = next(
            (item for item in draft.tasks if current_title in f"{item.title} {item.description}".lower()),
            None,
        )
        if task is not None and new_title:
            task.title = new_title[0].upper() + new_title[1:]
            task.description = f"Thực hiện công việc {new_title.lower()} theo yêu cầu đã cập nhật."
            return draft

    new_deadline = _infer_deadline(instruction)
    if new_deadline and ("deadline" in instruction or "hạn" in instruction or "đổi" in instruction):
        draft.deadline = new_deadline
        return draft

    priority_match = re.search(r"(cao nhất|ưu tiên cao|priority cao)", instruction)
    if priority_match:
        target = _find_priority_target_task(draft.tasks, instruction)
        if target:
            target.priority = 5
        return draft

    return draft


def _extract_production(text: str, normalized: str) -> ExtractResponse:
    quantity_match = re.search(r"(\d+(?:[.,]\d+)?)\s*(kg|hộp|túi|bao|cái)?", normalized)
    quantity = None
    unit = None
    if quantity_match:
        quantity = float(quantity_match.group(1).replace(",", "."))
        if quantity.is_integer():
            quantity = int(quantity)
        unit = quantity_match.group(2) or "đơn vị"

    product = None
    if "robusta" in normalized:
        product = "Robusta"
    elif "arabica" in normalized:
        product = "Arabica"

```
