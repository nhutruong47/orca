# Knowledge Document: InterGroupOrder.java (Chunk 5/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/InterGroupOrder.java",
  "language": "java",
  "module": "entity",
  "business_domain": "factory",
  "tags": [
    "factory",
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 4,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, production

## Source Code Chunk
```java
c void setBuyerViewed(Boolean buyerViewed) { this.buyerViewed = buyerViewed; }

    public Boolean getSellerViewed() { return sellerViewed; }
    public void setSellerViewed(Boolean sellerViewed) { this.sellerViewed = sellerViewed; }

    public String getDeliveryStatus() { return deliveryStatus; }
    public void setDeliveryStatus(String deliveryStatus) { this.deliveryStatus = deliveryStatus; }

    public LocalDateTime getDeliveryConfirmedAt() { return deliveryConfirmedAt; }
    public void setDeliveryConfirmedAt(LocalDateTime deliveryConfirmedAt) { this.deliveryConfirmedAt = deliveryConfirmedAt; }

    public Boolean getDeliveryConfirmed() { return deliveryConfirmed; }
    public void setDeliveryConfirmed(Boolean deliveryConfirmed) { this.deliveryConfirmed = deliveryConfirmed; }
}

```
