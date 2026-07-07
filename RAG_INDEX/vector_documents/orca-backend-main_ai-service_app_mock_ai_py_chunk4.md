# Knowledge Document: mock_ai.py (Chunk 5/7)

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
  "chunk_index": 4,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
c liên quan")
    assignee = _find_member(members, ["vệ sinh", "dọn", "operation", "vận hành"])

    return PlanDraftResponse(
        goalTitle=title,
        outputTarget=f"Hoàn thành công việc vận hành tại {area}",
        deadline=deadline,
        priority=_priority_number(fields.get("priority")),
        tasks=[
            TaskDraft(
                title=f"Thực hiện công việc tại {area}",
                description="Thực hiện công việc theo yêu cầu đã được mô tả.",
                priority=2,
                workload=1.0,
                suggestedAssigneeId=assignee["id"] if assignee else None,
                suggestedAssigneeName=assignee["name"] if assignee else None,
                suggestedReason=assignee["reason"] if assignee else "Chưa có thành viên có nhãn vận hành phù hợp.",
            ),
            TaskDraft(
                title="Kiểm tra lại sau khi hoàn thành",
                description="Xác nhận khu vực đã đạt yêu cầu trước khi đóng task.",
                priority=2,
                workload=0.5,
            ),
        ],
    )


def _infer_deadline(normalized: str) -> str | None:
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

```
