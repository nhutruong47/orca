# Knowledge Document: InterGroupOrderRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/InterGroupOrderRepository.java",
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

import org.example.backend.entity.InterGroupOrder;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.UUID;

public interface InterGroupOrderRepository extends JpaRepository<InterGroupOrder, UUID> {

    // Đơn mình đi đặt (Xưởng của mình là Buyer)
    List<InterGroupOrder> findByBuyerTeamIdOrderByCreatedAtDesc(UUID buyerTeamId);

    List<InterGroupOrder> findByBuyerUserIdOrderByCreatedAtDesc(UUID buyerUserId);

    // Đơn xưởng khác đặt mình (Xưởng của mình là Seller)
    List<InterGroupOrder> findBySellerTeamIdOrderByCreatedAtDesc(UUID sellerTeamId);
}

```
