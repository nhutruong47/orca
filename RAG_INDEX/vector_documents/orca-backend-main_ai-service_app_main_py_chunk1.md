# Knowledge Document: main.py (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/ai-service/app/main.py",
  "language": "py",
  "module": "app",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```py
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

@app.get("/models")
def list_models():
    import httpx
    url = "https://generativelanguage.googleapis.com/v1beta/models"
    try:
        resp = httpx.get(url, params={"key": settings.gemini_api_key}, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

```
