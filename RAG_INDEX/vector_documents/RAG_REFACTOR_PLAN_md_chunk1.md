# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 2/17)

## Metadata
```json
{
  "file_path": "RAG_REFACTOR_PLAN.md",
  "language": "md",
  "module": "orca",
  "business_domain": "authorization",
  "tags": [
    "authorization",
    "production",
    "factory",
    "inventory",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
    │   │
│  │              └─────────┘ └─────────┘ └─────────────┘               │   │
│  │                                    │                               │   │
│  │                                    ▼                               │   │
│  │                           ┌────────────────┐                       │   │
│  │                           │ Conversation   │                       │   │
│  │                           │ Memory         │                       │   │
│  │                           └────────────────┘                       │   │
│  │                                    │                               │   │
│  │                                    ▼                               │   │
│  │                           ┌────────────────┐                       │   │
│  │                           │ Citation       │                       │   │
│  │                           │ Formatter      │                       │   │
│  │                           └────────────────┘                       │   │
│  │                                                                  │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Implementation Tasks

### Phase 1: Core Infrastructure

#### Task 1.1: Create RAG Data Models

```python
# ai-service/app/rag/models.py

from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime

class KnowledgeDocument(BaseModel):
    """A chunk of indexed knowledge"""
    id: str
    source: Literal["inventory", "orders", "products", "users", "policies", "faq", "manual"]
    source_id: str  # Reference to original entity
    content: str
    metadata: dict = Field(default_factory=dict)
    embedding: Optional[List[float]] = None
    chunk_index: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
class RetrievedDocument(BaseModel):
    """A document retrieved from the knowledge base"""
    document: KnowledgeDocument
    relevance_score: float = Field(ge=0, le=1)
    rank: int

class RAGRequest(BaseModel):
    """Standard RAG request"""
    query: str
    team_id: str
    user_id: str

```
