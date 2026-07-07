# Knowledge Document: InterGroupOrderService.java (Chunk 15/18)

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
  "chunk_index": 14,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
ME".equals(deliveryStatus) && !"LATE".equals(deliveryStatus) && !"NOT_DELIVERED".equals(deliveryStatus)) {
            throw new RuntimeException("Trạng thái giao hàng không hợp lệ.");
        }

        if (rating < 1 || rating > 5) {
            throw new RuntimeException("Đánh giá phải từ 1 đến 5 sao.");
        }

        // Update order delivery info
        order.setDeliveryConfirmed(true);
        order.setDeliveryConfirmedAt(LocalDateTime.now());
        order.setDeliveryStatus(deliveryStatus);
        order.setStatus("COMPLETED");

        // Update seller trust stats
        Team sellerTeam = order.getSellerTeam();
        if ("ON_TIME".equals(deliveryStatus)) {
            sellerTeam.setOnTimeOrders(sellerTeam.getOnTimeOrders() + 1);
        } else if ("LATE".equals(deliveryStatus)) {
            sellerTeam.setLateOrders(sellerTeam.getLateOrders() + 1);
        }
        sellerTeam.setTotalRatings(sellerTeam.getTotalRatings() + 1);
        sellerTeam.setSumRatings(sellerTeam.getSumRatings() + rating);
        sellerTeam.setCompletedOrders(sellerTeam.getCompletedOrders() + 1);
        sellerTeam.setTotalOrders(sellerTeam.getTotalOrders() + 1);
        teamRepo.save(sellerTeam);

        // Update buyer team completed orders
        Team buyer = order.getBuyerTeam();
        if (buyer != null) {
            buyer.setCompletedOrders(buyer.getCompletedOrders() + 1);
            teamRepo.save(buyer);
        }

        // Save review
        org.example.backend.entity.Review review = new org.example.backend.entity.Review();
        review.setOrder(order);
        review.setBuyerTeam(order.getBuyerTeam());
        review.setBuyerUser(order.getBuyerUser());
        review.setSellerTeam(sellerTeam);
        review.setRating(rating);
        review.setComment(comment);
        review.setDeliveryResult(deliveryStatus);
        reviewRepo.save(review);

        InterGroupOrder saved = orderRepo.save(order);

        // Notify seller
        notifyUser(sellerTeam.getOwner(),
                "Người mua xác nhận giao hàng",
                "Đơn \"" + order.getTitle() + "\" đã được xác nhận: " + deliveryStatus + " | " + rating + " sao.",
                "ORDER_COMPLETED", null);

        return toDTO(saved);
    }

    @Transactional
    public void markOrdersAsViewed(List<UUID> orderIds, String role) {

```
