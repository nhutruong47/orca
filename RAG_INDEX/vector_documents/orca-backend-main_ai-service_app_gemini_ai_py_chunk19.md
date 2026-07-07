# Knowledge Document: gemini_ai.py (Chunk 20/21)

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
  "chunk_index": 19,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
=payload,
            timeout=settings.gemini_timeout_seconds,
        )
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        body = exc.response.text[:1000]
        raise error_cls(f"Vertex AI API returned HTTP {exc.response.status_code}: {body}") from exc
    except httpx.RequestError as exc:
        raise error_cls(f"Cannot reach Vertex AI API: {exc}") from exc

    raw_text = _read_gemini_text(response.json(), error_cls)
    return _parse_json_object(raw_text, error_cls)


def _vertex_model_name() -> str:
    model = _clean_env_value(settings.vertex_model)
    if model.startswith("projects/"):
        return model
    return (
        f"projects/{_clean_env_value(settings.vertex_project_id)}/locations/{_clean_env_value(settings.vertex_location)}"
        f"/publishers/google/models/{model}"
    )


def _vertex_service_endpoint() -> str:
    location = _clean_env_value(settings.vertex_location)
    if location == "global":
        return "aiplatform.googleapis.com"
    return f"{location}-aiplatform.googleapis.com"


def _clean_env_value(value: str) -> str:
    return value.strip().strip('"').strip("'")


def _vertex_access_token(error_cls: Type[RuntimeError]) -> str:
    try:
        import google.auth
        from google.auth.transport.requests import Request
    except ImportError as exc:
        raise error_cls("google-auth is required when AI_PROVIDER=vertex. Run pip install -r requirements.txt.") from exc

    try:
        credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
        credentials.refresh(Request())
    except Exception as exc:
        raise error_cls(
            "Cannot get Vertex AI credentials. Set GOOGLE_APPLICATION_CREDENTIALS to a service account JSON "
            "or run gcloud auth application-default login."
        ) from exc

    return credentials.token


def _read_gemini_text(body: dict, error_cls: Type[RuntimeError]) -> str:
    try:
        candidates = body["candidates"]
        parts = candidates[0]["content"]["parts"]
        text = "".join(part.get("text", "") for part in parts)
    except (KeyError, IndexError, TypeError) as exc:
        raise error_cls(f"Gemini API response did not contain text: {body}") from exc

    if not text.strip():
        raise error_cls("Gemini API returned empty text.")
    return text



```
