# Knowledge Document: gemini_ai.py (Chunk 12/21)

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
  "chunk_index": 11,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
sk: TaskDraft, allowed_members: dict[str, Any]) -> TaskDraft:
    if not task.suggestedAssigneeId:
        return task

    member = allowed_members.get(task.suggestedAssigneeId)
    if member is None:
        return task

    labels = _normalize_match_text(" ".join(member.jobLabels))
    if not labels.strip():
        return _clear_assignee(task, "Chưa có thành viên có nhãn công việc phù hợp.")

    text = _normalize_match_text(task_scope_text_for_matching(task))
    packaging_keywords = ["dong goi", "dan nhan", "bao bi", "pack", "label", "packaging", "thanh pham", "dan tem"]
    production_keywords = ["rang", "san xuat", "van hanh may", "thuc hien san xuat", "say", "roast", "production", "roasting"]
    preparation_keywords = ["chuan bi", "so che", "sang loc", "nhan", "kho", "prepar", "green bean", "nhan xanh", "inventory"]
    grinding_cooling_keywords = ["xay", "nguoi", "grind", "cool", "xay bot", "cooling", "grinding"]

    if _has_qc_intent(text):
        if not _has_matching_label(labels, ["qc", "kiem", "kiem tra", "chat luong", "quality", "cupping", "thu nem", "quality check"]):
            return _clear_assignee(task, "Chưa có thành viên có nhãn QC/kiểm tra chất lượng phù hợp.")
        return task

    if any(keyword in text for keyword in packaging_keywords):
        if not any(keyword in labels for keyword in packaging_keywords):
            return _clear_assignee(task, "Chưa có thành viên có nhãn đóng gói phù hợp.")
        return task

    if any(keyword in text for keyword in preparation_keywords):
        if not any(keyword in labels for keyword in (preparation_keywords + production_keywords)):
            return _clear_assignee(task, "Chưa có thành viên có nhãn sơ chế/chuẩn bị/sản xuất phù hợp.")
        return task

    if any(keyword in text for keyword in grinding_cooling_keywords):
        if not any(keyword in labels for keyword in (grinding_cooling_keywords + production_keywords)):
            return _clear_assignee(task, "Chưa có thành viên có nhãn xay/làm nguội/sản xuất phù hợp.")
        return task

    if any(keyword in text for keyword in production_keywords):
        if not any(keyword in labels for keyword in production_keywords):
            return _clear_assignee(task, "Chưa có thành viên có nhãn rang/sản xuất phù hợp.")
        return task

    return task



```
