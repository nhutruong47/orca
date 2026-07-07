# Knowledge Document: gemini_ai.py (Chunk 7/21)

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
  "chunk_index": 6,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
    draft.tasks = [_sanitize_assignee(task, allowed_members) for task in draft.tasks]

    if request.intent == "PRODUCTION_PLAN":
        draft.tasks = [_fill_missing_production_assignee(task, allowed_members) for task in draft.tasks]
        draft.tasks = [_sanitize_production_assignee(task, allowed_members) for task in draft.tasks]
        _require_task_count(draft.tasks, minimum=3, maximum=6)
    elif request.intent == "OPERATION_TASK":
        _require_task_count(draft.tasks, minimum=2, maximum=4)
        draft.tasks = [_sanitize_operation_assignee(task, allowed_members) for task in draft.tasks]
        text = _operation_scope_text(draft)
        forbidden_terms = ["sản xuất", "rang 120", "kg arabica", "kg robusta"]
        found_terms = [term for term in forbidden_terms if term in text]
        if found_terms:
            raise GeminiPlanError(f"Gemini plan added production terms to an operation task: {found_terms}.")

    return draft


def _validate_revise_output(draft: PlanDraftResponse, request: ReviseRequest) -> PlanDraftResponse:
    original = request.draft
    instruction = _normalize_revise_instruction(request.instruction)
    allowed_members = {member.userId: member for member in request.members}
    draft.tasks = [_sanitize_assignee(task, allowed_members) for task in draft.tasks]

    if not _mentions_any(instruction, ["tieu de", "title", "goal", "muc tieu", "output", "ket qua"]):
        _require_equal(draft.goalTitle, original.goalTitle, "Gemini revise changed goalTitle without instruction.")
        _require_equal(draft.outputTarget, original.outputTarget, "Gemini revise changed outputTarget without instruction.")

    if not _mentions_any(instruction, ["priority", "uu tien"]):
        _require_equal(draft.priority, original.priority, "Gemini revise changed goal priority without instruction.")

    requested_task_count = _requested_task_count(instruction)
    if requested_task_count is not None:
        if len(draft.tasks) != requested_task_count:
            raise GeminiReviseError(
                f"Gemini revise returned {len(draft.tasks)} tasks, expected {requested_task_count} tasks."
            )
    elif not _mentions_any(instruction, ["them", "xoa", "rut gon", "tach", "task", "cong viec"]):
        _require_task_signatures_equal(draft, original)

    requested_deadline = _requested_deadline(instruction)

```
