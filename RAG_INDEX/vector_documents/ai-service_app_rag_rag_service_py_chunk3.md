# Knowledge Document: rag_service.py (Chunk 4/6)

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
  "chunk_index": 3,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: production, admin, inventory, security

## Source Code Chunk
```py

        return json.dumps({
            "answer": "Tôi đã tìm thấy thông tin liên quan trong cơ sở tri thức ORCA.",
            "reasoning": "Dựa trên các tài liệu được truy xuất, tôi có thể cung cấp thông tin này.",
            "suggestions": [
                {"label": "Xem chi tiết", "type": "navigate", "payload": {}}
            ]
        })
    
    def _calculate_confidence(
        self, 
        docs: List[RetrievedDocument]
    ) -> Dict[str, Any]:
        """Calculate response confidence based on retrieved documents"""
        if not docs:
            return {
                "score": 0.0,
                "level": "low",
                "reasons": ["No relevant documents found in knowledge base"]
            }
        
        avg_relevance = sum(d.relevance_score for d in docs) / len(docs)
        
        if avg_relevance > 0.8:
            level = "high"
            reasons = ["High relevance scores from knowledge base"]
        elif avg_relevance > 0.5:
            level = "medium"
            reasons = ["Moderate relevance from knowledge base"]
        else:
            level = "low"
            reasons = ["Low relevance scores, response may be uncertain"]
        
        return {
            "score": round(avg_relevance, 2),
            "level": level,
            "reasons": reasons
        }
    
    def _format_citations(
        self, 
        docs: List[RetrievedDocument]
    ) -> List[Dict[str, Any]]:
        """Format documents as citations"""
        citations = []
        
        for doc in docs:
            meta = doc.document.metadata or {}
            
            citations.append({
                "document_id": doc.document.id,
                "source": doc.document.source,
                "source_id": doc.document.source_id,
                "title": meta.get("title", "Unknown"),
                "category": meta.get("category", "General"),
                "excerpt": self._truncate_content(doc.document.content, 200),
                "relevance_score": doc.relevance_score,
                "url": self._generate_url(doc.document)
            })
        
        return citations
    
    def _truncate_content(self, content: str, max_length: int) -> str:
        """Truncate content to max length"""
        if len(content) <= max_length:
            return content
        return content[:max_length].rsplit(" ", 1)[0] + "..."
    

```
