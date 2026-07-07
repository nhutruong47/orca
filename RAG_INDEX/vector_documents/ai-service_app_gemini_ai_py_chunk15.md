# Knowledge Document: gemini_ai.py (Chunk 16/24)

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
  "chunk_index": 15,
  "total_chunks": 24
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
equested_added_task_title(instruction: str) -> str | None:
    if "them" not in instruction:
        return None

    patterns = [
        r"\bthem(?:\s+\d+)?\s+(?:muc|task|cong viec)(?:\s+nua)?(?:\s+(?:la|ve|cho))?\s*[:\-]?\s*(.+)$",
        r"\bthem\s+(?:muc|task|cong viec)\s*[:\-]\s*(.+)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, instruction)
        if not match:
            continue
        title = match.group(1).strip(" .,:;-")
        title = re.sub(r"^(?:muc|task|cong viec)\s*(?:so)?\s*\d+\s*(?:la|:|-)?\s*", "", title).strip()
        if not title or title in {"nua", "moi", "mot muc", "mot task", "mot cong viec"}:
            return None
        return _format_task_title(title)
    return None


def _requested_removed_task_query(instruction: str) -> str | None:
    patterns = [
        r"\b(?:xoa|bo|loai bo)(?:\s+di)?\s+(?:muc|task|cong viec)?\s*[:\-]?\s*(.+)$",
        r"\b(?:xoa|bo)\s+(.+?)\s+(?:di|ra khoi danh sach)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, instruction)
        if match:
            query = match.group(1).strip(" .,:;-")
            if query:
                return query
    return None


def _requested_renamed_task(instruction: str) -> tuple[str, str] | None:
    patterns = [
        r"\b(?:doi ten|sua|doi)\s+(?:muc|task|cong viec)?\s*(.+?)\s+(?:thanh|sang)\s+(.+)$",
        r"\b(?:muc|task|cong viec)\s+(.+?)\s+(?:doi|sua)\s+(?:thanh|sang)\s+(.+)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, instruction)
        if not match:
            continue
        current_title = match.group(1).strip(" .,:;-")
        new_title = match.group(2).strip(" .,:;-")
        if current_title and new_title:
            return current_title, _format_task_title(new_title)
    return None


def _find_task_index_by_query(tasks: list[TaskDraft], query: str) -> int | None:
    normalized_query = _normalize_match_text(query)
    if not normalized_query:
        return None

    number_match = re.fullmatch(r"(?:muc|task|cong viec)?\s*(?:so)?\s*(\d+)", normalized_query)
    if number_match:
        requested_index = int(number_match.group(1)) - 1
        return requested_index if 0 <= requested_index < len(tasks) else None

    if normalized_query in {"cuoi", "muc cuoi", "task cuoi", "cong viec cuoi"}:
        return len(tasks) - 1 if tasks else None


```
