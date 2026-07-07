# Knowledge Document: InterGroupOrderDTO.java (Chunk 4/4)

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
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: factory

## Source Code Chunk
```java
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

    public void setSellerViewed(Boolean sellerViewed) {
        this.sellerViewed = sellerViewed;
    }

    public Boolean getDeliveryConfirmed() {
        return deliveryConfirmed;
    }

    public void setDeliveryConfirmed(Boolean deliveryConfirmed) {
        this.deliveryConfirmed = deliveryConfirmed;
    }

    public String getDeliveryStatus() {
        return deliveryStatus;
    }

    public void setDeliveryStatus(String deliveryStatus) {
        this.deliveryStatus = deliveryStatus;
    }

    public LocalDateTime getDeliveryConfirmedAt() {
        return deliveryConfirmedAt;
    }

    public void setDeliveryConfirmedAt(LocalDateTime deliveryConfirmedAt) {
        this.deliveryConfirmedAt = deliveryConfirmedAt;
    }

    // === Marketplace RFQ Getters & Setters ===

    public String getMaterialSource() { return materialSource; }
    public void setMaterialSource(String materialSource) { this.materialSource = materialSource; }

    public String getServices() { return services; }
    public void setServices(String services) { this.services = services; }

    public String getProductType() { return productType; }
    public void setProductType(String productType) { this.productType = productType; }

    public Double getQuotedPrice() { return quotedPrice; }
    public void setQuotedPrice(Double quotedPrice) { this.quotedPrice = quotedPrice; }

    public String getQuotedNote() { return quotedNote; }
    public void setQuotedNote(String quotedNote) { this.quotedNote = quotedNote; }

    public LocalDateTime getQuotedAt() { return quotedAt; }
    public void setQuotedAt(LocalDateTime quotedAt) { this.quotedAt = quotedAt; }

    public String getUnit() { return unit; }
    public void setUnit(String unit) { this.unit = unit; }
}

```
