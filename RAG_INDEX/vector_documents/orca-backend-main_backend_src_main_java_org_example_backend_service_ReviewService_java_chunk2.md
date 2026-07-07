# Knowledge Document: ReviewService.java (Chunk 3/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ReviewService.java",
  "language": "java",
  "module": "service",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Service",
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
() != null
                && review.getBuyerTeam().getOwner() != null
                && review.getBuyerTeam().getOwner().getId().equals(currentUser.getId());
        if (!isBuyerUser && !isBuyerTeamOwner) {
            throw new RuntimeException("Bạn chỉ được sửa hoặc xóa đánh giá của mình.");
        }
    }

    private void validateRating(int rating) {
        if (rating < 1 || rating > 5) {
            throw new RuntimeException("Đánh giá phải từ 1 đến 5 sao.");
        }
    }

    private void validateDeliveryResult(String deliveryResult) {
        if (!"ON_TIME".equals(deliveryResult) && !"LATE".equals(deliveryResult) && !"NOT_DELIVERED".equals(deliveryResult)) {
            throw new RuntimeException("Trạng thái giao hàng không hợp lệ.");
        }
    }

    private void adjustDeliveryStats(Team team, String oldResult, String newResult) {
        if (oldResult != null && oldResult.equals(newResult)) return;
        if ("ON_TIME".equals(oldResult)) {
            team.setOnTimeOrders(Math.max(0, team.getOnTimeOrders() - 1));
        } else if ("LATE".equals(oldResult)) {
            team.setLateOrders(Math.max(0, team.getLateOrders() - 1));
        }
        if ("ON_TIME".equals(newResult)) {
            team.setOnTimeOrders(team.getOnTimeOrders() + 1);
        } else if ("LATE".equals(newResult)) {
            team.setLateOrders(team.getLateOrders() + 1);
        }
    }

    public ReviewDTO toDTO(Review r) {
        ReviewDTO dto = new ReviewDTO();
        dto.setId(r.getId().toString());
        dto.setOrderId(r.getOrder().getId().toString());
        dto.setBuyerTeamId(r.getBuyerTeam() != null ? r.getBuyerTeam().getId().toString() : null);
        dto.setBuyerUserId(r.getBuyerUser() != null ? r.getBuyerUser().getId().toString() : null);
        dto.setSellerTeamId(r.getSellerTeam().getId().toString());
        dto.setRating(r.getRating());
        dto.setProductQuality(r.getProductQuality());
        dto.setDeliverySchedule(r.getDeliverySchedule());
        dto.setCustomerSupport(r.getCustomerSupport());
        dto.setOverallRating(r.getOverallRating());
        dto.setComment(r.getComment());
        dto.setImages(r.getImages());
        dto.setDeliveryResult(r.getDeliveryResult());
        dto.setCreatedAt(r.getCreatedAt());
        if (r.getBuyerTeam() != null) dto.setBuyerTeamName(r.getBuyerTeam().getName());

```
