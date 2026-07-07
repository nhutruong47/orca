# Knowledge Document: InventoryRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/InventoryRepository.java",
  "language": "java",
  "module": "repository",
  "business_domain": "inventory",
  "tags": [
    "inventory"
  ],
  "logical_type": "Repository",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Repository in repository.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory

## Source Code Chunk
```java
package org.example.backend.repository;

import org.example.backend.entity.InventoryItem;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface InventoryRepository extends JpaRepository<InventoryItem, UUID> {
    List<InventoryItem> findByTeamIdOrderByLastUpdatedDesc(UUID teamId);

    List<InventoryItem> findByTeamIdOrderByProductTypeAscProductStateAsc(UUID teamId);

    Optional<InventoryItem> findByTeamIdAndProductTypeAndProductState(UUID teamId, String productType, String productState);

    List<InventoryItem> findByTeamIdAndProductType(UUID teamId, String productType);

    List<InventoryItem> findByTeamIdAndProductState(UUID teamId, String productState);

    List<InventoryItem> findByIsFeaturedTrue();

    boolean existsByTeamId(UUID teamId);
}

```
