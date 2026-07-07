# Knowledge Document: gemini_ai.py (Chunk 8/21)

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
  "chunk_index": 7,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
ks) != requested_task_count:
            raise GeminiReviseError(
                f"Gemini revise returned {len(draft.tasks)} tasks, expected {requested_task_count} tasks."
            )
    elif not _mentions_any(instruction, ["them", "xoa", "rut gon", "tach", "task", "cong viec"]):
        _require_task_signatures_equal(draft, original)

    requested_deadline = _requested_deadline(instruction)
    if requested_deadline is not None:
        _require_equal(draft.deadline, requested_deadline, "Gemini revise did not apply requested deadline.")
    elif not _mentions_any(instruction, ["deadline", "han", "thoi han", "doi deadline", "doi han"]):
        _require_equal(draft.deadline, original.deadline, "Gemini revise changed deadline without instruction.")

    if _mentions_any(instruction, ["uu tien", "priority"]) and _mentions_any(instruction, ["cao nhat", "cao"]):
        _validate_priority_revise(draft, original, instruction)

    return draft


def _normalize_revise_output(draft: PlanDraftResponse, request: ReviseRequest) -> PlanDraftResponse:
    instruction = _normalize_revise_instruction(request.instruction)
    original = request.draft

    requested_task_count = _requested_task_count(instruction)
    if requested_task_count is not None and requested_task_count <= len(original.tasks):
        draft.goalTitle = original.goalTitle
        draft.outputTarget = original.outputTarget
        draft.deadline = original.deadline
        draft.priority = original.priority
        draft.tasks = [task.model_copy(deep=True) for task in original.tasks[:requested_task_count]]
        return draft

    requested_deadline = _requested_deadline(instruction)
    if requested_deadline is not None:
        draft.goalTitle = original.goalTitle
        draft.outputTarget = original.outputTarget
        draft.priority = original.priority
        draft.deadline = requested_deadline
        draft.tasks = [task.model_copy(deep=True) for task in original.tasks]
        return draft

    if _mentions_any(instruction, ["uu tien", "priority"]) and _mentions_any(instruction, ["cao nhat", "cao"]):
        target_indexes = _target_task_indexes(original, instruction)
        if target_indexes:
            draft.goalTitle = original.goalTitle
            draft.outputTarget = original.outputTarget
            draft.deadline = original.deadline

```
