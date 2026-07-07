# Knowledge Document: InterGroupOrderService.java (Chunk 8/18)

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
  "chunk_index": 7,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
entUser.getId()));
        boolean isSellerOwner = order.getSellerTeam().getOwner().getId().equals(currentUser.getId());

        if (!isBuyerOwner && !isSellerOwner) {
            throw new RuntimeException("Chỉ chủ xưởng mua hoặc bán mới được hủy đơn.");
        }

        // Logic 24h: Nếu người mua hủy và đơn đã quá 24h -> Chuyển thành Yêu cầu hủy
        if (isBuyerOwner && !isSellerOwner) {
            long hoursSinceCreation = java.time.temporal.ChronoUnit.HOURS.between(order.getCreatedAt(), LocalDateTime.now());
            if (hoursSinceCreation > 24) {
                order.setCancelRequested(true);
                order.setSellerViewed(false);
                InterGroupOrder saved = orderRepo.save(order);
                notifyUser(order.getSellerTeam().getOwner(),
                        "Yêu cầu hủy đơn hàng",
                        "Khách hàng đã yêu cầu hủy đơn \"" + order.getTitle() + "\". Hãy xem xét.",
                        "ORDER_CANCEL_REQUESTED", null);
                return toDTO(saved);
            }
        }

        // Thực hiện hủy ngay
        order.setStatus("CANCELED");
        order.setCancelledBy(isBuyerOwner ? "BUYER" : "SELLER");
        order.setCancelRequested(false);
        if (isBuyerOwner) {
            order.setSellerViewed(false);
        } else {
            order.setBuyerViewed(false);
        }

        // Penalty
        if (isBuyerOwner && order.getBuyerTeam() != null) {
            Team buyer = order.getBuyerTeam();
            buyer.setCancelledOrders(buyer.getCancelledOrders() + 1);
            teamRepo.save(buyer);
        } else if (isSellerOwner) {
            Team seller = order.getSellerTeam();
            seller.setCancelledOrders(seller.getCancelledOrders() + 1);
            teamRepo.save(seller);
        }

        InterGroupOrder saved = orderRepo.save(order);

        // Thông báo cho bên còn lại
        String cancellerName = isBuyerOwner ? "Bên mua" : "Bên bán";
        if (isBuyerOwner) {
            notifyUser(order.getSellerTeam().getOwner(),
                    "Đơn hàng đã bị hủy",
                    "Đơn hàng \"" + order.getTitle() + "\" đã bị hủy bởi " + cancellerName + " (chưa quá 24h).",
                    "ORDER_CANCELED", null);
        } else {
            User buyerToNotify = resolveBuyerUser(order);
            if (buyerToNotify != null) {

```
