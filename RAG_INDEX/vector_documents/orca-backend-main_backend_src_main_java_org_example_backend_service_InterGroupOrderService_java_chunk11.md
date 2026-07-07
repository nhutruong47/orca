# Knowledge Document: InterGroupOrderService.java (Chunk 12/18)

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
  "chunk_index": 11,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
ang DELIVERED từ trạng thái: " + currentStatus);
        }

        Team sellerTeam = order.getSellerTeam();
        if (!sellerTeam.getOwner().getId().equals(currentUser.getId())) {
            throw new RuntimeException("Chỉ chủ xưởng bán mới được đánh dấu đã giao.");
        }

        order.setStatus("DELIVERED");
        order.setDeliveryConfirmed(false);
        order.setBuyerViewed(false);
        if (deliveryNote != null && !deliveryNote.isBlank()) {
            order.setDeliveryNote(deliveryNote);
        }

        InterGroupOrder saved = orderRepo.save(order);

        User buyerToNotify = resolveBuyerUser(order);
        if (buyerToNotify != null) {
            notifyUser(buyerToNotify,
                    "Đơn hàng đã được giao",
                    "Đơn hàng \"" + order.getTitle() + "\" đã được " + sellerTeam.getName() + " giao. Vui lòng xác nhận đã nhận hàng.",
                    "ORDER_DELIVERED", null);
        }

        return toDTO(saved);
    }

    /**
     * Lifecycle step: Buyer confirms receipt.
     * Allowed transitions: DELIVERED -> COMPLETED.
     * Only the buyer (team owner or personal buyer) can call this.
     */
    @Transactional
    public InterGroupOrderDTO confirmDelivery(UUID orderId, String deliveryStatus, Integer rating, String comment, User currentUser) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));

        String currentStatus = order.getStatus();
        if (!"DELIVERED".equals(currentStatus) && !"SHIPPING".equals(currentStatus)) {
            throw new RuntimeException("Đơn hàng chưa ở trạng thái DELIVERED để xác nhận. Hiện tại: " + currentStatus);
        }

        boolean isBuyer = (order.getBuyerTeam() != null && order.getBuyerTeam().getOwner().getId().equals(currentUser.getId()))
                || (order.getBuyerUser() != null && order.getBuyerUser().getId().equals(currentUser.getId()));
        if (!isBuyer) {
            throw new RuntimeException("Chỉ bên mua mới xác nhận được giao hàng.");
        }

        if (order.getDeliveryConfirmed() != null && order.getDeliveryConfirmed()) {
            throw new RuntimeException("Đơn này đã được xác nhận trước đó.");
        }

        String safeStatus = "ON_TIME";
        if (deliveryStatus != null) {

```
