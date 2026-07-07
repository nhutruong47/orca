# Knowledge Document: vector_store.py (Chunk 2/4)

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
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
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
        metadata: Dict[str, Any]
    ):
        """
        Add a document vector.
        
        Args:
            doc_id: Unique document ID
            embedding: Vector embedding
            metadata: Document metadata
        """
        self._vectors[doc_id] = np.array(embedding)
        self._metadata[doc_id] = {
            **metadata,
            "indexed_at": datetime.utcnow().isoformat()
        }
        self._save()
    
    def search(
        self, 
        query_embedding: List[float], 
        k: int = 5,
        filter_source: Optional[str] = None
    ) -> List[Tuple[str, float]]:
        """
        Search for k most similar documents.
        
        Args:
            query_embedding: Query vector
            k: Number of results to return
            filter_source: Optional source filter
            
        Returns:
            List of (doc_id, similarity_score) tuples
        """
        if not self._vectors:
            return []
        
        query_vec = np.array(query_embedding)
        query_norm = np.linalg.norm(query_vec)
        
        if query_norm == 0:
            return []
        
        similarities = []
        
        for doc_id, doc_vec in self._vectors.items():
            # Apply source filter if specified
            if filter_source:
                doc_metadata = self._metadata.get(doc_id, {})
                if doc_metadata.get("source") != filter_source:
                    continue
            
            # Compute cosine similarity
            doc_norm = np.linalg.norm(doc_vec)
            if doc_norm == 0:
                continue
                
            sim = np.dot(query_vec, doc_vec) / (query_norm * doc_norm)
            similarities.append((doc_id, float(sim)))
        
        # Sort by similarity descending
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:k]
    
    def get(self, doc_id: str) -> Optional[Dict[str, Any]]:

```
