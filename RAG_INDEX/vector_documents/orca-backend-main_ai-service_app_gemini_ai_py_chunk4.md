# Knowledge Document: gemini_ai.py (Chunk 5/21)

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
  "chunk_index": 4,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
ber.model_dump() for member in request.members], ensure_ascii=False, indent=2)
    now = _local_now()

    return f"""
You are ORCA AI v2 revise module for a Vietnamese workshop/task management app.

Your only job is to revise an existing draft Goal/Tasks according to the user's revision instruction.
Do not classify intent. Do not create a new plan from scratch. Do not save data. Do not explain.

Current local datetime: {now.isoformat(timespec="minutes")}
Timezone: Asia/Ho_Chi_Minh

User revision instruction:
{request.instruction}

Current draft:
{draft_json}

Team members available for suggested assignment:
{members_json}

Output only one JSON object matching this exact schema:
{{
  "goalTitle": "string",
  "outputTarget": "string",
  "deadline": "ISO datetime string or null",
  "priority": integer from 1 to 5,
  "tasks": [
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
- Preserve the existing draft context. This is a revision, not a fresh plan.
- Only change the fields directly requested by the instruction.
- If the instruction asks to reduce to N tasks, return exactly N tasks and keep the most important existing tasks.
- If the instruction asks to add a task, keep all existing tasks unchanged and append exactly one new relevant task.
- If the instruction asks to split a task, keep unrelated tasks unchanged and replace only the target task with exactly two smaller tasks.
- If the instruction asks to change deadline, change only deadline and keep tasks unchanged unless explicitly requested.
- If the instruction asks to increase priority for a specific task type, change only matching task priority.
- If the instruction is unclear or too subjective, return the current draft unchanged.
- Never save data and never include id, status, createdAt, totalTasks, or database fields.
- suggestedAssigneeId is optional and must be one of the provided team member userId values.
- If no suitable member exists, set suggestedAssigneeId and suggestedAssigneeName to null.
- A member with empty jobLabels is not suitable for any specialized task.

```
