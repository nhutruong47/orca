# Knowledge Document: ReviewService.java (Chunk 2/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ReviewService.java",
  "language": "java",
  "module": "service",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
validateReviewOwner(review, currentUser);
        validateRating(rating);
        validateDeliveryResult(deliveryResult);

        int oldRating = review.getRating();
        String oldDeliveryResult = review.getDeliveryResult();
        review.setRating(rating);
        review.setComment(comment);
        review.setDeliveryResult(deliveryResult);
        review.setProductQuality(productQuality);
        review.setDeliverySchedule(deliverySchedule);
        review.setCustomerSupport(customerSupport);
        review.setOverallRating(overallRating);
        review.setImages(images);
        if (review.getOrder() != null) {
            review.getOrder().setDeliveryStatus(deliveryResult);
        }

        Team sellerTeam = review.getSellerTeam();
        sellerTeam.setSumRatings(Math.max(0.0, sellerTeam.getSumRatings() + rating - oldRating));
        adjustDeliveryStats(sellerTeam, oldDeliveryResult, deliveryResult);
        teamRepo.save(sellerTeam);

        return toDTO(reviewRepo.save(review));
    }

    @Transactional
    public void deleteReview(UUID reviewId, User currentUser) {
        Review review = reviewRepo.findById(reviewId)
                .orElseThrow(() -> new RuntimeException("Review not found"));
        validateReviewOwner(review, currentUser);

        Team sellerTeam = review.getSellerTeam();
        sellerTeam.setTotalRatings(Math.max(0, sellerTeam.getTotalRatings() - 1));
        sellerTeam.setSumRatings(Math.max(0.0, sellerTeam.getSumRatings() - review.getRating()));
        teamRepo.save(sellerTeam);
        reviewRepo.delete(review);
    }

    private void validateReviewOwner(Review review, User currentUser) {
        if (currentUser == null) {
            throw new RuntimeException("Bạn cần đăng nhập để thao tác đánh giá.");
        }
        boolean isBuyerUser = review.getBuyerUser() != null
                && review.getBuyerUser().getId().equals(currentUser.getId());
        boolean isBuyerTeamOwner = review.getBuyerTeam() != null
                && review.getBuyerTeam().getOwner() != null
                && review.getBuyerTeam().getOwner().getId().equals(currentUser.getId());
        if (!isBuyerUser && !isBuyerTeamOwner) {
            throw new RuntimeException("Bạn chỉ được sửa hoặc xóa đánh giá của mình.");
        }
    }

    private void validateRating(int rating) {
        if (rating < 1 || rating > 5) {

```
