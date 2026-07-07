# Knowledge Document: AiServiceClient.java (Chunk 5/7)

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
  "chunk_index": 4,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, chat

## Source Code Chunk
```java
ào và câu hỏi.\n"
                + "- Từng task ghi rõ [Ca: Sáng/Chiều] ở đầu mô tả.\n\n"
                + "3. PHONG CÁCH: Lịch sự, chuyên nghiệp, hỗ trợ tận tâm.\n\n"
                + "--- CONTEXT ---\n"
                + memberSection
                + historySection
                + (inventoryContext != null ? inventoryContext : "")
                + "Định dạng JSON Phản hồi (BẮT BUỘC):\n"
                + "{\n"
                + "  \"title\": \"Tên mục tiêu\",\n"
                + "  \"description\": \"Câu trả lời hoặc Bảng roadmap\",\n"
                + "  \"quantity\": \"Số lượng\",\n"
                + "  \"quantityNumber\": 100,\n"
                + "  \"unit\": \"đơn vị\",\n"
                + "  \"deadline\": \"YYYY-MM-DD\",\n"
                + "  \"priority\": \"High/Medium/Low\",\n"
                + "  \"needsClarification\": false,\n"
                + "  \"suggestedQuestions\": [\"Câu hỏi 1?\", \"Câu hỏi 2?\"],\n"
                + "  \"tasks\": [\n"
                + "    { \"title\": \"...\", \"description\": \"[Ca: ...] ...\", \"workload\": 8.0, \"priority\": 2, \"assignee\": \"...\", \"backupMember\": \"...\" }\n"
                + "  ]\n"
                + "}\n"
                + "Yêu cầu mới nhất của User: \"" + text + "\"";

        Map<String, Object> requestBody = new HashMap<>();
        Map<String, Object> contentMap = new HashMap<>();
        Map<String, Object> partMap = new HashMap<>();
        partMap.put("text", prompt);
        contentMap.put("role", "user");
        contentMap.put("parts", Collections.singletonList(partMap));
        requestBody.put("contents", Collections.singletonList(contentMap));

        Map<String, Object> generationConfig = new HashMap<>();
        generationConfig.put("temperature", 0.2);
        generationConfig.put("responseMimeType", "application/json");
        requestBody.put("generationConfig", generationConfig);

        String url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key=" + geminiApiKey;
        
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        headers.set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36");
        

```
