# Knowledge Document: ProductionPlanRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/ProductionPlanRepository.java",
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

import org.example.backend.entity.ProductionPlan;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface ProductionPlanRepository extends JpaRepository<ProductionPlan, UUID> {
    List<ProductionPlan> findByOrderIdOrderByCreatedAtDesc(UUID orderId);

    @Query("SELECT p FROM ProductionPlan p WHERE p.order.team.id = :teamId ORDER BY p.createdAt DESC")
    List<ProductionPlan> findByTeamId(@Param("teamId") UUID teamId);

    Optional<ProductionPlan> findTopByOrderIdOrderByCreatedAtDesc(UUID orderId);
}

```
