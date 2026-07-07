# Knowledge Document: gemini_ai.py (Chunk 1/21)

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
  "chunk_index": 0,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
from __future__ import annotations

import json
import re
import unicodedata
from datetime import datetime
from typing import Any, Type
from zoneinfo import ZoneInfo

import httpx
from pydantic import ValidationError

from app.config import settings
from app.models import ExtractRequest, ExtractResponse, PlanDraftResponse, PlanRequest, ReviseRequest, TaskDraft


class GeminiExtractError(RuntimeError):
    pass


class GeminiPlanError(RuntimeError):
    pass


class GeminiPlanInputError(GeminiPlanError):
    pass


class GeminiReviseError(RuntimeError):
    pass


def extract(request: ExtractRequest) -> ExtractResponse:
    prompt = _build_extract_prompt(request)
    data = _generate_json_object(prompt, max_output_tokens=2048, error_cls=GeminiExtractError)
    try:
        return ExtractResponse.model_validate(data)
    except ValidationError as exc:
        raise GeminiExtractError(f"Gemini extract JSON failed schema validation: {exc}") from exc


def plan(request: PlanRequest) -> PlanDraftResponse:
    _validate_plan_input(request)
    prompt = _build_plan_prompt(request)
    data = _generate_json_object(prompt, max_output_tokens=8192, error_cls=GeminiPlanError)
    try:
        draft = PlanDraftResponse.model_validate(data)
    except ValidationError as exc:
        raise GeminiPlanError(f"Gemini plan JSON failed schema validation: {exc}") from exc
    return _validate_plan_output(draft, request)


def revise(request: ReviseRequest) -> PlanDraftResponse:
    if _is_ambiguous_revise_instruction(request.instruction):
        return request.draft

    safe_draft = _revise_with_safe_rule(request)
    if safe_draft is not None:
        return safe_draft

    prompt = _build_revise_prompt(request)
    data = _generate_json_object(prompt, max_output_tokens=8192, error_cls=GeminiReviseError)
    try:
        draft = PlanDraftResponse.model_validate(data)
    except ValidationError as exc:
        raise GeminiReviseError(f"Gemini revise JSON failed schema validation: {exc}") from exc
    draft = _normalize_revise_output(draft, request)
    return _validate_revise_output(draft, request)


def _build_extract_prompt(request: ExtractRequest) -> str:
    now = _local_now()
    return f"""
You are ORCA AI v2 extract module for a Vietnamese workshop/task management app.

Your only job is to classify the user request and extract structured fields.

```
