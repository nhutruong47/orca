# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 10/17)

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
  "chunk_index": 9,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
 citations
    
    def _truncate_content(self, content: str, max_length: int) -> str:
        if len(content) <= max_length:
            return content
        return content[:max_length].rsplit(" ", 1)[0] + "..."
    
    def _generate_url(self, doc) -> str:
        """Generate URL to view source document"""
        source_url_map = {
            "inventory": f"/inventory/item/{doc.source_id}",
            "orders": f"/orders/{doc.source_id}",
            "products": f"/products/{doc.source_id}",
            "policies": f"/settings/policies#{doc.source_id}",
            "faq": f"/faq#{doc.source_id}"
        }
        return source_url_map.get(doc.source, "/")
```

#### Task 1.8: Create Main RAG Service

```python
# ai-service/app/rag/rag_service.py

from typing import List, Optional
import time
from app.rag.models import RAGRequest, StandardizedAIResponse
from app.rag.embedding import EmbeddingService
from app.rag.vector_store import VectorStore
from app.rag.retriever import Retriever
from app.rag.prompt_builder import PromptBuilder
from app.rag.memory import ConversationMemory
from app.rag.citation import CitationFormatter

class RAGService:
    """Main RAG orchestration service"""
    
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()
        self.retriever = Retriever(self.vector_store)
        self.prompt_builder = PromptBuilder()
        self.memory = ConversationMemory()
        self.citation_formatter = CitationFormatter()
    
    def query(self, request: RAGRequest) -> StandardizedAIResponse:
        """Process a RAG query"""
        start_time = time.time()
        
        # Get conversation history
        history = None
        if request.conversation_id:
            history = self.memory.get_history(request.conversation_id)
        
        # Embed query
        query_embedding = self.embedding_service.embed_query(request.query)
        
        # Retrieve relevant documents
        retrieved_docs = self.retriever.retrieve(
            query_embedding=query_embedding,
            sources=request.sources,
            k=request.max_documents
        )
        
        # Build context for LLM
        context = {
            "team_name": request.team_id,  # Would fetch actual team name
            "user_role": "member"
        }
        
        # Build prompt

```
