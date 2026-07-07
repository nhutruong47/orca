# Knowledge Document: mock_ai.py (Chunk 4/7)

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
  "chunk_index": 3,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
roduction_member = _find_member(members, ["rang", "sản xuất", "senior"])
    qc_member = _find_member(members, ["qc", "kiểm", "quality"])

    return PlanDraftResponse(
        goalTitle=title,
        outputTarget=output,
        deadline=deadline,
        priority=_priority_number(fields.get("priority")),
        tasks=[
            TaskDraft(
                title="Chuẩn bị kế hoạch sản xuất",
                description="Xác nhận yêu cầu, thời hạn và phân chia đầu việc trước khi thực hiện.",
                priority=3,
                workload=1.5,
                suggestedReason="Task điều phối ban đầu, có thể giao cho trưởng nhóm.",
            ),
            TaskDraft(
                title=f"Thực hiện sản xuất {product}",
                description=f"Thực hiện sản xuất theo yêu cầu: {output}.",
                priority=4,
                workload=6.0,
                suggestedAssigneeId=production_member["id"] if production_member else None,
                suggestedAssigneeName=production_member["name"] if production_member else None,
                suggestedReason=production_member["reason"] if production_member else "Chưa có thành viên có nhãn sản xuất/rang rõ ràng.",
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

```
