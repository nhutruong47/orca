# Knowledge Document: gemini_ai.py (Chunk 21/21)

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
  "chunk_index": 20,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
try:
        candidates = body["candidates"]
        parts = candidates[0]["content"]["parts"]
        text = "".join(part.get("text", "") for part in parts)
    except (KeyError, IndexError, TypeError) as exc:
        raise error_cls(f"Gemini API response did not contain text: {body}") from exc

    if not text.strip():
        raise error_cls("Gemini API returned empty text.")
    return text


def _parse_json_object(raw_text: str, error_cls: Type[RuntimeError]) -> dict:
    text = raw_text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if not match:
            raise error_cls(f"Gemini output is not JSON: {raw_text[:1000]}")
        try:
            parsed = json.loads(match.group(0))
        except json.JSONDecodeError as exc:
            raise error_cls(f"Gemini output contains invalid JSON: {raw_text[:1000]}") from exc

    if not isinstance(parsed, dict):
        raise error_cls("Gemini output must be a JSON object.")
    return parsed

```
