# Knowledge Document: PROMPT_STANDARDIZATION.md (Chunk 6/7)

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
  "chunk_index": 5,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, analytics, production, security, admin, inventory, employee

## Source Code Chunk
```md
ext, flags=re.IGNORECASE)
    
    return text.strip()
```

### 7.2 Output Validation

```python
def validate_llm_output(output: str, expected_schema: dict) -> bool:
    """Validate LLM output against expected schema"""
    try:
        parsed = json.loads(output)
        
        # Check required fields
        for field in expected_schema.get("required", []):
            if field not in parsed:
                return False
        
        # Check field types
        for field, field_type in expected_schema.get("types", {}).items():
            if field in parsed:
                if not isinstance(parsed[field], field_type):
                    return False
        
        return True
    except json.JSONDecodeError:
        return False
```

---

## 8. Token Management

### 8.1 Token Budget

```python
TOKEN_BUDGET = {
    "system_prompt": 500,      # Base system instructions
    "developer_prompt": 300,     # Technical rules
    "context": 2000,             # Retrieved knowledge
    "history": 1000,             # Conversation history
    "user_query": 500,          # User input
    "output": 1000,             # Expected response
    "safety_buffer": 200,        # Safety margin
}
```

### 8.2 Context Truncation

```python
def truncate_context(documents: List[dict], max_tokens: int) -> List[dict]:
    """Truncate documents to fit within token budget"""
    truncated = []
    current_tokens = 0
    
    for doc in sorted(documents, key=lambda x: x.get("relevance", 0), reverse=True):
        doc_tokens = estimate_tokens(doc["content"])
        
        if current_tokens + doc_tokens <= max_tokens:
            truncated.append(doc)
            current_tokens += doc_tokens
        else:
            break
    
    return truncated
```

---

## 9. Multi-Language Support

### 9.1 Vietnamese Date Parsing Rules

```python
DATE_PARSING_RULES = """
DATE PARSING RULES:
- "hôm nay" / "hom nay" = today
- "ngay mai" / "ngay mai" = tomorrow
- "ngay kia" / "ngay kia" = day after tomorrow
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


```
