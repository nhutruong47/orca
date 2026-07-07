# Knowledge Document: ReviewController.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/ReviewController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "factory",
  "tags": [
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
 > 0
                ? team.getSumRatings() / team.getTotalRatings()
                : 0.0;
        double onTimeRate = team.getTotalOrders() > 0
                ? (double) team.getOnTimeOrders() / team.getTotalOrders() * 100
                : 0.0;
        return ResponseEntity.ok(Map.of(
                "avgRating", Math.round(avgRating * 10.0) / 10.0,
                "reviewCount", reviewCount,
                "onTimeRate", Math.round(onTimeRate),
                "completedOrders", team.getCompletedOrders(),
                "totalOrders", team.getTotalOrders(),
                "onTimeOrders", team.getOnTimeOrders(),
                "lateOrders", team.getLateOrders(),
                "starCounts", reviewService.getStarCounts(teamId)
        ));
    }

    @PutMapping("/{reviewId}")
    public ResponseEntity<?> updateReview(@PathVariable UUID reviewId,
            @RequestBody Map<String, Object> payload,
            @AuthenticationPrincipal User user) {
        try {
            int rating = ((Number) payload.get("rating")).intValue();
            String comment = (String) payload.getOrDefault("comment", "");
            String deliveryResult = (String) payload.get("deliveryResult");
            Integer qualityScore = payload.containsKey("qualityScore") ? ((Number) payload.get("qualityScore")).intValue() : null;
            Integer timeScore = payload.containsKey("timeScore") ? ((Number) payload.get("timeScore")).intValue() : null;
            Integer communicationScore = payload.containsKey("communicationScore") ? ((Number) payload.get("communicationScore")).intValue() : null;
            Integer supportScore = payload.containsKey("supportScore") ? ((Number) payload.get("supportScore")).intValue() : null;
            String replyText = (String) payload.get("replyText");

            return ResponseEntity.ok(reviewService.updateReview(reviewId, rating, comment, deliveryResult, qualityScore, timeScore, communicationScore, supportScore, replyText, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @DeleteMapping("/{reviewId}")
    public ResponseEntity<?> deleteReview(@PathVariable UUID reviewId,
            @AuthenticationPrincipal User user) {
        try {
            reviewService.deleteReview(reviewId, user);

```
