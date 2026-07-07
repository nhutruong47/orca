# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 12/17)

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
  "chunk_index": 11,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
ould call Gemini API here
        return "This is a placeholder response."
    
    def _calculate_confidence(self, docs: List, response: str) -> dict:
        """Calculate response confidence"""
        if not docs:
            return {
                "score": 0.0,
                "level": "low",
                "reasons": ["No relevant documents found in knowledge base"]
            }
        
        avg_relevance = sum(d.relevance_score for d in docs) / len(docs)
        
        if avg_relevance > 0.8:
            level = "high"
            reasons = ["High relevance scores from knowledge base"]
        elif avg_relevance > 0.5:
            level = "medium"
            reasons = ["Moderate relevance from knowledge base"]
        else:
            level = "low"
            reasons = ["Low relevance scores, response may be uncertain"]
        
        return {
            "score": round(avg_relevance, 2),
            "level": level,
            "reasons": reasons
        }
    
    def _extract_reasoning(self, response: str) -> str:
        """Extract reasoning from response"""
        # Would parse structured response
        return "Based on the retrieved knowledge and analysis."
    
    def _extract_suggestions(self, response: str) -> List[dict]:
        """Extract suggested actions from response"""
        # Would parse structured response
        return []
    
    def index_document(self, doc_id: str, content: str, metadata: dict, source: str, source_id: str):
        """Index a document for retrieval"""
        embedding = self.embedding_service.embed([content])[0]
        self.vector_store.add(doc_id, embedding, {
            "content": content,
            "metadata": metadata,
            "source": source,
            "source_id": source_id
        })
```

### Phase 2: Knowledge Indexers

```python
# ai-service/app/knowledge/base.py

from abc import ABC, abstractmethod
from typing import List

class BaseIndexer(ABC):
    """Base class for knowledge indexers"""
    
    @property
    @abstractmethod
    def source_type(self) -> str:
        """Return the source type identifier"""
        pass
    
    @abstractmethod
    async def fetch_documents(self) -> List[dict]:
        """Fetch documents from source"""
        pass
    
    @abstractmethod
    def chunk_content(self, content: str) -> List[str]:
        """Split content into chunks"""

```
