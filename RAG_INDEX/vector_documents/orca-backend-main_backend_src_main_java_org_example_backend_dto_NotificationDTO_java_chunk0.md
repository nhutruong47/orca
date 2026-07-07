# Knowledge Document: NotificationDTO.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/NotificationDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "notification",
  "tags": [
    "notification"
  ],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: notification

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDateTime;

public class NotificationDTO {
    private String id;
    private String title;
    private String message;
    private String type;
    private String taskId;
    private boolean isRead;
    private LocalDateTime createdAt;

    // === Getters & Setters ===
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }

    public String getType() { return type; }
    public void setType(String type) { this.type = type; }

    public String getTaskId() { return taskId; }
    public void setTaskId(String taskId) { this.taskId = taskId; }

    public boolean isRead() { return isRead; }
    public void setRead(boolean read) { isRead = read; }

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}

```
