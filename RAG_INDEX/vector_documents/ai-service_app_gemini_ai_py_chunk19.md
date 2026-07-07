# Knowledge Document: gemini_ai.py (Chunk 20/24)

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
  "chunk_index": 19,
  "total_chunks": 24
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py


def task_text_for_matching(task: TaskDraft) -> str:
    return " ".join([task.title, task.description, task.suggestedReason or ""]).lower()


def task_scope_text_for_matching(task: TaskDraft) -> str:
    return " ".join([task.title, task.description]).lower()


def _normalize_match_text(value: str) -> str:
    text = value.lower().replace("đ", "d")
    text = unicodedata.normalize("NFKD", text)
    return "".join(char for char in text if not unicodedata.combining(char))


def _normalize_revise_instruction(value: str) -> str:
    text = _normalize_match_text(value)
    replacements = {
        r"\b(taks|tas|taskk|tsk)\b": "task",
        r"\b(dedline|deadlin|dealin|dealine|dedlin)\b": "deadline",
        r"\buu\s*tin\b": "uu tien",
        r"\buu\s*tienn\b": "uu tien",
        r"\bu\s*tien\b": "uu tien",
        r"\brut\s*gon\b": "rut gon",
        r"\bcao\s*nhat\b": "cao nhat",
    }
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)
    return re.sub(r"\s+", " ", text).strip()


def _operation_scope_text(draft: PlanDraftResponse) -> str:
    parts = [draft.goalTitle, draft.outputTarget]
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

```
