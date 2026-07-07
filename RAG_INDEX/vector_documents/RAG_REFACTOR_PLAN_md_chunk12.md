# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 13/17)

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
  "chunk_index": 12,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
e indexers"""
    
    @property
    @abstractmethod
    def source_type(self) -> str:
        """Return the source type identifier"""
        pass
    
    @abstractmethod
    async def fetch_documents(self) -> List[dict]:
        """Fetch documents from source"""
        pass
    
    @abstractmethod
    def chunk_content(self, content: str) -> List[str]:
        """Split content into chunks"""
        pass
    
    @abstractmethod
    def extract_metadata(self, document: dict) -> dict:
        """Extract metadata from document"""
        pass
    
    async def reindex(self, rag_service):
        """Reindex all documents"""
        documents = await self.fetch_documents()
        
        for doc in documents:
            doc_id = f"{self.source_type}_{doc['id']}"
            chunks = self.chunk_content(doc.get("content", ""))
            metadata = self.extract_metadata(doc)
            
            for i, chunk in enumerate(chunks):
                chunk_id = f"{doc_id}_chunk_{i}"
                chunk_metadata = {
                    **metadata,
                    "chunk_index": i,
                    "total_chunks": len(chunks)
                }
                rag_service.index_document(
                    chunk_id, chunk, chunk_metadata,
                    self.source_type, doc["id"]
                )
```

```python
# ai-service/app/knowledge/inventory.py

from app.knowledge.base import BaseIndexer
import httpx

class InventoryIndexer(BaseIndexer):
    """Index inventory documents"""
    
    @property
    def source_type(self) -> str:
        return "inventory"
    
    async def fetch_documents(self) -> List[dict]:
        """Fetch inventory items"""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{os.getenv('BACKEND_URL')}/api/inventory",
                headers={"Authorization": f"Bearer {os.getenv('BACKEND_TOKEN')}"}
            )
            items = response.json()
            
            return [
                {
                    "id": item["id"],
                    "content": self._format_content(item),
                    **item
                }
                for item in items
            ]
    
    def _format_content(self, item: dict) -> str:
        return f"""
{item['name']}
Loại: {item.get('category', 'Không xác định')}

```
