# Knowledge Document: mock_ai.py (Chunk 8/8)

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
  "chunk_index": 7,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
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
            name = member.fullName or member.username
            return {
                "id": member.userId,
                "name": name,
                "reason": f"Phù hợp vì có nhãn: {', '.join(member.jobLabels)}",
            }
    return None


def _find_priority_target_task(tasks: list[TaskDraft], instruction: str) -> TaskDraft | None:
    if "rang" in instruction:
        keywords = ["rang"]
    elif "sản xuất" in instruction:
        keywords = ["sản xuất", "thực hiện"]
    else:
        keywords = ["rang", "sản xuất", "thực hiện"]

    for task in tasks:
        title = task.title.lower()
        if any(keyword in title for keyword in keywords):
            return task

    for task in tasks:
        text = f"{task.title} {task.description}".lower()
        if any(keyword in text for keyword in keywords):
            return task

    return None

```
