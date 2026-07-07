# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 4/17)

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
  "chunk_index": 3,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
lf.dimension
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
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.vectors_file = self.storage_path / "vectors.json"
        self.metadata_file = self.storage_path / "metadata.json"
        self._load()
    
    def _load(self):
        if self.vectors_file.exists():
            with open(self.vectors_file) as f:
                data = json.load(f)
                self.vectors = {k: np.array(v) for k, v in data["vectors"].items()}
        else:
            self.vectors = {}
        
        if self.metadata_file.exists():
            with open(self.metadata_file) as f:
                self.metadata = json.load(f)
        else:
            self.metadata = {}
    
    def _save(self):
        with open(self.vectors_file, "w") as f:
            json.dump({
                "vectors": {k: v.tolist() for k, v in self.vectors.items()}
            }, f)
        with open(self.metadata_file, "w") as f:
            json.dump(self.metadata, f)
    
    def add(self, doc_id: str, embedding: List[float], metadata: dict):
        """Add a document vector"""
        self.vectors[doc_id] = np.array(embedding)
        self.metadata[doc_id] = metadata
        self._save()
    
    def search(self, query_embedding: List[float], k: int = 5) -> List[Tuple[str, float]]:
        """Search for k most similar documents"""
        query_vec = np.array(query_embedding)
        similarities = []
        
        for doc_id, doc_vec in self.vectors.items():
            # Cosine similarity
            sim = np.dot(query_vec, doc_vec) / (np.linalg.norm(query_vec) * np.linalg.norm(doc_vec))
            similarities.append((doc_id, float(sim)))
        
        # Sort by similarity descending
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:k]
    
    def get(self, doc_id: str) -> Optional[dict]:
        """Get document by ID"""
        if doc_id in self.metadata:
            return self.metadata[doc_id]
        return None
    

```
