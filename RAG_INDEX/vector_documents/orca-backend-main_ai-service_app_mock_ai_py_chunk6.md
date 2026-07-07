# Knowledge Document: mock_ai.py (Chunk 7/7)

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
  "chunk_index": 6,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
d} được không?"


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
