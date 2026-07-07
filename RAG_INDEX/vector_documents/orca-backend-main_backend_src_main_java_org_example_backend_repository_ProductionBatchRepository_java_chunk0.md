# Knowledge Document: ProductionBatchRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/ProductionBatchRepository.java",
  "language": "java",
  "module": "repository",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Repository",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Repository in repository.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
package org.example.backend.repository;

import org.example.backend.entity.ProductionBatch;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.UUID;

public interface ProductionBatchRepository extends JpaRepository<ProductionBatch, UUID> {
    List<ProductionBatch> findByTeamIdOrderByCreatedAtDesc(UUID teamId);
    List<ProductionBatch> findByOrderIdOrderByCreatedAtDesc(UUID orderId);
}

```
