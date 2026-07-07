# Knowledge Document: mock_ai.py (Chunk 6/7)

## Metadata
```json
{
  "file_path": "orca-backend-main/ai-service/app/mock_ai.py",
  "language": "py",
  "module": "app",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 5,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
s=1)).replace(hour=hour, minute=minute).isoformat()
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
    return hour, minute


def _production_question(product: str | None, missing: list[str]) -> str:
    parts = []
    if "quantity" in missing:
        parts.append(f"số lượng {product}" if product else "số lượng cần sản xuất")
    if "deadline" in missing:
        parts.append("hạn hoàn thành")
    if "productName" in missing:
        parts.append("sản phẩm cần sản xuất")
    joined = " và ".join(parts)
    return f"Anh/chị cho biết thêm {joined} được không?"


def _priority_number(priority: Any) -> int:
    if priority == "HIGH":
        return 4
    if priority == "LOW":
        return 2
    return 3


def _find_member(members: list[TeamMemberContext], keywords: list[str]) -> dict[str, str] | None:
    for member in members:
        labels = " ".join(member.jobLabels).lower()
        if any(keyword in labels for keyword in keywords):

```
