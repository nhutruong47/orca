# Knowledge Document: gemini_ai.py (Chunk 17/24)

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
  "chunk_index": 16,
  "total_chunks": 24
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
    return None

    number_match = re.fullmatch(r"(?:muc|task|cong viec)?\s*(?:so)?\s*(\d+)", normalized_query)
    if number_match:
        requested_index = int(number_match.group(1)) - 1
        return requested_index if 0 <= requested_index < len(tasks) else None

    if normalized_query in {"cuoi", "muc cuoi", "task cuoi", "cong viec cuoi"}:
        return len(tasks) - 1 if tasks else None

    for index, task in enumerate(tasks):
        if normalized_query in _normalize_match_text(task.title):
            return index
    for index, task in enumerate(tasks):
        if normalized_query in _normalize_match_text(task_scope_text_for_matching(task)):
            return index
    return None


def _format_task_title(value: str) -> str:
    normalized = _normalize_match_text(value).strip()
    known_titles = {
        "van chuyen": "Vận chuyển",
        "giao hang": "Giao hàng",
        "giao hang thanh pham": "Giao hàng thành phẩm",
        "ban giao": "Bàn giao",
        "dong goi": "Đóng gói",
        "kiem tra chat luong": "Kiểm tra chất lượng",
    }
    if normalized in known_titles:
        return known_titles[normalized]
    return value[0].upper() + value[1:]


def _is_task_revision_instruction(instruction: str) -> bool:
    return _mentions_any(
        instruction,
        ["them", "xoa", "bo", "loai bo", "sua", "doi", "tach", "task", "cong viec", "muc"],
    )


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


```
