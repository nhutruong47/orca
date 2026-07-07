# Knowledge Document: InterGroupOrderService.java (Chunk 11/18)

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
  "chunk_index": 10,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
tStatus()) && !"IN_PRODUCTION".equals(order.getStatus()) && !"QC".equals(order.getStatus())) {
            throw new RuntimeException("Đơn hàng chưa ở trạng thái có thể giao.");
        }

        Team sellerTeam = order.getSellerTeam();
        if (!sellerTeam.getOwner().getId().equals(currentUser.getId())) {
            throw new RuntimeException("Chỉ chủ xưởng bán mới được đánh dấu đã giao.");
        }

        order.setStatus("SHIPPING");
        order.setBuyerViewed(false);

        InterGroupOrder saved = orderRepo.save(order);

        // Notify buyer that order has been delivered
        User buyerToNotify = resolveBuyerUser(order);
        if (buyerToNotify != null) {
            notifyUser(buyerToNotify,
                    "Đơn hàng đã giao — Chờ xác nhận",
                    "Đơn hàng \"" + order.getTitle() + "\" đã được " + sellerTeam.getName() + " giao. Vui lòng xác nhận đã nhận hàng đúng hẹn hay không.",
                    "ORDER_DELIVERED", null);
        }

        return toDTO(saved);
    }

    /**
     * Lifecycle step: Seller marks the order as DELIVERED.
     * Allowed transitions:
     *   CONFIRMED -> SHIPPING -> DELIVERED (idempotent skip if already SHIPPING/DELIVERED)
     * Only the seller (receiving team owner) can call this.
     */
    @Transactional
    public InterGroupOrderDTO deliverOrder(UUID orderId, String deliveryNote, User currentUser) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));

        String currentStatus = order.getStatus();
        boolean allowed = "CONFIRMED".equals(currentStatus)
                || "IN_PRODUCTION".equals(currentStatus)
                || "QC".equals(currentStatus)
                || "COMPLETED".equals(currentStatus)
                || "SHIPPING".equals(currentStatus);
        if (!allowed) {
            throw new RuntimeException("Đơn hàng không thể chuyển sang DELIVERED từ trạng thái: " + currentStatus);
        }

        Team sellerTeam = order.getSellerTeam();
        if (!sellerTeam.getOwner().getId().equals(currentUser.getId())) {
            throw new RuntimeException("Chỉ chủ xưởng bán mới được đánh dấu đã giao.");
        }

        order.setStatus("DELIVERED");
        order.setDeliveryConfirmed(false);
        order.setBuyerViewed(false);

```
