# Knowledge Document: gemini_ai.py (Chunk 4/21)

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
  "chunk_index": 3,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
asks": [
    {{
      "title": "string",
      "description": "string",
      "priority": integer from 1 to 5,
      "workload": number greater than 0,
      "suggestedAssigneeId": "team member userId or null",
      "suggestedAssigneeName": "matching team member fullName/username or null",
      "suggestedReason": "Vietnamese reason or null"
    }}
  ]
}}

Hard rules:
- Return {task_count_rule}.
- deadline must be copied from extracted fields.deadline exactly when present.
- priority must be an integer: 1 lowest, 3 medium, 5 highest.
- workload is estimated effort hours, must be greater than 0.
- suggestedAssigneeId should strongly be suggested using one of the provided team member userId values.
- If no perfectly matching member exists, you can still suggest an assignee if their jobLabels are somewhat related, or if it is a general task.
- Match members to tasks based on their jobLabels (e.g. "Rang xay" matches roasting tasks).
- Never invent a person, username, full name, or userId.
- suggestedAssigneeName must match the selected member's fullName when available, otherwise username.
- Keep the draft in Vietnamese.
- The draft is not saved data, so do not include id, status, createdAt, totalTasks, or database fields.

Intent-specific rules:
- PRODUCTION_PLAN: create production workflow tasks, such as preparation, execution, checking/QC, and completion.
- PRODUCTION_PLAN: always include at least one QC/kiểm tra chất lượng task.
- PRODUCTION_PLAN: goalTitle and outputTarget must include productName, quantity, and unit when present.
- OPERATION_TASK: create only internal operation tasks based on title/area.
- OPERATION_TASK: do not create production/roasting/quantity tasks unless the extracted title explicitly says so.

Now produce the draft JSON.
""".strip()


def _build_revise_prompt(request: ReviseRequest) -> str:
    draft_json = json.dumps(request.draft.model_dump(), ensure_ascii=False, indent=2)
    members_json = json.dumps([member.model_dump() for member in request.members], ensure_ascii=False, indent=2)
    now = _local_now()

    return f"""
You are ORCA AI v2 revise module for a Vietnamese workshop/task management app.

Your only job is to revise an existing draft Goal/Tasks according to the user's revision instruction.
Do not classify intent. Do not create a new plan from scratch. Do not save data. Do not explain.


```
