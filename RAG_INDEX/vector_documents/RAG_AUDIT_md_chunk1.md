# Knowledge Document: RAG_AUDIT.md (Chunk 2/10)

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
  "chunk_index": 1,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: report, payment, factory, production, admin, inventory, security, chat

## Source Code Chunk
```md
ietnamese workshop/task management app.

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

Your only job is to convert extracted structured fields into a draft Goal and draft Tasks.
...
"""
```

#### Revise Prompt (`_build_revise_prompt`)
```python
# Lines 215-280
"""
You are ORCA AI v2 revise module for a Vietnamese workshop/task management app.

Your only job is to revise an existing draft Goal/Tasks according to the user's revision instruction.
...
"""
```

### 2.2 Issues with Current Prompts

| Issue | Location | Impact |
|-------|----------|--------|
| No RAG context injection | All prompts | Responses may lack domain knowledge |
| No conversation history context | Plan/Revise | Can't maintain coherent multi-turn |
| No source attribution | All | Users can't verify information |
| No confidence scoring | Extract | No uncertainty indication |
| Hardcoded rules | `safe_rules` functions | Logic buried in code |
| No safety/ethics rules | All prompts | Missing content guidelines |

### 2.3 Frontend Prompt Issues (`AiAssistantPanel.tsx`)

```tsx
// Line 85 - Hardcoded response text
content: res.description || 'Tôi đã phân tích yêu cầu của bạn:',

// No structured response format
// No reasoning summary
// No confidence score
// No suggested actions
```

---

## 3. Missing RAG Architecture

### 3.1 Required Services (Not Implemented)

| Service | Purpose | Status |
|---------|---------|--------|
| `RAGService` | Unified RAG orchestration | ❌ MISSING |
| `EmbeddingService` | Text vectorization | ❌ MISSING |
| `Retriever` | Semantic search | ❌ MISSING |
| `Chunker` | Document splitting | ❌ MISSING |
| `PromptBuilder` | Dynamic prompt construction | ❌ MISSING |
| `CitationFormatter` | Source attribution | ❌ MISSING |
| `ConversationMemory` | Multi-turn context | ❌ MISSING |
| `DocumentIndexer` | Knowledge base management | ❌ MISSING |
| `KnowledgeSource` | Data source abstraction | ❌ MISSING |

### 3.2 Knowledge Sources (Not Integrated)

| Source | Entity | Chunk Strategy | Status |
|--------|--------|----------------|--------|

```
