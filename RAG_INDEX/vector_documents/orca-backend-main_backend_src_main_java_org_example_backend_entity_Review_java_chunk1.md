# Knowledge Document: Review.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/Review.java",
  "language": "java",
  "module": "entity",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
ting != null) {
            this.rating = this.overallRating;
        }
    }

    public Review() {}

    // Getters & Setters

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }

    public InterGroupOrder getOrder() { return order; }
    public void setOrder(InterGroupOrder order) { this.order = order; }

    public Team getBuyerTeam() { return buyerTeam; }
    public void setBuyerTeam(Team buyerTeam) { this.buyerTeam = buyerTeam; }

    public User getBuyerUser() { return buyerUser; }
    public void setBuyerUser(User buyerUser) { this.buyerUser = buyerUser; }

    public Team getSellerTeam() { return sellerTeam; }
    public void setSellerTeam(Team sellerTeam) { this.sellerTeam = sellerTeam; }

    public int getRating() { return rating; }
    public void setRating(int rating) { this.rating = rating; }

    public Integer getProductQuality() { return productQuality; }
    public void setProductQuality(Integer productQuality) { this.productQuality = productQuality; }

    public Integer getDeliverySchedule() { return deliverySchedule; }
    public void setDeliverySchedule(Integer deliverySchedule) { this.deliverySchedule = deliverySchedule; }

    public Integer getCustomerSupport() { return customerSupport; }
    public void setCustomerSupport(Integer customerSupport) { this.customerSupport = customerSupport; }

    public Integer getOverallRating() { return overallRating; }
    public void setOverallRating(Integer overallRating) { this.overallRating = overallRating; }

    public String getComment() { return comment; }
    public void setComment(String comment) { this.comment = comment; }

    public String getImages() { return images; }
    public void setImages(String images) { this.images = images; }

    public String getDeliveryResult() { return deliveryResult; }
    public void setDeliveryResult(String deliveryResult) { this.deliveryResult = deliveryResult; }

    public LocalDateTime getCreatedAt() { return createdAt; }
}

```
