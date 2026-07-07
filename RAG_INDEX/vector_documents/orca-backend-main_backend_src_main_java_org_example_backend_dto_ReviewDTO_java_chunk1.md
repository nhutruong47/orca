# Knowledge Document: ReviewDTO.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ReviewDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "DTO",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
  public void setOverallRating(Integer overallRating) { this.overallRating = overallRating; }

    public String getComment() { return comment; }
    public void setComment(String comment) { this.comment = comment; }

    public String getImages() { return images; }
    public void setImages(String images) { this.images = images; }

    public String getDeliveryResult() { return deliveryResult; }
    public void setDeliveryResult(String deliveryResult) { this.deliveryResult = deliveryResult; }

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }

    public String getBuyerTeamName() { return buyerTeamName; }
    public void setBuyerTeamName(String buyerTeamName) { this.buyerTeamName = buyerTeamName; }

    public String getBuyerUserName() { return buyerUserName; }
    public void setBuyerUserName(String buyerUserName) { this.buyerUserName = buyerUserName; }
}

```
