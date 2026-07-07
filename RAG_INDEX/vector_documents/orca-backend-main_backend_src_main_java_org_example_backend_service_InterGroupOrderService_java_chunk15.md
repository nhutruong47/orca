# Knowledge Document: InterGroupOrderService.java (Chunk 16/18)

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
  "chunk_index": 15,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java

        // Notify seller
        notifyUser(sellerTeam.getOwner(),
                "Người mua xác nhận giao hàng",
                "Đơn \"" + order.getTitle() + "\" đã được xác nhận: " + deliveryStatus + " | " + rating + " sao.",
                "ORDER_COMPLETED", null);

        return toDTO(saved);
    }

    @Transactional
    public void markOrdersAsViewed(List<UUID> orderIds, String role) {
        if (orderIds == null || orderIds.isEmpty()) return;
        List<InterGroupOrder> orders = orderRepo.findAllById(orderIds);
        for (InterGroupOrder order : orders) {
            if ("BUYER".equalsIgnoreCase(role)) {
                order.setBuyerViewed(true);
            } else if ("SELLER".equalsIgnoreCase(role)) {
                order.setSellerViewed(true);
            }
        }
        orderRepo.saveAll(orders);
    }

    // === Helper methods ===

    /** Map delivery fields from DTO to entity */
    private void mapDeliveryFields(InterGroupOrder order, InterGroupOrderDTO dto) {
        order.setContactPhone(dto.getContactPhone());
        order.setContactPhoneAlt(dto.getContactPhoneAlt());
        order.setDeliveryAddress(dto.getDeliveryAddress());
        order.setPreferredDeliveryFrom(dto.getPreferredDeliveryFrom());
        order.setPreferredDeliveryTo(dto.getPreferredDeliveryTo());
        order.setDeliveryFailureAction(dto.getDeliveryFailureAction());
        order.setDeliveryNote(dto.getDeliveryNote());
    }

    /**
     * Xưởng gửi báo giá cho RFQ.
     */
    @Transactional
    public InterGroupOrderDTO quoteOrder(UUID orderId, Double price, String note, User currentUser) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));
        if (!order.getSellerTeam().getOwner().getId().equals(currentUser.getId())) {
            throw new RuntimeException("Chỉ chủ xưởng mới được báo giá.");
        }
        if (!"RFQ_CREATED".equals(order.getStatus()) && !"PENDING".equals(order.getStatus())) {
            throw new RuntimeException("Đơn hàng không ở trạng thái chờ báo giá.");
        }
        order.setQuotedPrice(price);
        order.setQuotedNote(note);
        order.setQuotedAt(LocalDateTime.now());
        order.setStatus("QUOTED");
        order.setBuyerViewed(false);
        InterGroupOrder saved = orderRepo.save(order);


```
