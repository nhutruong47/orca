# Knowledge Document: gemini_ai.py (Chunk 19/21)

## Metadata
```json
{
  "file_path": "orca-backend-main/ai-service/app/gemini_ai.py",
  "language": "py",
  "module": "app",
  "business_domain": "chat",
  "tags": [
    "chat",
    "inventory",
    "production",
    "authorization"
  ],
  "logical_type": "Generic",
  "chunk_index": 18,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
teContent"
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = httpx.post(
                url,
                params={"key": settings.gemini_api_key},
                json=payload,
                timeout=settings.gemini_timeout_seconds,
            )
            response.raise_for_status()
            break
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in {429, 503} and attempt < max_retries - 1:
                import time
                time.sleep(2)
                continue
            body = exc.response.text[:1000]
            raise error_cls(f"Gemini API returned HTTP {exc.response.status_code}: {body}") from exc
        except httpx.RequestError as exc:
            if attempt < max_retries - 1:
                import time
                time.sleep(2)
                continue
            raise error_cls(f"Cannot reach Gemini API: {exc}") from exc

    raw_text = _read_gemini_text(response.json(), error_cls)
    return _parse_json_object(raw_text, error_cls)


def _generate_json_object_with_vertex_ai(prompt: str, max_output_tokens: int, error_cls: Type[RuntimeError]) -> dict:
    if not settings.vertex_project_id:
        raise error_cls("VERTEX_PROJECT_ID is required when AI_PROVIDER=vertex.")

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}],
            }
        ],
        "generationConfig": {
            "temperature": 0.1,
            "topP": 0.8,
            "maxOutputTokens": max_output_tokens,
            "responseMimeType": "application/json",
        },
    }

    model_name = _vertex_model_name()
    service_endpoint = _vertex_service_endpoint()
    url = f"https://{service_endpoint}/v1/{model_name}:generateContent"
    try:
        response = httpx.post(
            url,
            headers={"Authorization": f"Bearer {_vertex_access_token(error_cls)}"},
            json=payload,
            timeout=settings.gemini_timeout_seconds,
        )
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        body = exc.response.text[:1000]
        raise error_cls(f"Vertex AI API returned HTTP {exc.response.status_code}: {body}") from exc
    except httpx.RequestError as exc:
        raise error_cls(f"Cannot reach Vertex AI API: {exc}") from exc


```
