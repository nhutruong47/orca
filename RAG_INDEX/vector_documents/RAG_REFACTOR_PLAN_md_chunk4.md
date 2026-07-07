# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 5/17)

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
  "chunk_index": 4,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
norm(doc_vec))
            similarities.append((doc_id, float(sim)))
        
        # Sort by similarity descending
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:k]
    
    def get(self, doc_id: str) -> Optional[dict]:
        """Get document by ID"""
        if doc_id in self.metadata:
            return self.metadata[doc_id]
        return None
    
    def delete(self, doc_id: str):
        """Delete a document"""
        if doc_id in self.vectors:
            del self.vectors[doc_id]
        if doc_id in self.metadata:
            del self.metadata[doc_id]
        self._save()
    
    def count(self) -> int:
        return len(self.vectors)
```

#### Task 1.4: Create Retriever

```python
# ai-service/app/rag/retriever.py

from typing import List, Optional
from app.rag.models import RetrievedDocument, KnowledgeDocument
from app.rag.vector_store import VectorStore
import json

class Retriever:
    """Semantic search retriever"""
    
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store
    
    def retrieve(
        self,
        query_embedding: List[float],
        sources: Optional[List[str]] = None,
        k: int = 5
    ) -> List[RetrievedDocument]:
        """Retrieve most relevant documents"""
        
        # Search vector store
        results = self.vector_store.search(query_embedding, k=k * 2 if sources else k)
        
        retrieved = []
        rank = 0
        
        for doc_id, score in results:
            metadata = self.vector_store.get(doc_id)
            if not metadata:
                continue
            
            # Filter by source if specified
            if sources and metadata.get("source") not in sources:
                continue
            
            retrieved.append(RetrievedDocument(
                document=KnowledgeDocument(
                    id=doc_id,
                    source=metadata.get("source", "unknown"),
                    source_id=metadata.get("source_id", ""),
                    content=metadata.get("content", ""),
                    metadata=metadata.get("metadata", {}),
                    chunk_index=metadata.get("chunk_index", 0)
                ),
                relevance_score=score,
                rank=rank
            ))
            rank += 1
            
            if len(retrieved) >= k:

```
