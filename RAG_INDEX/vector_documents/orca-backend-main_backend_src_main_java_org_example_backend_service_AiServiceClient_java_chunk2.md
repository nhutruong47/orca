# Knowledge Document: AiServiceClient.java (Chunk 3/7)

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
  "chunk_index": 2,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, chat

## Source Code Chunk
```java
end("- ").append(item.getName())
                      .append(": ").append(item.getQuantity()).append(" ").append(item.getUnit()).append("\n");
                }
                sb.append("LƯU Ý QUAN TRỌNG: Nếu yêu cầu sản lượng VƯỢT QUÁ số lượng nguyên liệu có trong kho, BẠN PHẢI GHI CẢNH BÁO RÕ RÀNG vào đầu mục 'description' (VD: ⚠️ CẢNH BÁO: Trong kho chỉ còn ... không đủ nguyên liệu).\n\n");
                inventoryContext = sb.toString();
            }
        }

        AiParseResult result = null;
        if (geminiApiKey != null && !geminiApiKey.isEmpty()) {
            try {
                result = parseWithGemini(text, memberContext, historyContext, inventoryContext);
            } catch (Exception e) {
                logger.error("⚠️ Lỗi gọi Gemini: {}", e.getMessage(), e);
                result = new AiParseResult();
                result.setTitle("LỖI KẾT NỐI AI");
                result.setDescription("❌ Google Cloud từ chối kết nối. Lỗi chi tiết: **" + e.getMessage() + "**\n\nNếu bạn thấy lỗi 403 hoặc 400, có nghĩa là **API Key này đã bị hỏng/hết hạn hoặc chưa được cấp quyền truy cập AI**.");
                result.setNeedsClarification(true);
            }
        }
        if (result == null) {
            result = parseWithRegex(text);
        }

        if (result.getTasks() == null || result.getTasks().isEmpty()) {
            List<Map<String, Object>> fallbackTasks = new ArrayList<>();
            Map<String, Object> genericTask = new HashMap<>();
            genericTask.put("title", "Xử lý yêu cầu: " + (result.getTitle() != null ? result.getTitle() : text));
            genericTask.put("description", result.getDescription() != null ? result.getDescription() : "Thực hiện công việc theo yêu cầu.");
            genericTask.put("workload", 8.0);
            genericTask.put("priority", 2);
            genericTask.put("assigneeRole", "Senior");
            fallbackTasks.add(genericTask);
            result.setTasks(fallbackTasks);
        }
        
        return result;
    }

    private AiParseResult parseWithGemini(String text, String memberContext, String historyContext, String inventoryContext) throws Exception {
        String memberSection = "";
        if (memberContext != null && !memberContext.isEmpty()) {
            memberSection = "\n--- DANH SÁCH THÀNH VIÊN VÀ NHÃN DÁN CÔNG VIỆC ---\n"

```
