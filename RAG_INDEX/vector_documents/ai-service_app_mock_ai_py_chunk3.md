# Knowledge Document: mock_ai.py (Chunk 4/8)

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
  "chunk_index": 3,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in app.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```py
malized)
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
        question = _production_question(product, missing)

    return ExtractResponse(
        intent="PRODUCTION_PLAN",
        confidence=0.78 if missing else 0.9,
        fields=fields,
        missingFields=missing,
        clarifyingQuestion=question,
    )


def _extract_operation(text: str, normalized: str) -> ExtractResponse:
    deadline = _infer_deadline(normalized)
    area = "xưởng" if "xưởng" in normalized else None
    if "khu đóng gói" in normalized:
        area = "khu đóng gói"
    elif "máy rang" in normalized:
        area = "máy rang"

    missing = [] if deadline else ["deadline"]
    title = text.rstrip(".")
    fields: dict[str, Any] = {
        "title": title,
        "priority": "MEDIUM",
    }
    if area:
        fields["area"] = area
    if deadline:
        fields["deadline"] = deadline

    return ExtractResponse(
        intent="OPERATION_TASK",
        confidence=0.92 if not missing else 0.82,
        fields=fields,
        missingFields=missing,
        clarifyingQuestion=None
        if not missing
        else "Anh/chị muốn hoàn thành công việc này vào thời điểm nào?",
    )



```
