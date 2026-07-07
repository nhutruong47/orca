# Knowledge Document: mock_ai.py (Chunk 2/8)

## Metadata
```json
{
  "file_path": "ai-service/app/mock_ai.py",
  "language": "py",
  "module": "app",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
t.tasks.append(
            TaskDraft(
                title="Kiểm tra chất lượng cuối cùng",
                description="Xác nhận kết quả hoàn thành đạt yêu cầu trước khi đóng mục tiêu.",
                priority=3,
                workload=1.0,
                suggestedAssigneeId=assignee["id"] if assignee else None,
                suggestedAssigneeName=assignee["name"] if assignee else None,
                suggestedReason=assignee["reason"] if assignee else "Chưa có thành viên có nhãn QC rõ ràng.",
            )
        )
        return draft

    added_task_match = re.search(
        r"\bthêm(?:\s+\d+)?\s+(?:mục|task|công việc)(?:\s+nữa)?(?:\s+(?:là|về|cho))?\s*[:\-]?\s*(.+)$",
        instruction,
    )
    if added_task_match:
        title = added_task_match.group(1).strip(" .,:;-")
        title = re.sub(r"^(?:mục|task|công việc)\s*(?:số)?\s*\d+\s*(?:là|:|-)?\s*", "", title).strip()
        if title:
            assignee = _find_member(request.members, ["vận chuyển", "giao hàng", "logistics", "kho", "ship"])
            draft.tasks.append(
                TaskDraft(
                    title=title[0].upper() + title[1:],
                    description=f"Thực hiện công việc {title.lower()} theo yêu cầu của kế hoạch.",
                    priority=3,
                    workload=1.0,
                    suggestedAssigneeId=assignee["id"] if assignee else None,
                    suggestedAssigneeName=assignee["name"] if assignee else None,
                    suggestedReason=assignee["reason"] if assignee else None,
                )
            )
            return draft

    remove_task_match = re.search(r"\b(?:xóa|bỏ|loại bỏ)(?:\s+đi)?\s+(?:mục|task|công việc)?\s*[:\-]?\s*(.+)$", instruction)
    if remove_task_match:
        query = remove_task_match.group(1).strip(" .,:;-").lower()
        number_match = re.fullmatch(r"(?:mục|task|công việc)?\s*(?:số)?\s*(\d+)", query)
        if number_match:
            requested_index = int(number_match.group(1)) - 1
            task_index = requested_index if 0 <= requested_index < len(draft.tasks) else None
        elif query in {"cuối", "mục cuối", "task cuối", "công việc cuối"}:
            task_index = len(draft.tasks) - 1 if draft.tasks else None
        else:
            task_index = next(

```
