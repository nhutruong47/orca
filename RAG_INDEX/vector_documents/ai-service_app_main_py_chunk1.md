# Knowledge Document: main.py (Chunk 2/3)

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
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, authentication, production

## Source Code Chunk
```py
us_code=400, detail="Cannot create a plan for UNKNOWN intent.")

    if settings.ai_v2_mode == "mock":
        try:
            return mock_plan(request)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
    if settings.ai_v2_mode == "gemini":
        try:
            return gemini_plan(request)
        except GeminiPlanInputError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        except GeminiPlanError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc
    raise HTTPException(status_code=400, detail=f"Unsupported AI_V2_MODE: {settings.ai_v2_mode}")


@app.post("/revise", response_model=PlanDraftResponse)
def revise(request: ReviseRequest) -> PlanDraftResponse:
    if settings.ai_v2_mode == "mock":
        return mock_revise(request)
    if settings.ai_v2_mode == "gemini":
        try:
            return gemini_revise(request)
        except GeminiReviseError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc
    raise HTTPException(status_code=400, detail=f"Unsupported AI_V2_MODE: {settings.ai_v2_mode}")


# =============================================================================
# RAG Endpoints (v0.2.0)
# =============================================================================

@app.post("/api/rag/query", response_model=StandardizedAIResponse)
def rag_query(request: RAGRequestModel) -> StandardizedAIResponse:
    """
    Query the RAG system with a natural language question.
    Returns a standardized response with citations.
    """
    try:
        rag_service = get_rag_service()
        return rag_service.query(request)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/api/rag/stats")
def rag_stats() -> dict:
    """
    Get RAG system statistics.
    """
    try:
        rag_service = get_rag_service()
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

```
