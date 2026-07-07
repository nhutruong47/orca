# Knowledge Document: ManufacturingRequestRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/ManufacturingRequestRepository.java",
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

import org.example.backend.entity.ManufacturingRequest;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Repository
public interface ManufacturingRequestRepository extends JpaRepository<ManufacturingRequest, UUID> {
    List<ManufacturingRequest> findAllByOrderByCreatedAtDesc();
}

```
