# Knowledge Document: PROMPT_STANDARDIZATION.md (Chunk 4/7)

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
  "chunk_index": 3,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, analytics, production, security, admin, inventory, employee

## Source Code Chunk
```md
HISTORY_MESSAGE_FORMAT = """
{role.upper()}: {content}
[{timestamp}]
"""
```

### 4.3 Team/User Context

```python
CONTEXT_BUILDER_USER = """
CURRENT CONTEXT:
- Team: {team_name}
- User: {user_name}
- User Role: {user_role}
- Current View: {current_page}

This context helps personalize responses and ensure appropriate permissions.
"""
```

---

## 5. Output Formatter

### 5.1 RAG Response Format

```python
OUTPUT_FORMAT_RAG = """
RESPONSE FORMAT:
Every response must include these sections:

**Answer**: [Clear, direct response to the user's question]

**Reasoning**: [Brief explanation of how you arrived at the answer]

**Sources**: 
- [Source 1]: [Document title] - [Relevant excerpt]
- [Source 2]: [Document title] - [Relevant excerpt]

**Confidence**: {level} ({score}/10)
- [Reason 1]
- [Reason 2]

**Suggested Actions** (if applicable):
1. [Action 1] - [Brief description]
2. [Action 2] - [Brief description]
"""

### 5.2 Extraction Response Format

```python
OUTPUT_FORMAT_EXTRACTION = """
{{
  "intent": "PRODUCTION_PLAN" | "OPERATION_TASK" | "UNKNOWN",
  "confidence": 0.0-1.0,
  "fields": {{
    "title": "string",
    "productName": "string" (PRODUCTION_PLAN only),
    "quantity": number (PRODUCTION_PLAN only),
    "unit": "string" (PRODUCTION_PLAN only),
    "deadline": "ISO datetime" (if provided),
    "priority": "LOW" | "MEDIUM" | "HIGH" (if inferred)
  }},
  "missingFields": ["field1", "field2"],
  "clarifyingQuestion": "string" (if missing fields exist)
}}
"""
```

### 5.3 Plan Generation Response Format

```python
OUTPUT_FORMAT_PLAN = """
{{
  "goalTitle": "string",
  "outputTarget": "string",
  "deadline": "ISO datetime" | null,
  "priority": 1-5,
  "tasks": [
    {{
      "title": "string",
      "description": "string",
      "priority": 1-5,
      "workload": number (>0),
      "suggestedAssigneeId": "userId" | null,
      "suggestedAssigneeName": "string" | null,
      "suggestedReason": "string" | null
    }}
  ]
}}
"""
```

---

## 6. Prompt Templates Library

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

```
