# Knowledge Document: mock_ai.py (Chunk 2/7)

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
  "chunk_index": 1,
  "total_chunks": 7
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

    new_deadline = _infer_deadline(instruction)
    if new_deadline and ("deadline" in instruction or "hạn" in instruction or "đổi" in instruction):
        draft.deadline = new_deadline
        return draft

    priority_match = re.search(r"(cao nhất|ưu tiên cao|priority cao)", instruction)
    if priority_match:
        target = _find_priority_target_task(draft.tasks, instruction)
        if target:
            target.priority = 5
        return draft

    return draft


def _extract_production(text: str, normalized: str) -> ExtractResponse:
    quantity_match = re.search(r"(\d+(?:[.,]\d+)?)\s*(kg|hộp|túi|bao|cái)?", normalized)
    quantity = None
    unit = None
    if quantity_match:
        quantity = float(quantity_match.group(1).replace(",", "."))
        if quantity.is_integer():
            quantity = int(quantity)
        unit = quantity_match.group(2) or "đơn vị"

    product = None
    if "robusta" in normalized:
        product = "Robusta"
    elif "arabica" in normalized:
        product = "Arabica"
    elif "cà phê" in normalized:
        product = "cà phê"

    deadline = _infer_deadline(normalized)
    missing = []
    if product is None:
        missing.append("productName")
    if quantity is None:
        missing.append("quantity")
    if deadline is None:
        missing.append("deadline")

    fields: dict[str, Any] = {}
    if product:
        fields["productName"] = product
    if quantity is not None:
        fields["quantity"] = quantity
        fields["unit"] = unit
    if deadline:
        fields["deadline"] = deadline
    fields["priority"] = "HIGH" if "gấp" in normalized or "trước" in normalized else "MEDIUM"
    if product and quantity is not None:
        fields["title"] = f"Sản xuất {quantity}{unit if unit else ''} {product}"

    question = None
    if missing:

```
