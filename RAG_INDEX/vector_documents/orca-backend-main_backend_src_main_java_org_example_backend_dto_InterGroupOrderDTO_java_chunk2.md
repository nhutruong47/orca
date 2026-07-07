# Knowledge Document: InterGroupOrderDTO.java (Chunk 3/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/InterGroupOrderDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "factory",
  "tags": [
    "factory"
  ],
  "logical_type": "DTO",
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: factory

## Source Code Chunk
```java
   this.createdAt = createdAt;
    }

    public int getBuyerTrustScore() {
        return buyerTrustScore;
    }

    public void setBuyerTrustScore(int buyerTrustScore) {
        this.buyerTrustScore = buyerTrustScore;
    }

    public String getCancelledBy() {
        return cancelledBy;
    }

    public void setCancelledBy(String cancelledBy) {
        this.cancelledBy = cancelledBy;
    }

    // === Delivery Profile Getters & Setters ===

    public String getContactPhone() {
        return contactPhone;
    }

    public void setContactPhone(String contactPhone) {
        this.contactPhone = contactPhone;
    }

    public String getContactPhoneAlt() {
        return contactPhoneAlt;
    }

    public void setContactPhoneAlt(String contactPhoneAlt) {
        this.contactPhoneAlt = contactPhoneAlt;
    }

    public String getDeliveryAddress() {
        return deliveryAddress;
    }

    public void setDeliveryAddress(String deliveryAddress) {
        this.deliveryAddress = deliveryAddress;
    }

    public LocalDateTime getPreferredDeliveryFrom() {
        return preferredDeliveryFrom;
    }

    public void setPreferredDeliveryFrom(LocalDateTime preferredDeliveryFrom) {
        this.preferredDeliveryFrom = preferredDeliveryFrom;
    }

    public LocalDateTime getPreferredDeliveryTo() {
        return preferredDeliveryTo;
    }

    public void setPreferredDeliveryTo(LocalDateTime preferredDeliveryTo) {
        this.preferredDeliveryTo = preferredDeliveryTo;
    }

    public String getDeliveryFailureAction() {
        return deliveryFailureAction;
    }

    public void setDeliveryFailureAction(String deliveryFailureAction) {
        this.deliveryFailureAction = deliveryFailureAction;
    }

    public String getDeliveryNote() {
        return deliveryNote;
    }

    public void setDeliveryNote(String deliveryNote) {
        this.deliveryNote = deliveryNote;
    }

    public Boolean getCancelRequested() {
        return cancelRequested;
    }

    public void setCancelRequested(Boolean cancelRequested) {
        this.cancelRequested = cancelRequested;
    }

    public Boolean getBuyerViewed() {
        return buyerViewed;
    }

    public void setBuyerViewed(Boolean buyerViewed) {
        this.buyerViewed = buyerViewed;
    }

    public Boolean getSellerViewed() {
        return sellerViewed;
    }


```
