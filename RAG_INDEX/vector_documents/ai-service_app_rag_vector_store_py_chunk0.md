# Knowledge Document: vector_store.py (Chunk 1/4)

## Metadata
```json
{
  "file_path": "ai-service/app/rag/vector_store.py",
  "language": "py",
  "module": "rag",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
"""
Vector Store - Simple file-based vector storage for development
"""

import os
import json
import numpy as np
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class VectorStore:
    """
    Simple file-based vector store for development.
    For production, replace with Qdrant, Pinecone, or Weaviate.
    """
    
    def __init__(self, storage_path: str = "./data/vectors"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        self.vectors_file = self.storage_path / "vectors.json"
        self.metadata_file = self.storage_path / "metadata.json"
        
        self._vectors: Dict[str, np.ndarray] = {}
        self._metadata: Dict[str, Dict[str, Any]] = {}
        
        self._load()
    
    def _load(self):
        """Load vectors and metadata from disk"""
        try:
            if self.vectors_file.exists():
                with open(self.vectors_file, 'r') as f:
                    data = json.load(f)
                    self._vectors = {
                        k: np.array(v) for k, v in data.get("vectors", {}).items()
                    }
            
            if self.metadata_file.exists():
                with open(self.metadata_file, 'r') as f:
                    self._metadata = json.load(f)
                    
            logger.info(f"Loaded {len(self._vectors)} vectors from storage")
            
        except Exception as e:
            logger.warning(f"Failed to load vector store: {e}")
            self._vectors = {}
            self._metadata = {}
    
    def _save(self):
        """Save vectors and metadata to disk"""
        try:
            with open(self.vectors_file, 'w') as f:
                json.dump({
                    "vectors": {
                        k: v.tolist() for k, v in self._vectors.items()
                    },
                    "updated_at": datetime.utcnow().isoformat()
                }, f)
            
            with open(self.metadata_file, 'w') as f:
                json.dump(self._metadata, f, default=str)
                
        except Exception as e:
            logger.error(f"Failed to save vector store: {e}")
    
    def add(
        self, 
        doc_id: str, 
        embedding: List[float], 

```
