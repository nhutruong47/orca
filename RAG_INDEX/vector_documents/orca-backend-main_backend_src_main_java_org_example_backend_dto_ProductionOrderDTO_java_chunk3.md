# Knowledge Document: ProductionOrderDTO.java (Chunk 4/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ProductionOrderDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "DTO",
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
ic void setRemainingQuantity(Double remainingQuantity) { this.remainingQuantity = remainingQuantity; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }

    public String getContactPhoneAlt() { return contactPhoneAlt; }
    public void setContactPhoneAlt(String contactPhoneAlt) { this.contactPhoneAlt = contactPhoneAlt; }
    public String getDeliveryAddress() { return deliveryAddress; }
    public void setDeliveryAddress(String deliveryAddress) { this.deliveryAddress = deliveryAddress; }
    public LocalDateTime getPreferredDeliveryFrom() { return preferredDeliveryFrom; }
    public void setPreferredDeliveryFrom(LocalDateTime preferredDeliveryFrom) { this.preferredDeliveryFrom = preferredDeliveryFrom; }
    public LocalDateTime getPreferredDeliveryTo() { return preferredDeliveryTo; }
    public void setPreferredDeliveryTo(LocalDateTime preferredDeliveryTo) { this.preferredDeliveryTo = preferredDeliveryTo; }
    public String getDeliveryFailureAction() { return deliveryFailureAction; }
    public void setDeliveryFailureAction(String deliveryFailureAction) { this.deliveryFailureAction = deliveryFailureAction; }
    public String getDeliveryNote() { return deliveryNote; }
    public void setDeliveryNote(String deliveryNote) { this.deliveryNote = deliveryNote; }
    public Boolean getCancelRequested() { return cancelRequested; }
    public void setCancelRequested(Boolean cancelRequested) { this.cancelRequested = cancelRequested; }
    public Boolean getBuyerViewed() { return buyerViewed; }
    public void setBuyerViewed(Boolean buyerViewed) { this.buyerViewed = buyerViewed; }
    public Boolean getSellerViewed() { return sellerViewed; }
    public void setSellerViewed(Boolean sellerViewed) { this.sellerViewed = sellerViewed; }
}

```
