# Knowledge Document: ChatMessageDTO.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ChatMessageDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "chat",
  "tags": [
    "chat"
  ],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: chat

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDateTime;

public class ChatMessageDTO {
    private String id;
    private String teamId;
    private String senderId;
    private String senderName;
    private String recipientId;
    private String recipientName;
    private String content;
    private LocalDateTime createdAt;

    // === Getters & Setters ===
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getTeamId() { return teamId; }
    public void setTeamId(String teamId) { this.teamId = teamId; }

    public String getSenderId() { return senderId; }
    public void setSenderId(String senderId) { this.senderId = senderId; }

    public String getSenderName() { return senderName; }
    public void setSenderName(String senderName) { this.senderName = senderName; }

    public String getRecipientId() { return recipientId; }
    public void setRecipientId(String recipientId) { this.recipientId = recipientId; }

    public String getRecipientName() { return recipientName; }
    public void setRecipientName(String recipientName) { this.recipientName = recipientName; }

    public String getContent() { return content; }
    public void setContent(String content) { this.content = content; }

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}

```
