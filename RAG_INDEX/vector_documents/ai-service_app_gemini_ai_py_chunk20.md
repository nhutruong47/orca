# Knowledge Document: gemini_ai.py (Chunk 21/24)

## Metadata
```json
{
  "file_path": "ai-service/app/gemini_ai.py",
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
  "chunk_index": 20,
  "total_chunks": 24
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
ax_output_tokens: int, error_cls: Type[RuntimeError]) -> dict:
    provider = settings.ai_provider.replace("-", "_")
    if provider in {"gemini", "gemini_api", "google_ai"}:
        return _generate_json_object_with_gemini_api(prompt, max_output_tokens, error_cls)
    if provider in {"vertex", "vertex_ai"}:
        return _generate_json_object_with_vertex_ai(prompt, max_output_tokens, error_cls)
    raise error_cls(f"Unsupported AI_PROVIDER: {settings.ai_provider}")


def _generate_json_object_with_gemini_api(prompt: str, max_output_tokens: int, error_cls: Type[RuntimeError]) -> dict:
    if not settings.gemini_api_key:
        raise error_cls("GEMINI_API_KEY is required when AI_PROVIDER=gemini_api.")

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

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{settings.gemini_model}:generateContent"
    max_retries = 5
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
                time.sleep(2 ** attempt)  # Exponential backoff: 1s, 2s, 4s, 8s...
                continue
            body = exc.response.text[:1000]
            raise error_cls(f"Gemini API returned HTTP {exc.response.status_code}: {body}") from exc
        except httpx.RequestError as exc:
            if attempt < max_retries - 1:
                import time
                time.sleep(2 ** attempt)
                continue
            raise error_cls(f"Cannot reach Gemini API: {exc}") from exc

    raw_text = _read_gemini_text(response.json(), error_cls)
    return _parse_json_object(raw_text, error_cls)



```
