# Knowledge Document: gemini_ai.py (Chunk 24/24)

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
  "chunk_index": 23,
  "total_chunks": 24
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
text)
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
