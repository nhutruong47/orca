# Knowledge Document: InterGroupOrderService.java (Chunk 6/18)

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
  "chunk_index": 5,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
OrderDTO dto = new InterGroupOrderDTO();
        dto.setId(order.getId().toString());
        dto.setBuyerTeamId(order.getBuyerTeam() != null ? order.getBuyerTeam().getId().toString() : null);
        dto.setBuyerTeamName(order.getBuyerTeam() != null ? order.getBuyerTeam().getName() : null);
        dto.setBuyerUserId(order.getBuyerUser() != null ? order.getBuyerUser().getId().toString() : null);
        dto.setBuyerUserName(order.getBuyerUser() != null
                ? (order.getBuyerUser().getFullName() != null && !order.getBuyerUser().getFullName().isBlank()
                        ? order.getBuyerUser().getFullName()
                        : order.getBuyerUser().getUsername())
                : null);
        dto.setSellerTeamId(order.getSellerTeam().getId().toString());
        dto.setSellerTeamName(order.getSellerTeam().getName());
        dto.setTitle(order.getTitle());
        dto.setDescription(order.getDescription());
        dto.setQuantity(order.getQuantity());
        dto.setDeadline(order.getDeadline());
        dto.setStatus(order.getStatus());
        dto.setLinkedGoalId(order.getLinkedGoalId() != null ? order.getLinkedGoalId().toString() : null);
        dto.setCreatedAt(order.getCreatedAt());
        dto.setCancelledBy(order.getCancelledBy());
        dto.setCancelRequested(order.getCancelRequested());
        dto.setBuyerViewed(order.getBuyerViewed());
        dto.setSellerViewed(order.getSellerViewed());

        // Delivery profile
        dto.setContactPhone(order.getContactPhone());
        dto.setContactPhoneAlt(order.getContactPhoneAlt());
        dto.setDeliveryAddress(order.getDeliveryAddress());
        dto.setPreferredDeliveryFrom(order.getPreferredDeliveryFrom());
        dto.setPreferredDeliveryTo(order.getPreferredDeliveryTo());
        dto.setDeliveryFailureAction(order.getDeliveryFailureAction());
        dto.setDeliveryNote(order.getDeliveryNote());

        // Delivery confirmation
        dto.setDeliveryConfirmed(order.getDeliveryConfirmed());
        dto.setDeliveryStatus(order.getDeliveryStatus());
        dto.setDeliveryConfirmedAt(order.getDeliveryConfirmedAt());

        // Marketplace RFQ fields
        dto.setMaterialSource(order.getMaterialSource());
        dto.setServices(order.getServices());
        dto.setProductType(order.getProductType());
        dto.setQuotedPrice(order.getQuotedPrice());

```
