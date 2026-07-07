# Knowledge Document: gemini_ai.py (Chunk 13/21)

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
  "chunk_index": 12,
  "total_chunks": 21
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: chat, inventory, production, authorization

## Source Code Chunk
```py
s)):
            return _clear_assignee(task, "Chưa có thành viên có nhãn xay/làm nguội/sản xuất phù hợp.")
        return task

    if any(keyword in text for keyword in production_keywords):
        if not any(keyword in labels for keyword in production_keywords):
            return _clear_assignee(task, "Chưa có thành viên có nhãn rang/sản xuất phù hợp.")
        return task

    return task


def _fill_missing_production_assignee(task: TaskDraft, allowed_members: dict[str, Any]) -> TaskDraft:
    if task.suggestedAssigneeId:
        return task

    text = _normalize_match_text(task_scope_text_for_matching(task))

    packaging_keywords = ["dong goi", "dan nhan", "bao bi", "pack", "label", "packaging", "thanh pham", "dan tem"]
    production_keywords = ["rang", "san xuat", "van hanh may", "thuc hien san xuat", "say", "roast", "production", "roasting"]
    preparation_keywords = ["chuan bi", "so che", "sang loc", "nhan", "kho", "prepar", "green bean", "nhan xanh", "inventory"]
    grinding_cooling_keywords = ["xay", "nguoi", "grind", "cool", "xay bot", "cooling", "grinding"]

    if _has_qc_intent(text):
        member = _find_member_by_labels(allowed_members, ["qc", "kiem", "kiem tra", "chat luong", "quality", "cupping", "thu nem", "quality check"])
        return _assign_if_found(task, member, "Phù hợp vì có nhãn QC/kiểm tra chất lượng.")

    if any(keyword in text for keyword in packaging_keywords):
        member = _find_member_by_labels(allowed_members, ["dong goi", "bao bi", "pack", "dan nhan", "dan tem", "packaging", "label"])
        return _assign_if_found(task, member, "Phù hợp vì có nhãn đóng gói.")

    if any(keyword in text for keyword in preparation_keywords):
        member = _find_member_by_labels(allowed_members, ["so che", "chuan bi", "kho", "rang", "san xuat", "inventory"])
        return _assign_if_found(task, member, "Phù hợp vì có nhãn sơ chế/chuẩn bị/kho/rang.")

    if any(keyword in text for keyword in grinding_cooling_keywords):
        member = _find_member_by_labels(allowed_members, ["xay", "rang", "san xuat", "grinding", "cooling"])
        return _assign_if_found(task, member, "Phù hợp vì có nhãn xay/rang/sản xuất.")

    if any(keyword in text for keyword in production_keywords):
        member = _find_member_by_labels(allowed_members, ["rang", "san xuat", "roast", "production", "roasting"])

```
