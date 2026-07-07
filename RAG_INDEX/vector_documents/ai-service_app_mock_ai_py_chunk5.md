# Knowledge Document: mock_ai.py (Chunk 6/8)

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
  "chunk_index": 5,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
eason"] if production_member else "Chưa có thành viên có nhãn sản xuất/rang rõ ràng.",
            ),
            TaskDraft(
                title="Kiểm tra kết quả hoàn thành",
                description="Kiểm tra số lượng và chất lượng trước khi đóng mục tiêu.",
                priority=3,
                workload=1.5,
                suggestedAssigneeId=qc_member["id"] if qc_member else None,
                suggestedAssigneeName=qc_member["name"] if qc_member else None,
                suggestedReason=qc_member["reason"] if qc_member else "Chưa có thành viên có nhãn QC rõ ràng.",
            ),
        ],
    )


def _plan_operation(fields: dict[str, Any], members: list[TeamMemberContext]) -> PlanDraftResponse:
    title = fields.get("title") or "Công việc vận hành"
    deadline = fields.get("deadline")
    area = fields.get("area", "khu vực liên quan")
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

```
