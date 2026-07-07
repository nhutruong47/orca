# Knowledge Document: SubscriptionPlanRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/SubscriptionPlanRepository.java",
  "language": "java",
  "module": "repository",
  "business_domain": "subscription",
  "tags": [
    "subscription"
  ],
  "logical_type": "Repository",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Repository in repository.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription

## Source Code Chunk
```java
package org.example.backend.repository;

import org.example.backend.entity.SubscriptionPlan;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface SubscriptionPlanRepository extends JpaRepository<SubscriptionPlan, UUID> {
}

```
