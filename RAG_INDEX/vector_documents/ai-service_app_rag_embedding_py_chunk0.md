# Knowledge Document: embedding.py (Chunk 1/2)

## Metadata
```json
{
  "file_path": "ai-service/app/rag/embedding.py",
  "language": "py",
  "module": "rag",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```py
"""
Embedding Service - Text vectorization using sentence transformers
"""

import os
import numpy as np
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


class EmbeddingService:
    """
    Text vectorization service using sentence transformers.
    Supports multilingual embeddings for Vietnamese content.
    """
    
    def __init__(self):
        self._model = None
        self._dimension = None
        self._initialized = False
        
    @property
    def model(self):
        """Lazy load model on first use"""
        if self._model is None:
            self._load_model()
        return self._model
    
    @property
    def dimension(self) -> int:
        """Get embedding dimension"""
        if self._dimension is None:
            self._load_model()
        return self._dimension
    
    def _load_model(self):
        """Load the sentence transformer model"""
        try:
            from sentence_transformers import SentenceTransformer
            
            # Use multilingual model for Vietnamese support
            model_name = os.getenv(
                "EMBEDDING_MODEL", 
                "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
            )
            
            logger.info(f"Loading embedding model: {model_name}")
            self._model = SentenceTransformer(model_name)
            self._dimension = self._model.get_sentence_embedding_dimension()
            self._initialized = True
            
            logger.info(f"Embedding model loaded. Dimension: {self._dimension}")
            
        except ImportError:
            logger.warning("sentence-transformers not installed. Using mock embeddings.")
            self._model = None
            self._dimension = 384
            self._initialized = True
    
    def embed(self, texts: List[str]) -> List[List[float]]:
        """
        Convert a list of texts to embeddings.
        
        Args:
            texts: List of text strings to embed
            
        Returns:
            List of embedding vectors
        """
        if not texts:
            return []
        
        # Use mock embeddings if model not available
        if self._model is None:
            return self._mock_embeddings(len(texts))
        
        try:
            embeddings = self.model.encode(texts, convert_to_numpy=True)

```
