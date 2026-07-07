# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 9/17)

## Metadata
```json
{
  "file_path": "RAG_REFACTOR_PLAN.md",
  "language": "md",
  "module": "orca",
  "business_domain": "authorization",
  "tags": [
    "authorization",
    "production",
    "factory",
    "inventory",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 8,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
_message(self, conversation_id: str, role: str, content: str):
        """Add a message to conversation"""
        filepath = os.path.join(self.storage_path, f"{conversation_id}.json")
        
        if os.path.exists(filepath):
            with open(filepath) as f:
                data = json.load(f)
        else:
            data = {"messages": [], "created_at": datetime.utcnow().isoformat()}
        
        data["messages"].append({
            "role": role,
            "content": content,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Keep last 20 messages
        data["messages"] = data["messages"][-20:]
        
        with open(filepath, "w") as f:
            json.dump(data, f)
    
    def clear_history(self, conversation_id: str):
        """Clear conversation history"""
        filepath = os.path.join(self.storage_path, f"{conversation_id}.json")
        if os.path.exists(filepath):
            os.remove(filepath)
```

#### Task 1.7: Create Citation Formatter

```python
# ai-service/app/rag/citation.py

from typing import List
from app.rag.models import RetrievedDocument

class CitationFormatter:
    """Format citations for responses"""
    
    def format_citations(self, documents: List[RetrievedDocument]) -> List[dict]:
        """Format documents as citations"""
        citations = []
        
        for doc in documents:
            citations.append({
                "document_id": doc.document.id,
                "source": doc.document.source,
                "source_id": doc.document.source_id,
                "title": doc.document.metadata.get("title", "Unknown"),
                "category": doc.document.metadata.get("category", "General"),
                "excerpt": self._truncate_content(doc.document.content, 200),
                "relevance_score": doc.relevance_score,
                "url": self._generate_url(doc.document)
            })
        
        return citations
    
    def _truncate_content(self, content: str, max_length: int) -> str:
        if len(content) <= max_length:
            return content
        return content[:max_length].rsplit(" ", 1)[0] + "..."
    
    def _generate_url(self, doc) -> str:
        """Generate URL to view source document"""
        source_url_map = {
            "inventory": f"/inventory/item/{doc.source_id}",

```
