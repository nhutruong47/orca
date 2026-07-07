# Knowledge Document: ProductionOrder.java (Chunk 5/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/ProductionOrder.java",
  "language": "java",
  "module": "entity",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 4,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
etyBufferDays; }
    public String getRecipientName() { return recipientName; }
    public void setRecipientName(String recipientName) { this.recipientName = recipientName; }
    public String getRecipientPhone() { return recipientPhone; }
    public void setRecipientPhone(String recipientPhone) { this.recipientPhone = recipientPhone; }
    public String getShippingNote() { return shippingNote; }
    public void setShippingNote(String shippingNote) { this.shippingNote = shippingNote; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public Double getCompletedQuantity() { return completedQuantity; }
    public void setCompletedQuantity(Double completedQuantity) { this.completedQuantity = completedQuantity; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }

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

```
