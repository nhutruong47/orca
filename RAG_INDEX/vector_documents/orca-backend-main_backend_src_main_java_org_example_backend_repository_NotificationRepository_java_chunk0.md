# Knowledge Document: NotificationRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/NotificationRepository.java",
  "language": "java",
  "module": "repository",
  "business_domain": "notification",
  "tags": [
    "notification"
  ],
  "logical_type": "Repository",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Repository in repository.
- **Dependencies**: Refer to module imports.
- **Tags**: notification

## Source Code Chunk
```java
package org.example.backend.repository;

import org.example.backend.entity.Notification;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.UUID;

public interface NotificationRepository extends JpaRepository<Notification, UUID> {
    List<Notification> findByUserIdOrderByCreatedAtDesc(UUID userId);
    long countByUserIdAndIsReadFalse(UUID userId);
}

```
