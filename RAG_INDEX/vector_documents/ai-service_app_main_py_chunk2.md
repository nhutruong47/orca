# Knowledge Document: main.py (Chunk 3/3)

## Metadata
```json
{
  "file_path": "ai-service/app/main.py",
  "language": "py",
  "module": "app",
  "business_domain": "admin",
  "tags": [
    "admin",
    "authentication",
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, authentication, production

## Source Code Chunk
```py
()
        return rag_service.get_stats()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/api/rag/index/{source_type}")
def rag_index(source_type: str) -> dict:
    """
    Trigger reindexing for a source type.
    Admin only - would need authentication in production.
    """
    # This would trigger async indexing job
    return {
        "status": "indexing_started",
        "source": source_type,
        "message": f"Reindexing for source '{source_type}' has been queued."
    }


@app.get("/api/rag/sources")
def rag_sources() -> dict:
    """
    List all indexed knowledge sources.
    """
    try:
        rag_service = get_rag_service()
        stats = rag_service.get_stats()
        return {
            "sources": list(stats.get("sources", {}).keys()),
            "documents_by_source": stats.get("sources", {}),
            "total_documents": stats.get("documents_indexed", 0)
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

```
