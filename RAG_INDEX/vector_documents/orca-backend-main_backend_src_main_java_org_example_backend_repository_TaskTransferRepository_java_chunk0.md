# Knowledge Document: TaskTransferRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/TaskTransferRepository.java",
  "language": "java",
  "module": "repository",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Repository",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Repository in repository.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.repository;

import org.example.backend.entity.TaskTransfer;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.UUID;

public interface TaskTransferRepository extends JpaRepository<TaskTransfer, UUID> {
    List<TaskTransfer> findByTaskIdOrderByCreatedAtDesc(UUID taskId);
}
```
