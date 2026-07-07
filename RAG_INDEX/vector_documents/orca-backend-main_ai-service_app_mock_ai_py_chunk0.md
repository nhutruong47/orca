# Knowledge Document: mock_ai.py (Chunk 1/7)

## Metadata
```json
{
  "file_path": "orca-backend-main/ai-service/app/mock_ai.py",
  "language": "py",
  "module": "app",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
from __future__ import annotations

import re
from datetime import datetime, timedelta
from typing import Any

from app.models import (
    ExtractRequest,
    ExtractResponse,
    PlanDraftResponse,
    PlanRequest,
    ReviseRequest,
    TaskDraft,
    TeamMemberContext,
)


def extract(request: ExtractRequest) -> ExtractResponse:
    text = request.text.strip()
    normalized = text.lower()

    if any(keyword in normalized for keyword in ["quét", "dọn", "sắp xếp", "vệ sinh", "kiểm tra máy"]):
        return _extract_operation(text, normalized)

    has_production_keyword = any(keyword in normalized for keyword in ["sản xuất", "rang", "kg", "hộp", "robusta", "arabica"])
    has_make_with_quantity = "làm" in normalized and re.search(r"\d+", normalized)
    if has_production_keyword or has_make_with_quantity:
        return _extract_production(text, normalized)

    return ExtractResponse(
        intent="UNKNOWN",
        confidence=0.35,
        fields={},
        missingFields=["taskDescription"],
        clarifyingQuestion="Anh/chị muốn tạo công việc gì và hạn hoàn thành khi nào?",
    )


def plan(request: PlanRequest) -> PlanDraftResponse:
    if request.intent == "PRODUCTION_PLAN":
        return _plan_production(request.fields, request.members)

    if request.intent == "OPERATION_TASK":
        return _plan_operation(request.fields, request.members)

    raise ValueError("Cannot create a plan for UNKNOWN intent.")


def revise(request: ReviseRequest) -> PlanDraftResponse:
    instruction = request.instruction.lower()
    draft = request.draft.model_copy(deep=True)

    count_match = re.search(r"(\d+)\s*task", instruction)
    if "rút gọn" in instruction and count_match:
        target_count = max(1, int(count_match.group(1)))
        draft.tasks = draft.tasks[:target_count]
        return draft

    if "kiểm tra chất lượng" in instruction or "qc" in instruction:
        assignee = _find_member(request.members, ["qc", "kiểm", "quality"])
        draft.tasks.append(
            TaskDraft(
                title="Kiểm tra chất lượng cuối cùng",
                description="Xác nhận kết quả hoàn thành đạt yêu cầu trước khi đóng mục tiêu.",
                priority=3,
                workload=1.0,
                suggestedAssigneeId=assignee["id"] if assignee else None,
                suggestedAssigneeName=assignee["name"] if assignee else None,

```
