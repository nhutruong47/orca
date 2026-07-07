# Knowledge Document: rag_service.py (Chunk 6/6)

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
  "chunk_index": 5,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: production, admin, inventory, security

## Source Code Chunk
```py
sation memory here
        pass
    
    def index_document(
        self,
        doc_id: str,
        content: str,
        metadata: Dict[str, Any],
        source: str,
        source_id: str
    ):
        """
        Index a document for retrieval.
        
        Args:
            doc_id: Unique document ID
            content: Text content to index
            metadata: Document metadata
            source: Source type
            source_id: Original entity ID
        """
        # Generate embedding
        embedding = self.embedding_service.embed([content])[0]
        
        # Store in vector database
        self.vector_store.add(doc_id, embedding, {
            "content": content,
            "metadata": metadata,
            "source": source,
            "source_id": source_id
        })
    
    def remove_document(self, doc_id: str):
        """Remove a document from the index"""
        self.vector_store.delete(doc_id)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get RAG service statistics"""
        vector_stats = self.vector_store.get_stats()
        return {
            "documents_indexed": vector_stats["total_vectors"],
            "sources": vector_stats["sources"],
            "embedding_dimension": self.embedding_service.dimension,
            "embedding_model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        }


# Singleton instance
_rag_service: Optional[RAGService] = None


def get_rag_service() -> RAGService:
    """Get singleton RAG service instance"""
    global _rag_service
    if _rag_service is None:
        _rag_service = RAGService()
    return _rag_service

```
