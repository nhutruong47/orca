# Knowledge Document: RAG_REFACTOR_PLAN.md (Chunk 14/17)

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
  "chunk_index": 13,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization, production, factory, inventory, chat

## Source Code Chunk
```md
ms = response.json()
            
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
Số lượng: {item.get('quantity', 0)} {item.get('unit', 'đơn vị')}
Giá: {item.get('price', 0):,} VND
Mô tả: {item.get('description', 'Không có mô tả')}
Trạng thái: {item.get('status', 'Không xác định')}
""".strip()
    
    def chunk_content(self, content: str) -> List[str]:
        """Chunk by paragraphs"""
        paragraphs = content.split("\n")
        chunks = []
        current_chunk = []
        
        for para in paragraphs:
            current_chunk.append(para)
            if len("\n".join(current_chunk)) > 500:
                if current_chunk:
                    chunks.append("\n".join(current_chunk))
                current_chunk = []
        
        if current_chunk:
            chunks.append("\n".join(current_chunk))
        
        return chunks if chunks else [content]
    
    def extract_metadata(self, document: dict) -> dict:
        return {
            "title": document.get("name", "Unknown Item"),
            "category": document.get("category", "General"),
            "tags": [document.get("category", "inventory")],
            "last_updated": document.get("updatedAt", "")
        }
```

### Phase 3: API Endpoints

```python
# ai-service/app/main.py additions

from fastapi import APIRouter, HTTPException
from app.rag.models import RAGRequest, StandardizedAIResponse
from app.rag.rag_service import RAGService

router = APIRouter(prefix="/api/rag", tags=["RAG"])

rag_service = RAGService()

@router.post("/query", response_model=StandardizedAIResponse)
async def rag_query(request: RAGRequest):
    """Query the RAG system"""
    try:
        return rag_service.query(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/index/{source_type}")
async def trigger_indexing(source_type: str):
    """Trigger reindexing for a source type"""
    # Would trigger async indexing job
    return {"status": "indexing started", "source": source_type}

@router.get("/stats")
async def get_stats():

```
