# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 15/17)

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
  "chunk_index": 14,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
turn rag_service.query(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/index/{source_type}")
async def trigger_indexing(source_type: str):
    """Trigger reindexing for a source type"""
    # Would trigger async indexing job
    return {"status": "indexing started", "source": source_type}

@router.get("/stats")
async def get_stats():
    """Get RAG system statistics"""
    return {
        "documents_indexed": rag_service.vector_store.count(),
        "sources": ["inventory", "orders", "products", "policies", "faq"]
    }
```

---

## 3. Frontend Integration

### 3.1 Updated AI Service

```typescript
// src/services/ragService.ts

import api from './api';

export interface RAGRequest {
    query: string;
    teamId: string;
    userId: string;
    sources?: string[];
    maxDocuments?: number;
    conversationId?: string;
}

export interface ReferencedKnowledge {
    documentId: string;
    source: string;
    sourceId: string;
    title: string;
    category: string;
    excerpt: string;
    relevanceScore: number;
    url: string;
}

export interface Confidence {
    score: number;
    level: 'high' | 'medium' | 'low';
    reasons: string[];
}

export interface SuggestedAction {
    label: string;
    type: 'create' | 'update' | 'navigate' | 'confirm';
    payload?: any;
}

export interface StandardizedAIResponse {
    answer: string;
    reasoningSummary: string;
    referencedKnowledge: ReferencedKnowledge[];
    confidence: Confidence;
    suggestedActions: SuggestedAction[];
    metadata: {
        model: string;
        tokensUsed: number;
        processingTimeMs: number;
        documentsRetrieved: number;
    };
}

export const ragService = {
    query: async (request: RAGRequest): Promise<StandardizedAIResponse> => {
        return api.post<StandardizedAIResponse>('/api/rag/query', request).then(r => r.data);
    },
    
    getStats: async () => {
        return api.get('/api/rag/stats').then(r => r.data);
    },
    
    triggerIndexing: async (sourceType: string) => {
        return api.post(`/api/rag/index/${sourceType}`).then(r => r.data);
    }
};
```

### 3.2 Updated Chat Panel

```typescript
// src/components/AIChatPanel.tsx

import { ragService, type StandardizedAIResponse, type RAGRequest } from '../services/ragService';

```
