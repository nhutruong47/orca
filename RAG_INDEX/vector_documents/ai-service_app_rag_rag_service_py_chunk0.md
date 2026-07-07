# Knowledge Document: rag_service.py (Chunk 1/6)

## Metadata
```json
{
  "file_path": "ai-service/app/rag/rag_service.py",
  "language": "py",
  "module": "rag",
  "business_domain": "production",
  "tags": [
    "production",
    "admin",
    "inventory",
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: production, admin, inventory, security

## Source Code Chunk
```py
"""
Main RAG Service - Orchestrates the RAG pipeline
"""

import json
import time
from typing import List, Optional, Dict, Any
from datetime import datetime

from app.rag.models import (
    RAGRequest,
    StandardizedAIResponse,
    RetrievedDocument,
    KnowledgeDocument,
    SourceAttribution
)
from app.rag.embedding import EmbeddingService, get_embedding_service
from app.rag.vector_store import VectorStore, get_vector_store
from app.rag.prompt_builder import PromptBuilder


class RAGService:
    """
    Main RAG orchestration service.
    Coordinates embedding, retrieval, prompt building, and response formatting.
    """
    
    def __init__(
        self,
        embedding_service: Optional[EmbeddingService] = None,
        vector_store: Optional[VectorStore] = None
    ):
        self.embedding_service = embedding_service or get_embedding_service()
        self.vector_store = vector_store or get_vector_store()
        self.prompt_builder = PromptBuilder()
    
    def query(self, request: RAGRequest) -> StandardizedAIResponse:
        """
        Process a RAG query.
        
        Args:
            request: RAG request with query and parameters
            
        Returns:
            Standardized AI response with citations
        """
        start_time = time.time()
        
        # Sanitize query
        query = self._sanitize_input(request.query)
        
        # Get conversation history
        history = None
        if request.conversation_id:
            history = self._get_conversation_history(request.conversation_id)
        
        # Embed query
        query_embedding = self.embedding_service.embed_query(query)
        
        # Retrieve relevant documents
        retrieved_docs = self._retrieve(
            query_embedding=query_embedding,
            sources=request.sources,
            max_docs=request.max_documents
        )
        
        # Build context
        context = {
            "team_id": request.team_id,
            "user_id": request.user_id
        }
        
        # Build prompt
        prompt = self.prompt_builder.build(
            query=query,
            retrieved_docs=retrieved_docs,
            conversation_history=history,
            context=context
        )
        
        # Generate response (placeholder - would call LLM)
        response_text = self._generate_response(prompt)
        

```
