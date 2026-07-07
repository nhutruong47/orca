# Knowledge Document: AiServiceClient.java (Chunk 1/7)

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
  "chunk_index": 0,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, chat

## Source Code Chunk
```java
package org.example.backend.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.example.backend.dto.AiParseResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.*;
import java.util.*;

import org.example.backend.repository.TeamMemberRepository;
import org.example.backend.repository.InventoryRepository;
import org.example.backend.entity.InventoryItem;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
public class AiServiceClient {

    private static final Logger logger = LoggerFactory.getLogger(AiServiceClient.class);

    @Value("${ai.service.api-key:}")
    private String geminiApiKey;

    private final RestTemplate restTemplate = new RestTemplate();
    private final ObjectMapper objectMapper = new ObjectMapper();
    
    private final InventoryRepository inventoryRepository;

    public AiServiceClient(InventoryRepository inventoryRepository) {
        this.inventoryRepository = inventoryRepository;
    }

    @jakarta.annotation.PostConstruct
    public void init() {
        if (this.geminiApiKey != null) {
            this.geminiApiKey = this.geminiApiKey.trim();
            logger.info("DEBUG AiServiceClient - Gemini API Key Initialized, Length: {}", this.geminiApiKey.length());
        } else {
            logger.error("DEBUG AiServiceClient - Gemini API Key is MISSING!");
        }
    }

    public AiParseResult generateTaskPlan(String outputTarget, String deadline, Integer priority,
            UUID teamId, Map<String, List<String>> memberLabels) {
        String input = outputTarget;
        if (deadline != null && !deadline.isEmpty()) {
            input += ", hạn chót: " + deadline;
        }

        StringBuilder context = new StringBuilder();
        if (memberLabels != null && !memberLabels.isEmpty()) {
            context.append("--- DANH SÁCH NHÂN SỰ ---\n");
            for (Map.Entry<String, List<String>> entry : memberLabels.entrySet()) {
                String name = entry.getKey();
                List<String> labels = entry.getValue();
                context.append("- ").append(name);
                if (labels != null && !labels.isEmpty()) {

```
