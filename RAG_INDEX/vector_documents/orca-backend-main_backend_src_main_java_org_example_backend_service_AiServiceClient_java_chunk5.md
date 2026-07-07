# Knowledge Document: AiServiceClient.java (Chunk 6/7)

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
  "chunk_index": 5,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, chat

## Source Code Chunk
```java
l = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key=" + geminiApiKey;
        
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        headers.set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36");
        
        String requestJson = objectMapper.writeValueAsString(requestBody);
        HttpEntity<String> entity = new HttpEntity<>(requestJson, headers);

        String responseBody;
        try {
            logger.info("📡 Calling Gemini API: {}", url);
            ResponseEntity<String> response = restTemplate.exchange(url, HttpMethod.POST, entity, String.class);
            responseBody = response.getBody();
        } catch (org.springframework.web.client.HttpClientErrorException.TooManyRequests e) {
            logger.error("🛑 Gemini Rate Limit (429) hit: {}", e.getResponseBodyAsString());
            throw new Exception("Hệ thống đang quá tải (Rate limit). Vui lòng thử lại sau giây lát.");
        } catch (Exception e) {
            logger.error("❌ Gemini Call Exception: {}", e.getMessage());
            throw e;
        }

        if (responseBody == null || responseBody.isBlank()) {
            throw new Exception("Gemini API returned an empty response.");
        }

        JsonNode rootNode;
        try {
            rootNode = objectMapper.readTree(responseBody);
        } catch (Exception e) {
            logger.error("❌ Failed to parse Gemini response as JSON. Body preview: {}", 
                responseBody.substring(0, Math.min(responseBody.length(), 500)));
            throw new Exception("Lỗi xử lý phản hồi từ AI. Bản tin không đúng định dạng.");
        }

        JsonNode candidate = rootNode.path("candidates").get(0);
        if (candidate.isMissingNode()) {
            logger.error("❌ No candidates in Gemini response: {}", responseBody);
            throw new Exception("AI không đưa ra phản hồi phù hợp.");
        }

        String responseText = candidate.path("content").path("parts").get(0).path("text").asText();

        String jsonStr = responseText.trim();
        if (jsonStr.startsWith("```json")) jsonStr = jsonStr.substring(7).trim();
        if (jsonStr.endsWith("```")) jsonStr = jsonStr.substring(0, jsonStr.length() - 3).trim();


```
