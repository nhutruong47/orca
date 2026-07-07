# Knowledge Document: ProductionOrderService.java (Chunk 5/5)

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
  "chunk_index": 4,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
xpectedLoss(o.getExpectedLoss());
        dto.setInputRequired(o.getInputRequired());
        dto.setUnit(o.getUnit());
        dto.setOrderDate(o.getOrderDate());
        dto.setConfirmDate(o.getConfirmDate());
        dto.setProductionStartDate(o.getProductionStartDate());
        dto.setInternalDeadline(o.getInternalDeadline());
        dto.setCustomerDeliveryDate(o.getCustomerDeliveryDate());
        dto.setSafetyBufferDays(o.getSafetyBufferDays());
        dto.setRecipientName(o.getRecipientName());
        dto.setRecipientPhone(o.getRecipientPhone());
        dto.setShippingNote(o.getShippingNote());
        
        dto.setContactPhoneAlt(o.getContactPhoneAlt());
        dto.setDeliveryAddress(o.getDeliveryAddress());
        dto.setPreferredDeliveryFrom(o.getPreferredDeliveryFrom());
        dto.setPreferredDeliveryTo(o.getPreferredDeliveryTo());
        dto.setDeliveryFailureAction(o.getDeliveryFailureAction());
        dto.setDeliveryNote(o.getDeliveryNote());
        dto.setCancelRequested(o.getCancelRequested());
        dto.setBuyerViewed(o.getBuyerViewed());
        dto.setSellerViewed(o.getSellerViewed());

        dto.setStatus(o.getStatus());
        dto.setCompletedQuantity(o.getCompletedQuantity());
        dto.setProgressPercent(o.getProgressPercent());
        dto.setRemainingQuantity(o.getRemainingQuantity());
        dto.setCreatedAt(o.getCreatedAt());
        dto.setUpdatedAt(o.getUpdatedAt());
        return dto;
    }
}

```
