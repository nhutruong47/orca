# Knowledge Document: RAG_AUDIT.md (Chunk 1/10)

## Metadata
```json
{
  "file_path": "RAG_AUDIT.md",
  "language": "md",
  "module": "orca",
  "business_domain": "report",
  "tags": [
    "report",
    "payment",
    "factory",
    "production",
    "admin",
    "inventory",
    "security",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, production, admin, inventory, security, chat

## Source Code Chunk
```md
# ORCA Platform - AI/RAG Architecture Audit Report

**Date:** July 7, 2026
**Auditor:** Lead Software Architect
**Status:** IN PROGRESS

---

## Executive Summary

The ORCA platform has AI capabilities concentrated in `ai-service` (Python FastAPI) and frontend components. Current architecture suffers from:

1. **No unified RAG pipeline** - AI responses don't retrieve from knowledge base
2. **Duplicated prompt templates** across components
3. **Inconsistent response formats** between AI features
4. **No citation/source tracking** in AI responses
5. **No vector embeddings** for semantic search
6. **Limited conversation memory** handling
7. **No unified PromptBuilder pattern**

---

## 1. Current AI Architecture

### 1.1 AI Service Structure (`ai-service/`)

```
ai-service/
├── app/
│   ├── main.py          # FastAPI endpoints
│   ├── config.py        # Settings
│   ├── models.py        # Pydantic models
│   ├── gemini_ai.py     # Gemini integration (1130 lines)
│   └── mock_ai.py       # Mock mode
├── requirements.txt
└── .env
```

### 1.2 Frontend AI Components

| Component | Purpose | Location |
|-----------|---------|----------|
| `AiAssistantPanel.tsx` | Chat interface | `src/components/` |
| `groupService.ts` | AI API client | `src/services/` |
| Backend `AiController.java` | API gateway | `backend/` |

### 1.3 AI Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/ai/parse` | POST | Legacy text parsing |
| `/api/ai/v2/extract` | POST | V2 intent extraction |
| `/api/ai/v2/plan` | POST | Generate task plan |
| `/api/ai/v2/revise` | POST | Revise existing plan |
| `ai-service /extract` | POST | Internal AI extraction |
| `ai-service /plan` | POST | Internal AI planning |
| `ai-service /revise` | POST | Internal AI revision |

---

## 2. Current Prompt Architecture

### 2.1 Prompt Templates in `gemini_ai.py`

#### Extract Prompt (`_build_extract_prompt`)
```python
# Lines 71-148
"""
You are ORCA AI v2 extract module for a Vietnamese workshop/task management app.

Your only job is to classify the user request and extract structured fields.
Do not create tasks. Do not save data. Do not explain.

Supported intents:
- PRODUCTION_PLAN
- OPERATION_TASK
- UNKNOWN
...
"""
```

#### Plan Prompt (`_build_plan_prompt`)
```python
# Lines 151-212
"""
You are ORCA AI v2 plan module for a Vietnamese workshop/task management app.


```
