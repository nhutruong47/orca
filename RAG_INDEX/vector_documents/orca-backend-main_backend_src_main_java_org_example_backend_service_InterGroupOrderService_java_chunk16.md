# Knowledge Document: InterGroupOrderService.java (Chunk 17/18)

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
  "chunk_index": 16,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
r.getStatus()) && !"PENDING".equals(order.getStatus())) {
            throw new RuntimeException("Đơn hàng không ở trạng thái chờ báo giá.");
        }
        order.setQuotedPrice(price);
        order.setQuotedNote(note);
        order.setQuotedAt(LocalDateTime.now());
        order.setStatus("QUOTED");
        order.setBuyerViewed(false);
        InterGroupOrder saved = orderRepo.save(order);

        User buyerToNotify = resolveBuyerUser(order);
        if (buyerToNotify != null) {
            notifyUser(buyerToNotify, "Đã nhận báo giá",
                    "Xưởng " + order.getSellerTeam().getName() + " đã báo giá cho đơn \"" + order.getTitle() + "\".",
                    "ORDER_QUOTED", null);
        }
        return toDTO(saved);
    }

    /**
     * Update order status along the new marketplace flow.
     * Valid transitions: CONFIRMED -> IN_PRODUCTION -> QC -> COMPLETED -> SHIPPING -> DELIVERED
     */
    @Transactional
    public InterGroupOrderDTO updateOrderStatus(UUID orderId, String newStatus, User currentUser) {
        InterGroupOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Order not found"));

        if (!order.getSellerTeam().getOwner().getId().equals(currentUser.getId())) {
            throw new RuntimeException("Chỉ chủ xưởng mới được cập nhật trạng thái.");
        }

        order.setStatus(newStatus);
        order.setBuyerViewed(false);

        // Auto deduct inventory when DELIVERED + factory-provided materials
        if ("DELIVERED".equals(newStatus)) {
            order.setDeliveryConfirmed(false);
            String matSource = order.getMaterialSource();
            if (matSource == null || "FACTORY_PROVIDED".equals(matSource) || "COMBINED".equals(matSource)) {
                String productType = order.getProductType();
                if (productType != null && !productType.isBlank() && order.getQuantity() != null) {
                    try {
                        inventoryService.deductPackagedStock(
                                order.getSellerTeam().getId(), productType, order.getQuantity());
                    } catch (Exception e) {
                        System.err.println("Auto inventory deduction failed: " + e.getMessage());
                    }
                }
            }
        }

        InterGroupOrder saved = orderRepo.save(order);


```
