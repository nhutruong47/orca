# Knowledge Document: ReviewService.java (Chunk 1/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ReviewService.java",
  "language": "java",
  "module": "service",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.ReviewDTO;
import org.example.backend.entity.Review;
import org.example.backend.entity.Team;
import org.example.backend.entity.User;
import org.example.backend.repository.ReviewRepository;
import org.example.backend.repository.TeamRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class ReviewService {

    private final ReviewRepository reviewRepo;
    private final TeamRepository teamRepo;

    public ReviewService(ReviewRepository reviewRepo, TeamRepository teamRepo) {
        this.reviewRepo = reviewRepo;
        this.teamRepo = teamRepo;
    }

    public List<ReviewDTO> getReviewsByTeam(UUID teamId) {
        return reviewRepo.findBySellerTeamIdOrderByCreatedAtDesc(teamId)
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    public long getReviewCount(UUID teamId) {
        return reviewRepo.countBySellerTeamId(teamId);
    }

    public Map<Integer, Long> getStarCounts(UUID teamId) {
        Map<Integer, Long> counts = new LinkedHashMap<>();
        for (int star = 5; star >= 1; star--) {
            counts.put(star, reviewRepo.countBySellerTeamIdAndRating(teamId, star));
        }
        return counts;
    }

    @Transactional
    public ReviewDTO updateReview(UUID reviewId, int rating, String comment, String deliveryResult,
                                   Integer productQuality, Integer deliverySchedule,
                                   Integer customerSupport, Integer overallRating,
                                   String images, User currentUser) {
        Review review = reviewRepo.findById(reviewId)
                .orElseThrow(() -> new RuntimeException("Review not found"));
        validateReviewOwner(review, currentUser);
        validateRating(rating);
        validateDeliveryResult(deliveryResult);

        int oldRating = review.getRating();
        String oldDeliveryResult = review.getDeliveryResult();
        review.setRating(rating);
        review.setComment(comment);
        review.setDeliveryResult(deliveryResult);
        review.setProductQuality(productQuality);

```
