# Knowledge Document: gemini_ai.py (Chunk 14/21)

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
  "chunk_index": 13,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
nding_cooling_keywords):
        member = _find_member_by_labels(allowed_members, ["xay", "rang", "san xuat", "grinding", "cooling"])
        return _assign_if_found(task, member, "Phù hợp vì có nhãn xay/rang/sản xuất.")

    if any(keyword in text for keyword in production_keywords):
        member = _find_member_by_labels(allowed_members, ["rang", "san xuat", "roast", "production", "roasting"])
        return _assign_if_found(task, member, "Phù hợp vì có nhãn rang/sản xuất.")

    return task


def _find_member_by_labels(allowed_members: dict[str, Any], keywords: list[str]) -> Any | None:
    for member in allowed_members.values():
        labels = _normalize_match_text(" ".join(member.jobLabels))
        if labels and _has_matching_label(labels, keywords):
            return member
    return None


def _assign_if_found(task: TaskDraft, member: Any | None, reason: str) -> TaskDraft:
    if member is None:
        return task
    task.suggestedAssigneeId = member.userId
    task.suggestedAssigneeName = member.fullName or member.username
    task.suggestedReason = reason
    return task


def _has_matching_label(labels: str, keywords: list[str]) -> bool:
    return any(keyword in labels for keyword in keywords)


def _has_qc_intent(text: str) -> bool:
    normalized = _normalize_match_text(text)
    return any(keyword in normalized for keyword in ["qc", "chat luong", "quality", "kiem dinh", "cupping", "thu nem"])


def _clear_assignee(task: TaskDraft, reason: str) -> TaskDraft:
    task.suggestedAssigneeId = None
    task.suggestedAssigneeName = None
    task.suggestedReason = reason
    return task


def _require_task_count(tasks: list[TaskDraft], minimum: int, maximum: int) -> None:
    if not minimum <= len(tasks) <= maximum:
        raise GeminiPlanError(f"Gemini plan returned {len(tasks)} tasks, expected {minimum}..{maximum}.")


def _requested_task_count(instruction: str) -> int | None:
    if _mentions_any(instruction, ["tach", "them"]):
        return None
    if not _mentions_any(instruction, ["rut gon", "giam", "con", "chi"]):
        return None

    match = re.search(r"(\d+)\s*task", instruction)
    if not match:
        return None
    return max(1, int(match.group(1)))


def _requested_deadline(instruction: str) -> str | None:
    if not _mentions_any(instruction, ["deadline", "han", "thoi han", "doi"]):
        return None

```
