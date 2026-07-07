# Knowledge Document: ReviewRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/ReviewRepository.java",
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

import org.example.backend.entity.Review;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface ReviewRepository extends JpaRepository<Review, UUID> {
    List<Review> findBySellerTeamIdOrderByCreatedAtDesc(UUID sellerTeamId);
    long countBySellerTeamId(UUID sellerTeamId);
    long countBySellerTeamIdAndRating(UUID sellerTeamId, int rating);
    boolean existsByOrderId(UUID orderId);
    Optional<Review> findByOrderId(UUID orderId);
    Optional<Review> findByOrderIdAndBuyerUserId(UUID orderId, UUID buyerUserId);
}

```
