# Knowledge Document: mock_ai.py (Chunk 7/8)

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
  "chunk_index": 6,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
e:
    now = datetime.now().replace(second=0, microsecond=0)

    explicit_time = _extract_time(normalized)
    if "hôm nay" in normalized:
        hour, minute = explicit_time or (17, 0)
        return now.replace(hour=hour, minute=minute).isoformat()
    if "chiều nay" in normalized:
        hour, minute = explicit_time or (14, 0)
        return now.replace(hour=hour, minute=minute).isoformat()
    if "sáng mai" in normalized:
        hour, minute = explicit_time or (9, 0)
        return (now + timedelta(days=1)).replace(hour=hour, minute=minute).isoformat()
    if "chiều mai" in normalized:
        hour, minute = explicit_time or (14, 0)
        return (now + timedelta(days=1)).replace(hour=hour, minute=minute).isoformat()
    if "ngày mai" in normalized or "mai" in normalized:
        hour, minute = explicit_time or (17, 0)
        return (now + timedelta(days=1)).replace(hour=hour, minute=minute).isoformat()
    duration_match = re.search(r"trong\s+(\d+)\s*ngày", normalized)
    if duration_match:
        days = int(duration_match.group(1))
        hour, minute = explicit_time or (17, 0)
        return (now + timedelta(days=days)).replace(hour=hour, minute=minute).isoformat()
    if "thứ hai tuần sau" in normalized or "thứ 2 tuần sau" in normalized:
        days_ahead = (7 - now.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        hour, minute = explicit_time or (17, 0)
        return (now + timedelta(days=days_ahead)).replace(hour=hour, minute=minute).isoformat()
    if "thứ sáu" in normalized or "thứ 6" in normalized:
        days_ahead = (4 - now.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        hour, minute = explicit_time or (17, 0)
        return (now + timedelta(days=days_ahead)).replace(hour=hour, minute=minute).isoformat()
    if "trước" in normalized:
        if explicit_time:
            hour, minute = explicit_time
            return now.replace(hour=hour, minute=minute).isoformat()
        return (now + timedelta(days=3)).replace(hour=17, minute=0).isoformat()
    return None


def _extract_time(normalized: str) -> tuple[int, int] | None:
    time_match = re.search(r"(\d{1,2})(?::|h)(\d{2})?", normalized)
    if not time_match:
        return None
    hour = int(time_match.group(1))
    minute = int(time_match.group(2) or 0)
    if hour > 23 or minute > 59:
        return None

```
