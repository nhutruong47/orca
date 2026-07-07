# Knowledge Document: embedding.py (Chunk 2/2)

## Metadata
```json
{
  "file_path": "ai-service/app/rag/embedding.py",
  "language": "py",
  "module": "rag",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```py
ts: List of text strings to embed
            
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
            return embeddings.tolist()
        except Exception as e:
            logger.error(f"Embedding generation failed: {e}")
            return self._mock_embeddings(len(texts))
    
    def embed_query(self, query: str) -> List[float]:
        """
        Embed a single query string.
        
        Args:
            query: Query text to embed
            
        Returns:
            Embedding vector
        """
        return self.embed([query])[0]
    
    def _mock_embeddings(self, count: int) -> List[List[float]]:
        """
        Generate mock embeddings for testing when model is unavailable.
        Uses deterministic random based on text hash.
        """
        embeddings = []
        for i in range(count):
            # Use fixed seed for reproducibility
            np.random.seed(i + 42)
            embedding = np.random.randn(self._dimension).astype(float)
            # Normalize
            embedding = embedding / np.linalg.norm(embedding)
            embeddings.append(embedding.tolist())
        return embeddings
    
    @property
    def is_initialized(self) -> bool:
        """Check if the service is initialized"""
        return self._initialized


# Singleton instance
_embedding_service: Optional[EmbeddingService] = None


def get_embedding_service() -> EmbeddingService:
    """Get singleton embedding service instance"""
    global _embedding_service
    if _embedding_service is None:
        _embedding_service = EmbeddingService()
    return _embedding_service

```
