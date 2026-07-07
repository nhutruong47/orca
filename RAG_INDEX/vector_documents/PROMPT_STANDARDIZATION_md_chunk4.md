# Knowledge Document: PROMPT_STANDARDIZATION.md (Chunk 5/7)

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
  "chunk_index": 4,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, analytics, production, security, admin, inventory, employee

## Source Code Chunk
```md
 Prompt Templates Library

### 6.1 Question Answering Template

```python
PROMPT_TEMPLATE_QA = """
{SYSTEM_PROMPT}

{SAFETY_RULES}

{CONTEXT_RETRIEVAL}

CONVERSATION HISTORY:
{history}

USER QUESTION:
{user_question}

{OUTPUT_FORMAT_QA}

Remember:
- Only use information from the retrieved documents
- If you cannot find the answer, say: "Tôi không tìm thấy thông tin này trong cơ sở tri thức ORCA."
- Provide sources for all factual claims
- Be helpful and concise
"""
```

### 6.2 Production Plan Generation Template

```python
PROMPT_TEMPLATE_PLAN = """
{SYSTEM_PROMPT_EXTRACTION}

{DEVELOPER_PROMPT}

TASK: Generate a production plan based on the following information:

Extracted Fields:
{extracted_fields}

Team Members:
{team_members}

{VALIDATION_RULES}

{DEADLINE_PARSING_RULES}

{DEADLINE_FORMAT_RULES}

Now generate the plan following the exact output format.
"""
```

### 6.3 Data Analysis Template

```python
PROMPT_TEMPLATE_ANALYSIS = """
You are an ORCA data analyst helping with production analytics.

TASK: Analyze the following data and provide insights:

Data Summary:
{data_summary}

Time Period: {start_date} to {end_date}

Please provide:
1. Key trends and patterns
2. Anomalies or unusual values
3. Recommendations for improvement
4. Predicted outcomes for next period

FORMAT: Provide a structured analysis with clear sections.
"""
```

---

## 7. Prompt Injection Prevention

### 7.1 Input Sanitization

```python
def sanitize_prompt_input(text: str) -> str:
    """Remove potential prompt injection patterns"""
    dangerous_patterns = [
        r"ignore previous instructions",
        r"disregard.*instructions",
        r"you are now.*different",
        r"forget.*instruction",
        r"new instructions:",
        r"override.*security",
        r"admin.*mode",
        r"developer.*mode",
        r"sudo.*mode",
        r"```system",
        r"```instructions",
    ]
    
    for pattern in dangerous_patterns:
        text = re.sub(pattern, "[FILTERED]", text, flags=re.IGNORECASE)
    
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

```
