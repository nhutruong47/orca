# Knowledge Document: ProductionOrder.java (Chunk 6/6)

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
  "chunk_index": 5,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
void setDeliveryNote(String deliveryNote) { this.deliveryNote = deliveryNote; }
    public Boolean getCancelRequested() { return cancelRequested; }
    public void setCancelRequested(Boolean cancelRequested) { this.cancelRequested = cancelRequested; }
    public Boolean getBuyerViewed() { return buyerViewed; }
    public void setBuyerViewed(Boolean buyerViewed) { this.buyerViewed = buyerViewed; }
    public Boolean getSellerViewed() { return sellerViewed; }
    public void setSellerViewed(Boolean sellerViewed) { this.sellerViewed = sellerViewed; }

    public double getProgressPercent() {
        if (outputTarget == null || outputTarget == 0) return 0;
        double completed = completedQuantity != null ? completedQuantity : 0;
        return Math.min(100, Math.round((completed / outputTarget) * 1000.0) / 10.0);
    }

    public double getRemainingQuantity() {
        double completed = completedQuantity != null ? completedQuantity : 0;
        return Math.max(0, (outputTarget != null ? outputTarget : 0) - completed);
    }
}

```
