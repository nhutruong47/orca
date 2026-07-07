# Knowledge Document: InterGroupOrderService.java (Chunk 10/18)

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
  "chunk_index": 9,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
    "Yêu cầu hủy được chấp nhận",
                    "Xưởng " + order.getSellerTeam().getName() + " đã đồng ý hủy đơn \"" + order.getTitle() + "\".",
                    "ORDER_CANCELED", null);
        }

        return toDTO(saved);
    }

    /**
     * Seller từ chối yêu cầu hủy của Buyer (Chỉ hợp lệ nếu > 24h, mà code ở trên đã chặn việc tạo request nếu < 24h rồi)
     */
    @Transactional
    public InterGroupOrderDTO rejectCancelOrder(UUID orderId, User currentUser) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));

        if (!order.getSellerTeam().getOwner().getId().equals(currentUser.getId())) {
            throw new RuntimeException("Chỉ chủ xưởng bán mới có quyền từ chối hủy đơn.");
        }
        if (order.getCancelRequested() == null || !order.getCancelRequested()) {
            throw new RuntimeException("Đơn hàng không có yêu cầu hủy.");
        }

        // Tắt cờ yêu cầu hủy, đơn hàng trở lại bình thường
        order.setCancelRequested(false);
        order.setBuyerViewed(false);
        InterGroupOrder saved = orderRepo.save(order);

        User buyerToNotify = resolveBuyerUser(order);
        if (buyerToNotify != null) {
            notifyUser(buyerToNotify,
                    "Yêu cầu hủy bị từ chối",
                    "Xưởng " + order.getSellerTeam().getName() + " đã từ chối yêu cầu hủy đơn \"" + order.getTitle() + "\". Đơn hàng vẫn tiếp tục.",
                    "ORDER_CANCEL_REJECTED", null);
        }

        return toDTO(saved);
    }

    /**
     * Xưởng đánh dấu đã giao hàng — chuyển sang DELIVERED, chờ người mua xác nhận
     */
    @Transactional
    public InterGroupOrderDTO shipOrder(UUID orderId, User currentUser) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));

        if (!"COMPLETED".equals(order.getStatus()) && !"ACCEPTED".equals(order.getStatus()) && !"IN_PRODUCTION".equals(order.getStatus()) && !"QC".equals(order.getStatus())) {
            throw new RuntimeException("Đơn hàng chưa ở trạng thái có thể giao.");
        }

        Team sellerTeam = order.getSellerTeam();
        if (!sellerTeam.getOwner().getId().equals(currentUser.getId())) {
            throw new RuntimeException("Chỉ chủ xưởng bán mới được đánh dấu đã giao.");

```
