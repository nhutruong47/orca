# Knowledge Document: gemini_ai.py (Chunk 3/21)

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
  "chunk_index": 2,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
e, productName, quantity, unit, deadline, priority.
- OPERATION_TASK fields may include: title, area, deadline, priority.
- UNKNOWN should not invent production fields.
- If missingFields is not empty, clarifyingQuestion must ask for those missing details in Vietnamese.
- If missingFields is empty, clarifyingQuestion must be null.

Examples:
User: "Rang 120kg Arabica trước 17:00 hôm nay"
JSON:
{{
  "intent": "PRODUCTION_PLAN",
  "confidence": 0.9,
  "fields": {{
    "title": "Rang 120kg Arabica",
    "productName": "Arabica",
    "quantity": 120,
    "unit": "kg",
    "deadline": "{now.strftime("%Y-%m-%d")}T17:00:00",
    "priority": "HIGH"
  }},
  "missingFields": [],
  "clarifyingQuestion": null
}}

User: "Làm cái kia cho khách"
JSON:
{{
  "intent": "UNKNOWN",
  "confidence": 0.35,
  "fields": {{}},
  "missingFields": ["taskDescription"],
  "clarifyingQuestion": "Anh/chị muốn tạo công việc gì và hạn hoàn thành khi nào?"
}}

Now extract this user request:
{request.text}
""".strip()


def _build_plan_prompt(request: PlanRequest) -> str:
    fields_json = json.dumps(request.fields, ensure_ascii=False, indent=2)
    members_json = json.dumps([member.model_dump() for member in request.members], ensure_ascii=False, indent=2)
    task_count_rule = "3 to 6 tasks" if request.intent == "PRODUCTION_PLAN" else "2 to 4 tasks"

    return f"""
You are ORCA AI v2 plan module for a Vietnamese workshop/task management app.

Your only job is to convert extracted structured fields into a draft Goal and draft Tasks.
Do not classify intent. Do not ask questions. Do not save data. Do not explain.

Input intent:
{request.intent}

Extracted fields:
{fields_json}

Team members available for suggested assignment:
{members_json}

Output only one JSON object matching this exact schema:
{{
  "goalTitle": "string",
  "outputTarget": "string",
  "deadline": "ISO datetime string from extracted fields or null",
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
- Return {task_count_rule}.

```
