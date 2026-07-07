# Knowledge Document: vector_store.py (Chunk 3/4)

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
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
         if doc_norm == 0:
                continue
                
            sim = np.dot(query_vec, doc_vec) / (query_norm * doc_norm)
            similarities.append((doc_id, float(sim)))
        
        # Sort by similarity descending
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:k]
    
    def get(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """Get document metadata by ID"""
        return self._metadata.get(doc_id)
    
    def get_vector(self, doc_id: str) -> Optional[List[float]]:
        """Get document vector by ID"""
        vec = self._vectors.get(doc_id)
        return vec.tolist() if vec is not None else None
    
    def delete(self, doc_id: str):
        """Delete a document"""
        if doc_id in self._vectors:
            del self._vectors[doc_id]
        if doc_id in self._metadata:
            del self._metadata[doc_id]
        self._save()
    
    def delete_by_source(self, source: str):
        """Delete all documents from a source"""
        to_delete = [
            doc_id for doc_id, meta in self._metadata.items()
            if meta.get("source") == source
        ]
        
        for doc_id in to_delete:
            self.delete(doc_id)
    
    def count(self) -> int:
        """Get total number of vectors"""
        return len(self._vectors)
    
    def count_by_source(self, source: str) -> int:
        """Get number of vectors for a source"""
        return sum(
            1 for meta in self._metadata.values()
            if meta.get("source") == source
        )
    
    def list_sources(self) -> List[str]:
        """List all unique sources"""
        sources = set()
        for meta in self._metadata.values():
            if source := meta.get("source"):
                sources.add(source)
        return sorted(list(sources))
    
    def get_stats(self) -> Dict[str, Any]:
        """Get vector store statistics"""
        sources = self.list_sources()
        return {
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

```
