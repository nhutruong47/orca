# Knowledge Document: PROMPT_STANDARDIZATION.md (Chunk 7/7)

## Metadata
```json
{
  "file_path": "PROMPT_STANDARDIZATION.md",
  "language": "md",
  "module": "orca",
  "business_domain": "factory",
  "tags": [
    "factory",
    "analytics",
    "production",
    "security",
    "admin",
    "inventory",
    "employee"
  ],
  "logical_type": "Generic",
  "chunk_index": 6,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, analytics, production, security, admin, inventory, employee

## Source Code Chunk
```md
tomorrow
- "sang" / "sáng" = morning (default 09:00)
- "chieu" / "chiều" = afternoon (default 14:00)
- "toi" / "tối" = evening (default 18:00)

TIME DEFAULTS:
- If date present but time absent, default to 17:00
- If exact time present, use that time

OUTPUT FORMAT:
- Always return ISO 8601 local datetime
- Format: "YYYY-MM-DDTHH:MM:SS"
- No timezone offset
- Use Asia/Ho_Chi_Minh timezone
"""
```

---

## 10. Testing Prompts

### 10.1 Prompt Test Cases

```python
PROMPT_TEST_CASES = {
    "extraction": [
        {
            "input": "Rang 120kg Arabica trước 17:00 hôm nay",
            "expected_intent": "PRODUCTION_PLAN",
            "expected_confidence": ">0.8",
        },
        {
            "input": "Dọn dẹp kho hàng ngày mai",
            "expected_intent": "OPERATION_TASK",
            "expected_fields": ["title", "deadline"],
        },
        {
            "input": "Làm cái này đi",
            "expected_intent": "UNKNOWN",
            "expected_missing": ["taskDescription"],
        },
    ],
    "planning": [
        {
            "input": "Tạo kế hoạch rang 100kg Robusta trước cuối tuần",
            "expected_task_count": "3-6",
            "expected_qc_task": True,
        },
    ],
}
```

---

## 11. Version Control

### 11.1 Prompt Version Schema

```python
PROMPT_VERSION = {
    "version": "1.0.0",
    "created": "2026-07-07",
    "author": "AI Team",
    "changes": [
        "Initial prompt framework",
        "Added safety rules",
        "Added output formatting",
    ],
    "test_status": "passing",
}
```

---

## 12. Monitoring & Logging

### 12.1 Prompt Metrics

```python
PROMPT_METRICS = {
    "tokens_used": int,
    "prompt_eval_count": int,
    "completion_tokens": int,
    "total_duration_ms": int,
    "intent_classified": str,
    "confidence_score": float,
    "retrieval_count": int,
    "sources_cited": List[str],
}
```

### 12.2 Logging Format

```python
PROMPT_LOG_ENTRY = {
    "timestamp": "ISO datetime",
    "user_id": str,
    "team_id": str,
    "prompt_type": str,
    "input_tokens": int,
    "output_tokens": int,
    "latency_ms": int,
    "success": bool,
    "error": str | null,
    "metrics": PROMPT_METRICS,
}
```

```
