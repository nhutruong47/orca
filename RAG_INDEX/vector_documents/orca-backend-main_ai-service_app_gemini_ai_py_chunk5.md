# Knowledge Document: gemini_ai.py (Chunk 6/21)

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
  "chunk_index": 5,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
oo subjective, return the current draft unchanged.
- Never save data and never include id, status, createdAt, totalTasks, or database fields.
- suggestedAssigneeId is optional and must be one of the provided team member userId values.
- If no suitable member exists, set suggestedAssigneeId and suggestedAssigneeName to null.
- A member with empty jobLabels is not suitable for any specialized task.
- Never invent a person, username, full name, or userId.
- Keep the draft in Vietnamese.

Deadline rules:
- Return deadline as ISO local datetime string without timezone offset, e.g. "2026-06-09T18:00:00".
- Resolve Vietnamese relative dates using Current local datetime.
- "hôm nay" means today.
- If exact time is present, use that exact time.

Now return the revised draft JSON.
""".strip()


def _validate_plan_input(request: PlanRequest) -> None:
    if request.intent == "UNKNOWN":
        raise GeminiPlanInputError("Cannot create a plan for UNKNOWN intent.")

    fields = request.fields or {}
    if request.intent == "PRODUCTION_PLAN":
        required = ["productName", "quantity", "unit", "deadline"]
    elif request.intent == "OPERATION_TASK":
        required = ["title", "deadline"]
    else:
        raise GeminiPlanInputError(f"Unsupported intent for plan: {request.intent}")

    missing = [field for field in required if _is_blank(fields.get(field))]
    if request.intent == "PRODUCTION_PLAN" and _is_generic_product_name(fields.get("productName")):
        missing.append("productName")
    if missing:
        raise GeminiPlanInputError(f"Cannot create plan because required fields are missing: {', '.join(missing)}.")


def _validate_plan_output(draft: PlanDraftResponse, request: PlanRequest) -> PlanDraftResponse:
    fields = request.fields or {}
    if fields.get("deadline") and draft.deadline != fields["deadline"]:
        raise GeminiPlanError("Gemini plan changed the extracted deadline.")

    allowed_members = {member.userId: member for member in request.members}
    draft.tasks = [_sanitize_assignee(task, allowed_members) for task in draft.tasks]

    if request.intent == "PRODUCTION_PLAN":
        draft.tasks = [_fill_missing_production_assignee(task, allowed_members) for task in draft.tasks]
        draft.tasks = [_sanitize_production_assignee(task, allowed_members) for task in draft.tasks]
        _require_task_count(draft.tasks, minimum=3, maximum=6)

```
