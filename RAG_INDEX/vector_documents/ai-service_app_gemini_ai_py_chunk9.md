# Knowledge Document: gemini_ai.py (Chunk 10/24)

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
  "chunk_index": 9,
  "total_chunks": 24
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
)
            for index in target_indexes:
                if index < len(draft.tasks):
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

    added_task_title = _requested_added_task_title(instruction)
    if added_task_title is not None:
        draft = original.model_copy(deep=True)
        task = TaskDraft(
            title=added_task_title,
            description=f"Thực hiện công việc {added_task_title.lower()} theo yêu cầu của kế hoạch.",
            priority=3,
            workload=1.0,
        )
        normalized_title = _normalize_match_text(added_task_title)
        if _mentions_any(normalized_title, ["van chuyen", "giao hang", "ban giao", "logistics"]):
            assignee = _find_member_by_labels(
                {member.userId: member for member in request.members},
                ["van chuyen", "giao hang", "logistics", "kho", "ship"],
            )
            task = _assign_if_found(task, assignee, "Phù hợp vì có nhãn vận chuyển/kho/giao hàng.")
        draft.tasks.append(task)
        return draft

    removed_task_query = _requested_removed_task_query(instruction)
    if removed_task_query is not None:
        task_index = _find_task_index_by_query(original.tasks, removed_task_query)
        if task_index is not None:
            draft = original.model_copy(deep=True)
            draft.tasks.pop(task_index)
            return draft

    renamed_task = _requested_renamed_task(instruction)
    if renamed_task is not None:

```
