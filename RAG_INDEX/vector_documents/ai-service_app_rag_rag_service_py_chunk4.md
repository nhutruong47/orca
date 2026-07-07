# Knowledge Document: rag_service.py (Chunk 5/6)

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
  "chunk_index": 4,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: production, admin, inventory, security

## Source Code Chunk
```py
 "relevance_score": doc.relevance_score,
                "url": self._generate_url(doc.document)
            })
        
        return citations
    
    def _truncate_content(self, content: str, max_length: int) -> str:
        """Truncate content to max length"""
        if len(content) <= max_length:
            return content
        return content[:max_length].rsplit(" ", 1)[0] + "..."
    
    def _generate_url(self, doc: KnowledgeDocument) -> str:
        """Generate URL to view source document"""
        source_url_map = {
            "inventory": f"/inventory/item/{doc.source_id}",
            "orders": f"/orders/{doc.source_id}",
            "products": f"/products/{doc.source_id}",
            "policies": f"/settings/policies",
            "faq": f"/faq",
            "manual": f"/manual"
        }
        return source_url_map.get(doc.source, "/")
    
    def _parse_response(
        self, 
        response_text: str
    ) -> tuple[str, str, List[Dict[str, Any]]]:
        """Parse LLM response into structured components"""
        try:
            data = json.loads(response_text)
            return (
                data.get("answer", "Không có câu trả lời."),
                data.get("reasoning", "Dựa trên thông tin có sẵn."),
                data.get("suggestions", [])
            )
        except json.JSONDecodeError:
            return (
                response_text,
                "Dựa trên thông tin được truy xuất.",
                []
            )
    
    def _get_conversation_history(
        self, 
        conversation_id: str
    ) -> Optional[List[Dict[str, str]]]:
        """Get conversation history from storage"""
        # Would implement conversation memory here
        return None
    
    def _add_to_history(
        self,
        conversation_id: str,
        user_id: str,
        query: str,
        response: str
    ):
        """Add message to conversation history"""
        # Would implement conversation memory here
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

```
