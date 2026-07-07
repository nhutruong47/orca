# Knowledge Document: ProductionOrderService.java (Chunk 3/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ProductionOrderService.java",
  "language": "java",
  "module": "service",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Service",
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
   order.setPackageSize(raw.getPackageSize());
        order.setTotalPackages(raw.getTotalPackages());
        order.setOutputTarget(raw.getOutputTarget());
        order.setExpectedYield(raw.getExpectedYield());
        order.setExpectedLoss(raw.getExpectedLoss());
        order.setUnit(raw.getUnit());
        order.setOrderDate(raw.getOrderDate() != null ? raw.getOrderDate() : LocalDate.now());
        order.setConfirmDate(raw.getConfirmDate());
        order.setProductionStartDate(raw.getProductionStartDate());
        order.setCustomerDeliveryDate(raw.getCustomerDeliveryDate());
        order.setSafetyBufferDays(raw.getSafetyBufferDays() != null ? raw.getSafetyBufferDays() : 2);
        order.setRecipientName(raw.getRecipientName());
        order.setRecipientPhone(raw.getRecipientPhone());
        order.setShippingNote(raw.getShippingNote());
        
        order.setContactPhoneAlt(raw.getContactPhoneAlt());
        order.setDeliveryAddress(raw.getDeliveryAddress());
        order.setPreferredDeliveryFrom(raw.getPreferredDeliveryFrom());
        order.setPreferredDeliveryTo(raw.getPreferredDeliveryTo());
        order.setDeliveryFailureAction(raw.getDeliveryFailureAction());
        order.setDeliveryNote(raw.getDeliveryNote());
        if (raw.getCancelRequested() != null) order.setCancelRequested(raw.getCancelRequested());
        if (raw.getBuyerViewed() != null) order.setBuyerViewed(raw.getBuyerViewed());
        if (raw.getSellerViewed() != null) order.setSellerViewed(raw.getSellerViewed());
    }

    private void validateOrder(ProductionOrder order) {
        if (order.getTitle() == null || order.getTitle().isBlank()) {
            throw new RuntimeException("Tieu de don hang khong duoc de trong");
        }
        if (order.getOutputTarget() == null || order.getOutputTarget() <= 0) {
            throw new RuntimeException("San luong muc tieu phai lon hon 0");
        }
        if (order.getCustomerDeliveryDate() != null && order.getProductionStartDate() != null
                && !order.getCustomerDeliveryDate().isAfter(order.getProductionStartDate())) {
            throw new RuntimeException("Ngay giao hang phai sau ngay bat dau san xuat");
        }
    }

    public List<ProductionOrder> getOrdersByTeam(UUID teamId) {
        return orderRepo.findByTeamIdOrderByCreatedAtDesc(teamId);
    }


```
