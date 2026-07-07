# Knowledge Document: gemini_ai.py (Chunk 9/21)

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
  "chunk_index": 8,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
in original.tasks]
        return draft

    if _mentions_any(instruction, ["uu tien", "priority"]) and _mentions_any(instruction, ["cao nhat", "cao"]):
        target_indexes = _target_task_indexes(original, instruction)
        if target_indexes:
            draft.goalTitle = original.goalTitle
            draft.outputTarget = original.outputTarget
            draft.deadline = original.deadline
            draft.priority = original.priority
            draft.tasks = [task.model_copy(deep=True) for task in original.tasks]
            for index in target_indexes:
                if index < len(draft.tasks):
                    draft.tasks[index].priority = 5
            return draft

    draft.goalTitle = original.goalTitle
    draft.outputTarget = original.outputTarget
    draft.deadline = original.deadline
    draft.priority = original.priority
    draft.tasks = [task.model_copy(deep=True) for task in original.tasks]
    return draft


def _revise_with_safe_rule(request: ReviseRequest) -> PlanDraftResponse | None:
    instruction = _normalize_revise_instruction(request.instruction)
    original = request.draft

    requested_task_count = _requested_task_count(instruction)
    if requested_task_count is not None and requested_task_count <= len(original.tasks):
        draft = original.model_copy(deep=True)
        draft.tasks = [task.model_copy(deep=True) for task in original.tasks[:requested_task_count]]
        return draft

    requested_deadline = _requested_deadline(instruction)
    if requested_deadline is not None:
        draft = original.model_copy(deep=True)
        draft.deadline = requested_deadline
        return draft

    if _mentions_any(instruction, ["uu tien", "priority"]) and _mentions_any(instruction, ["cao nhat", "cao"]):
        target_indexes = _target_task_indexes(original, instruction)
        if target_indexes:
            draft = original.model_copy(deep=True)
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

```
