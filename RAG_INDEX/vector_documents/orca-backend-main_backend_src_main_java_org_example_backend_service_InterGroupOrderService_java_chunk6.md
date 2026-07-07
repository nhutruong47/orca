# Knowledge Document: InterGroupOrderService.java (Chunk 7/18)

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
  "chunk_index": 6,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
order.getDeliveryConfirmed());
        dto.setDeliveryStatus(order.getDeliveryStatus());
        dto.setDeliveryConfirmedAt(order.getDeliveryConfirmedAt());

        // Marketplace RFQ fields
        dto.setMaterialSource(order.getMaterialSource());
        dto.setServices(order.getServices());
        dto.setProductType(order.getProductType());
        dto.setQuotedPrice(order.getQuotedPrice());
        dto.setQuotedNote(order.getQuotedNote());
        dto.setQuotedAt(order.getQuotedAt());
        dto.setUnit(order.getUnit());

        // Buyer trust score — updated to include delivery performance
        Team buyer = order.getBuyerTeam();
        int trustScore = 100;
        if (buyer != null && buyer.getTotalOrders() > 0) {
            int completed = buyer.getCompletedOrders();
            int cancelled = buyer.getCancelledOrders();
            trustScore = (int) ((double) completed / (completed + cancelled) * 100);
        }
        dto.setBuyerTrustScore(trustScore);

        return dto;
    }

    /**
     * Khách hàng hoặc xưởng hủy đơn. Nếu người mua hủy đơn sau 24h, đơn sẽ chuyển sang trạng thái "Đang xin hủy".
     */
    @Transactional
    public InterGroupOrderDTO cancelOrder(UUID orderId, User currentUser) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));

        if (!"RFQ_CREATED".equals(order.getStatus()) && !"QUOTED".equals(order.getStatus()) && !"CONFIRMED".equals(order.getStatus()) && !"PENDING".equals(order.getStatus()) && !"ACCEPTED".equals(order.getStatus())) {
            throw new RuntimeException("Chỉ đơn chưa sản xuất mới được hủy.");
        }

        boolean isBuyerOwner = (order.getBuyerTeam() != null && order.getBuyerTeam().getOwner().getId().equals(currentUser.getId()))
                || (order.getBuyerUser() != null && order.getBuyerUser().getId().equals(currentUser.getId()));
        boolean isSellerOwner = order.getSellerTeam().getOwner().getId().equals(currentUser.getId());

        if (!isBuyerOwner && !isSellerOwner) {
            throw new RuntimeException("Chỉ chủ xưởng mua hoặc bán mới được hủy đơn.");
        }

        // Logic 24h: Nếu người mua hủy và đơn đã quá 24h -> Chuyển thành Yêu cầu hủy
        if (isBuyerOwner && !isSellerOwner) {

```
