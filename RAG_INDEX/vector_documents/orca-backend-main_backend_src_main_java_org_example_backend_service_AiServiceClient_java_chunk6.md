# Knowledge Document: AiServiceClient.java (Chunk 7/7)

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
  "chunk_index": 6,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, chat

## Source Code Chunk
```java
   throw new Exception("AI không đưa ra phản hồi phù hợp.");
        }

        String responseText = candidate.path("content").path("parts").get(0).path("text").asText();

        String jsonStr = responseText.trim();
        if (jsonStr.startsWith("```json")) jsonStr = jsonStr.substring(7).trim();
        if (jsonStr.endsWith("```")) jsonStr = jsonStr.substring(0, jsonStr.length() - 3).trim();

        return objectMapper.readValue(jsonStr, AiParseResult.class);
    }

    private AiParseResult parseWithRegex(String text) {
        AiParseResult result = new AiParseResult();
        result.setSource("regex");
        result.setTitle("Kế hoạch: " + text.substring(0, Math.min(text.length(), 50)));
        result.setDescription("Hệ thống tự động biên dịch do AI Model gặp lỗi hoặc không khả dụng.");
        result.setNeedsClarification(false);
        return result;
    }
}

```
