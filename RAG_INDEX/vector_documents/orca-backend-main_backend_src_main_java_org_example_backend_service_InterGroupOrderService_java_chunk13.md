# Knowledge Document: InterGroupOrderService.java (Chunk 14/18)

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
  "chunk_index": 13,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
ckend.entity.Review review = new org.example.backend.entity.Review();
        review.setOrder(order);
        review.setBuyerTeam(order.getBuyerTeam());
        review.setBuyerUser(order.getBuyerUser());
        review.setSellerTeam(sellerTeam);
        review.setRating(safeRating);
        review.setComment(comment);
        review.setDeliveryResult(safeStatus);
        reviewRepo.save(review);

        InterGroupOrder saved = orderRepo.save(order);

        notifyUser(sellerTeam.getOwner(),
                "Người mua xác nhận giao hàng",
                "Đơn \"" + order.getTitle() + "\" đã được xác nhận: " + safeStatus + " | " + safeRating + " sao.",
                "ORDER_COMPLETED", null);

        return toDTO(saved);
    }

    /**
     * Người mua xác nhận đã nhận hàng + đánh giá sao.
     * Trạng thái đơn: ON_TIME / LATE / NOT_DELIVERED
     * Trust score của xưởng được cập nhật theo đánh giá.
     */
    @Transactional
    public InterGroupOrderDTO buyerConfirmDelivery(UUID orderId, String deliveryStatus,
            int rating, String comment, User currentUser) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));

        if (!"DELIVERED".equals(order.getStatus()) && !"SHIPPING".equals(order.getStatus())) {
            throw new RuntimeException("Chỉ đơn DELIVERED hoặc SHIPPING mới xác nhận được.");
        }

        // Verify buyer
        boolean isBuyer = (order.getBuyerTeam() != null && order.getBuyerTeam().getOwner().getId().equals(currentUser.getId()))
                || (order.getBuyerUser() != null && order.getBuyerUser().getId().equals(currentUser.getId()));
        if (!isBuyer) {
            throw new RuntimeException("Chỉ bên mua mới xác nhận được.");
        }

        if (order.getDeliveryConfirmed() != null && order.getDeliveryConfirmed()) {
            throw new RuntimeException("Đơn này đã được xác nhận trước đó.");
        }

        if (!"ON_TIME".equals(deliveryStatus) && !"LATE".equals(deliveryStatus) && !"NOT_DELIVERED".equals(deliveryStatus)) {
            throw new RuntimeException("Trạng thái giao hàng không hợp lệ.");
        }

        if (rating < 1 || rating > 5) {
            throw new RuntimeException("Đánh giá phải từ 1 đến 5 sao.");
        }

        // Update order delivery info
        order.setDeliveryConfirmed(true);

```
