# Knowledge Document: gemini_ai.py (Chunk 12/24)

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
  "chunk_index": 11,
  "total_chunks": 24
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
phẩm, kiểm tra bao gói và sẵn sàng bàn giao.",
                    priority=original_task.priority,
                    workload=second_workload,
                    suggestedAssigneeId=original_task.suggestedAssigneeId,
                    suggestedAssigneeName=original_task.suggestedAssigneeName,
                    suggestedReason=original_task.suggestedReason,
                ),
            ]
            draft.tasks = draft.tasks[:packaging_index] + split_tasks + draft.tasks[packaging_index + 1 :]
            return draft

    return None


def _sanitize_assignee(task: TaskDraft, allowed_members: dict[str, Any]) -> TaskDraft:
    if not task.suggestedAssigneeId:
        task.suggestedAssigneeName = None
        return task

    member = allowed_members.get(task.suggestedAssigneeId)
    if member is None:
        task.suggestedAssigneeId = None
        task.suggestedAssigneeName = None
        task.suggestedReason = "AI gợi ý thành viên không thuộc team nên hệ thống đã bỏ gợi ý này."
        return task

    task.suggestedAssigneeName = member.fullName or member.username
    return task


def _sanitize_operation_assignee(task: TaskDraft, allowed_members: dict[str, Any]) -> TaskDraft:
    if not task.suggestedAssigneeId:
        return task

    member = allowed_members.get(task.suggestedAssigneeId)
    if member is None:
        return task

    labels = _normalize_match_text(" ".join(member.jobLabels))
    operation_keywords = ["ve sinh", "don", "operation", "van hanh", "dong goi", "sap xep"]
    if any(keyword in labels for keyword in operation_keywords):
        return task

    task.suggestedAssigneeId = None
    task.suggestedAssigneeName = None
    task.suggestedReason = "Chưa có thành viên có nhãn vận hành phù hợp."
    return task


def _sanitize_production_assignee(task: TaskDraft, allowed_members: dict[str, Any]) -> TaskDraft:
    if not task.suggestedAssigneeId:
        return task

    member = allowed_members.get(task.suggestedAssigneeId)
    if member is None:
        return task

    labels = _normalize_match_text(" ".join(member.jobLabels))
    if not labels.strip():
        return _clear_assignee(task, "Chưa có thành viên có nhãn công việc phù hợp.")

    text = _normalize_match_text(task_scope_text_for_matching(task))
    packaging_keywords = ["dong goi", "dan nhan", "bao bi", "pack", "label", "packaging", "thanh pham", "dan tem"]

```
