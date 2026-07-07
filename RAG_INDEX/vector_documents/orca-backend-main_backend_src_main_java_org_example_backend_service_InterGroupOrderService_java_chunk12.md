# Knowledge Document: InterGroupOrderService.java (Chunk 13/18)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/InterGroupOrderService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory",
    "production",
    "notification"
  ],
  "logical_type": "Service",
  "chunk_index": 12,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
.equals(currentUser.getId()));
        if (!isBuyer) {
            throw new RuntimeException("Chỉ bên mua mới xác nhận được giao hàng.");
        }

        if (order.getDeliveryConfirmed() != null && order.getDeliveryConfirmed()) {
            throw new RuntimeException("Đơn này đã được xác nhận trước đó.");
        }

        String safeStatus = "ON_TIME";
        if (deliveryStatus != null) {
            if (!"ON_TIME".equals(deliveryStatus) && !"LATE".equals(deliveryStatus) && !"NOT_DELIVERED".equals(deliveryStatus)) {
                throw new RuntimeException("Trạng thái giao hàng không hợp lệ.");
            }
            safeStatus = deliveryStatus;
        }

        int safeRating = rating == null ? 5 : rating;
        if (safeRating < 1 || safeRating > 5) {
            throw new RuntimeException("Đánh giá phải từ 1 đến 5 sao.");
        }

        order.setDeliveryConfirmed(true);
        order.setDeliveryConfirmedAt(LocalDateTime.now());
        order.setDeliveryStatus(safeStatus);
        order.setStatus("COMPLETED");
        order.setSellerViewed(false);

        // Update seller trust stats
        Team sellerTeam = order.getSellerTeam();
        if ("ON_TIME".equals(safeStatus)) {
            sellerTeam.setOnTimeOrders(sellerTeam.getOnTimeOrders() + 1);
        } else if ("LATE".equals(safeStatus)) {
            sellerTeam.setLateOrders(sellerTeam.getLateOrders() + 1);
        }
        sellerTeam.setTotalRatings(sellerTeam.getTotalRatings() + 1);
        sellerTeam.setSumRatings(sellerTeam.getSumRatings() + safeRating);
        sellerTeam.setCompletedOrders(sellerTeam.getCompletedOrders() + 1);
        sellerTeam.setTotalOrders(sellerTeam.getTotalOrders() + 1);
        teamRepo.save(sellerTeam);

        Team buyer = order.getBuyerTeam();
        if (buyer != null) {
            buyer.setCompletedOrders(buyer.getCompletedOrders() + 1);
            teamRepo.save(buyer);
        }

        org.example.backend.entity.Review review = new org.example.backend.entity.Review();
        review.setOrder(order);
        review.setBuyerTeam(order.getBuyerTeam());
        review.setBuyerUser(order.getBuyerUser());
        review.setSellerTeam(sellerTeam);
        review.setRating(safeRating);
        review.setComment(comment);
        review.setDeliveryResult(safeStatus);
        reviewRepo.save(review);


```
