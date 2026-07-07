# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 3/17)

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
  "chunk_index": 2,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
d(default_factory=datetime.utcnow)
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
    sources: Optional[List[str]] = None  # Filter by source type
    max_documents: int = Field(default=5, ge=1, le=20)
    conversation_id: Optional[str] = None
    
class StandardizedAIResponse(BaseModel):
    """Standardized AI response format"""
    # Core answer
    answer: str
    reasoning_summary: str
    
    # Knowledge attribution
    referenced_knowledge: List[dict] = Field(default_factory=list)
    
    # Confidence
    confidence: dict = Field(default_factory=dict)
    
    # Actions
    suggested_actions: List[dict] = Field(default_factory=list)
    
    # Metadata
    metadata: dict = Field(default_factory=dict)
```

#### Task 1.2: Create Embedding Service

```python
# ai-service/app/rag/embedding.py

from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List
import os

class EmbeddingService:
    """Text vectorization service"""
    
    def __init__(self):
        model_name = os.getenv("EMBEDDING_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        self.model = SentenceTransformer(model_name)
        self.dimension = self.model.get_sentence_embedding_dimension()
    
    def embed(self, texts: List[str]) -> List[List[float]]:
        """Convert texts to embeddings"""
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings.tolist()
    
    def embed_query(self, query: str) -> List[float]:
        """Embed a single query"""
        return self.embed([query])[0]
    
    @property
    def embedding_dimension(self) -> int:
        return self.dimension
```

#### Task 1.3: Create Vector Store

```python
# ai-service/app/rag/vector_store.py

import numpy as np
from typing import List, Optional, Tuple
import json
import os
from pathlib import Path

class VectorStore:
    """Simple file-based vector store for development"""
    
    def __init__(self, storage_path: str = "./data/vectors"):
        self.storage_path = Path(storage_path)

```
