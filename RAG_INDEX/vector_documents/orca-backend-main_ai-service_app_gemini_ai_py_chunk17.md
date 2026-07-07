# Knowledge Document: gemini_ai.py (Chunk 18/21)

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
  "chunk_index": 17,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
rget]
    for task in draft.tasks:
        parts.extend([task.title, task.description])
    return " ".join(parts).lower()


def _is_blank(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str) and not value.strip():
        return True
    return False


def _is_generic_product_name(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    normalized = value.strip().lower()
    return normalized in {"sản phẩm", "cà phê", "hàng", "đơn hàng", "mặt hàng"}


def _local_now() -> datetime:
    try:
        return datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")).replace(second=0, microsecond=0)
    except Exception:
        return datetime.now().replace(second=0, microsecond=0)


def _generate_json_object(prompt: str, max_output_tokens: int, error_cls: Type[RuntimeError]) -> dict:
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

```
