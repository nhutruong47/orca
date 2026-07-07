# Knowledge Document: gemini_ai.py (Chunk 2/21)

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
  "chunk_index": 1,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
 schema validation: {exc}") from exc
    draft = _normalize_revise_output(draft, request)
    return _validate_revise_output(draft, request)


def _build_extract_prompt(request: ExtractRequest) -> str:
    now = _local_now()
    return f"""
You are ORCA AI v2 extract module for a Vietnamese workshop/task management app.

Your only job is to classify the user request and extract structured fields.
Do not create tasks. Do not save data. Do not explain.

Current local datetime: {now.isoformat(timespec="minutes")}
Timezone: Asia/Ho_Chi_Minh

Supported intents:
- PRODUCTION_PLAN: production/manufacturing requests such as roast, produce, make a quantity of coffee/product.
- OPERATION_TASK: internal operational tasks such as cleaning, arranging, checking an area or equipment.
- UNKNOWN: unclear requests or features outside MVP such as inventory summary, marketplace, delivery workflow, maintenance workflow, progress summary.

Required fields:
- PRODUCTION_PLAN: productName, quantity, unit, deadline.
- OPERATION_TASK: title, deadline if the user gives or implies a time/date; if no deadline is present, include missingFields ["deadline"].

Deadline rules:
- Return deadline as ISO local datetime string without timezone offset, e.g. "2026-06-07T17:00:00".
- Resolve Vietnamese relative dates using Current local datetime.
- "hom nay"/"hôm nay" means today.
- "ngay mai"/"ngày mai"/"mai" means tomorrow.
- "sang"/"sáng" default time 09:00.
- "chieu"/"chiều" default time 14:00.
- If date is present but time is absent, default time 17:00.
- If exact time is present, use that exact time.

Output only one JSON object matching this schema:
{{
  "intent": "PRODUCTION_PLAN" | "OPERATION_TASK" | "UNKNOWN",
  "confidence": number between 0 and 1,
  "fields": object,
  "missingFields": array of strings,
  "clarifyingQuestion": string or null
}}

Field conventions:
- fields.priority must be "LOW", "MEDIUM", or "HIGH" when known.
- PRODUCTION_PLAN fields may include: title, productName, quantity, unit, deadline, priority.
- OPERATION_TASK fields may include: title, area, deadline, priority.
- UNKNOWN should not invent production fields.
- If missingFields is not empty, clarifyingQuestion must ask for those missing details in Vietnamese.
- If missingFields is empty, clarifyingQuestion must be null.

Examples:
User: "Rang 120kg Arabica trước 17:00 hôm nay"
JSON:
{{

```
