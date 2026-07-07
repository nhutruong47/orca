# Knowledge Document: vector_store.py (Chunk 4/4)

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
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
urn {
            "total_vectors": self.count(),
            "sources": {
                source: self.count_by_source(source) 
                for source in sources
            },
            "dimension": len(list(self._vectors.values())[0]) if self._vectors else 0,
            "storage_path": str(self.storage_path)
        }
    
    def clear(self):
        """Clear all vectors and metadata"""
        self._vectors = {}
        self._metadata = {}
        self._save()


# Singleton instance
_vector_store: Optional[VectorStore] = None


def get_vector_store() -> VectorStore:
    """Get singleton vector store instance"""
    global _vector_store
    if _vector_store is None:
        storage_path = os.getenv("VECTOR_STORE_PATH", "./data/vectors")
        _vector_store = VectorStore(storage_path)
    return _vector_store

```
