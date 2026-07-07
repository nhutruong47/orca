# Knowledge Document: AiServiceClient.java (Chunk 2/7)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AiServiceClient.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory",
    "chat"
  ],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, chat

## Source Code Chunk
```java
Labels != null && !memberLabels.isEmpty()) {
            context.append("--- DANH SÁCH NHÂN SỰ ---\n");
            for (Map.Entry<String, List<String>> entry : memberLabels.entrySet()) {
                String name = entry.getKey();
                List<String> labels = entry.getValue();
                context.append("- ").append(name);
                if (labels != null && !labels.isEmpty()) {
                    context.append(" (Kỹ năng/Nhãn: ").append(String.join(", ", labels)).append(")");
                } else {
                    context.append(" (Chưa gán nhãn)");
                }
                context.append("\n");
            }
        }

        if (teamId != null) {
            List<InventoryItem> items = inventoryRepository.findByTeamIdOrderByLastUpdatedDesc(teamId);
            if (!items.isEmpty()) {
                context.append("\n--- TÌNH TRẠNG KHO HIỆN TẠI ---\n");
                for (InventoryItem item : items) {
                    context.append("- ").append(item.getName())
                           .append(": ").append(item.getQuantity()).append(" ").append(item.getUnit())
                           .append(" (Trạng thái: ").append(item.getStockStatus()).append(")\n");
                }
            }
        }

        return parseTask(input, teamId, context.toString(), null);
    }

    public AiParseResult parseTask(String text, java.util.UUID teamId) {
        return parseTask(text, teamId, null, null);
    }

    public AiParseResult parseTask(String text, java.util.UUID teamId, String memberContext, String historyContext) {
        String inventoryContext = "";
        if (teamId != null) {
            List<InventoryItem> items = inventoryRepository.findByTeamIdOrderByLastUpdatedDesc(teamId);
            if (!items.isEmpty()) {
                StringBuilder sb = new StringBuilder();
                sb.append("\n--- TÌNH TRẠNG KHO HIỆN TẠI ---\n");
                for (InventoryItem item : items) {
                    sb.append("- ").append(item.getName())
                      .append(": ").append(item.getQuantity()).append(" ").append(item.getUnit()).append("\n");
                }
                sb.append("LƯU Ý QUAN TRỌNG: Nếu yêu cầu sản lượng VƯỢT QUÁ số lượng nguyên liệu có trong kho, BẠN PHẢI GHI CẢNH BÁO RÕ RÀNG vào đầu mục 'description' (VD: ⚠️ CẢNH BÁO: Trong kho chỉ còn ... không đủ nguyên liệu).\n\n");

```
