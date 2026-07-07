# Knowledge Document: gemini_ai.py (Chunk 11/24)

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
  "chunk_index": 10,
  "total_chunks": 24
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
sted_removed_task_query(instruction)
    if removed_task_query is not None:
        task_index = _find_task_index_by_query(original.tasks, removed_task_query)
        if task_index is not None:
            draft = original.model_copy(deep=True)
            draft.tasks.pop(task_index)
            return draft

    renamed_task = _requested_renamed_task(instruction)
    if renamed_task is not None:
        current_title, new_title = renamed_task
        task_index = _find_task_index_by_query(original.tasks, current_title)
        if task_index is not None:
            draft = original.model_copy(deep=True)
            task = draft.tasks[task_index]
            task.title = new_title
            task.description = f"Thực hiện công việc {new_title.lower()} theo yêu cầu đã cập nhật."
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
                    suggestedAssigneeName=original_task.suggestedAssigneeName,
                    suggestedReason=original_task.suggestedReason,
                ),
            ]

```
