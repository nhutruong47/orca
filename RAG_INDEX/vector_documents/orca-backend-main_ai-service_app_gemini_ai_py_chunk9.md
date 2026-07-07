# Knowledge Document: gemini_ai.py (Chunk 10/21)

## Metadata
```json
{
  "file_path": "orca-backend-main/ai-service/app/gemini_ai.py",
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
  "chunk_index": 9,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
raft.tasks):
                    draft.tasks[index].priority = 5
            return draft

    if _mentions_any(instruction, ["them"]) and _has_qc_intent(instruction):
        draft = original.model_copy(deep=True)
        assignee = _find_member_by_labels(
            {member.userId: member for member in request.members},
            ["qc", "kiem", "kiem tra", "chat luong", "quality"],
        )
        task = TaskDraft(
            title="Kiểm tra chất lượng cuối cùng",
            description="Kiểm tra chất lượng tổng thể và xác nhận thành phẩm đạt yêu cầu trước khi hoàn tất.",
            priority=3,
            workload=1.0,
        )
        if assignee is not None:
            task.suggestedAssigneeId = assignee.userId
            task.suggestedAssigneeName = assignee.fullName or assignee.username
            task.suggestedReason = "Phù hợp vì có nhãn QC/kiểm tra chất lượng."
        draft.tasks.append(task)
        return draft

    if _mentions_any(instruction, ["tach"]) and _mentions_any(instruction, ["dong goi"]):
        packaging_index = _find_packaging_task_index(original.tasks)
        if packaging_index is not None:
            draft = original.model_copy(deep=True)
            original_task = original.tasks[packaging_index]
            first_workload = max(round(original_task.workload / 2, 2), 0.25)
            second_workload = max(round(original_task.workload - first_workload, 2), 0.25)
            split_tasks = [
                TaskDraft(
                    title="Chuẩn bị bao bì và nhãn thành phẩm",
                    description="Chuẩn bị bao bì, nhãn và khu vực đóng gói trước khi xử lý thành phẩm.",
                    priority=original_task.priority,
                    workload=first_workload,
                    suggestedAssigneeId=original_task.suggestedAssigneeId,
                    suggestedAssigneeName=original_task.suggestedAssigneeName,
                    suggestedReason=original_task.suggestedReason,
                ),
                TaskDraft(
                    title="Đóng gói và kiểm tra bao gói thành phẩm",
                    description="Đóng gói thành phẩm, kiểm tra bao gói và sẵn sàng bàn giao.",
                    priority=original_task.priority,
                    workload=second_workload,
                    suggestedAssigneeId=original_task.suggestedAssigneeId,

```
