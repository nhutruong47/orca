# Knowledge Document: InterGroupOrderService.java (Chunk 9/18)

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
  "chunk_index": 8,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
       if (isBuyerOwner) {
            notifyUser(order.getSellerTeam().getOwner(),
                    "Đơn hàng đã bị hủy",
                    "Đơn hàng \"" + order.getTitle() + "\" đã bị hủy bởi " + cancellerName + " (chưa quá 24h).",
                    "ORDER_CANCELED", null);
        } else {
            User buyerToNotify = resolveBuyerUser(order);
            if (buyerToNotify != null) {
                notifyUser(buyerToNotify,
                        "Đơn hàng đã bị hủy",
                        "Đơn hàng \"" + order.getTitle() + "\" đã bị hủy bởi " + cancellerName + ".",
                        "ORDER_CANCELED", null);
            }
        }

        return toDTO(saved);
    }

    /**
     * Seller đồng ý yêu cầu hủy của Buyer
     */
    @Transactional
    public InterGroupOrderDTO approveCancelOrder(UUID orderId, User currentUser) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));

        if (!order.getSellerTeam().getOwner().getId().equals(currentUser.getId())) {
            throw new RuntimeException("Chỉ chủ xưởng bán mới có quyền duyệt hủy đơn.");
        }
        if (order.getCancelRequested() == null || !order.getCancelRequested()) {
            throw new RuntimeException("Đơn hàng không có yêu cầu hủy.");
        }

        order.setStatus("CANCELED");
        order.setCancelledBy("BUYER");
        order.setCancelRequested(false);
        order.setBuyerViewed(false);

        // Penalty cho buyer
        if (order.getBuyerTeam() != null) {
            Team buyer = order.getBuyerTeam();
            buyer.setCancelledOrders(buyer.getCancelledOrders() + 1);
            teamRepo.save(buyer);
        }

        InterGroupOrder saved = orderRepo.save(order);

        User buyerToNotify = resolveBuyerUser(order);
        if (buyerToNotify != null) {
            notifyUser(buyerToNotify,
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

```
