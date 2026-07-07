# Knowledge Document: rag_service.py (Chunk 3/6)

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
  "chunk_index": 2,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: production, admin, inventory, security

## Source Code Chunk
```py
admin.*mode",
            r"developer.*mode",
            r"```system",
            r"```instructions",
        ]
        
        for pattern in dangerous_patterns:
            text = re.sub(pattern, "[FILTERED]", text, flags=re.IGNORECASE)
        
        return text.strip()
    
    def _retrieve(
        self,
        query_embedding: List[float],
        sources: Optional[List[str]] = None,
        max_docs: int = 5
    ) -> List[RetrievedDocument]:
        """Retrieve documents from vector store"""
        results = self.vector_store.search(
            query_embedding=query_embedding,
            k=max_docs * 2  # Get more for filtering
        )
        
        retrieved = []
        rank = 0
        
        for doc_id, score in results:
            metadata = self.vector_store.get(doc_id)
            if not metadata:
                continue
            
            # Filter by source if specified
            if sources and metadata.get("source") not in sources:
                continue
            
            doc = KnowledgeDocument(
                id=doc_id,
                source=metadata.get("source", "unknown"),
                source_id=metadata.get("source_id", ""),
                content=metadata.get("content", ""),
                metadata=metadata.get("metadata", {}),
                chunk_index=metadata.get("chunk_index", 0)
            )
            
            retrieved.append(RetrievedDocument(
                document=doc,
                relevance_score=score,
                rank=rank
            ))
            rank += 1
            
            if len(retrieved) >= max_docs:
                break
        
        return retrieved
    
    def _generate_response(self, prompt: str) -> str:
        """
        Generate response using LLM.
        This is a placeholder - actual implementation would call Gemini API.
        """
        # In production, this would call Gemini API
        # For now, return a structured placeholder
        return json.dumps({
            "answer": "Tôi đã tìm thấy thông tin liên quan trong cơ sở tri thức ORCA.",
            "reasoning": "Dựa trên các tài liệu được truy xuất, tôi có thể cung cấp thông tin này.",
            "suggestions": [
                {"label": "Xem chi tiết", "type": "navigate", "payload": {}}
            ]
        })
    
    def _calculate_confidence(
        self, 

```
