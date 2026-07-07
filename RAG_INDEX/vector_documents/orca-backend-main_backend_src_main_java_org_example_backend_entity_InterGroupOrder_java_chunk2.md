# Knowledge Document: InterGroupOrder.java (Chunk 3/5)

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
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, production

## Source Code Chunk
```java

    public Team getBuyerTeam() { return buyerTeam; }
    public void setBuyerTeam(Team buyerTeam) { this.buyerTeam = buyerTeam; }

    public User getBuyerUser() { return buyerUser; }
    public void setBuyerUser(User buyerUser) { this.buyerUser = buyerUser; }

    public Team getSellerTeam() { return sellerTeam; }
    public void setSellerTeam(Team sellerTeam) { this.sellerTeam = sellerTeam; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public Integer getQuantity() { return quantity; }
    public void setQuantity(Integer quantity) { this.quantity = quantity; }

    public LocalDateTime getDeadline() { return deadline; }
    public void setDeadline(LocalDateTime deadline) { this.deadline = deadline; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }

    public UUID getLinkedGoalId() { return linkedGoalId; }
    public void setLinkedGoalId(UUID linkedGoalId) { this.linkedGoalId = linkedGoalId; }

    public LocalDateTime getCreatedAt() { return createdAt; }

    public String getCancelledBy() { return cancelledBy; }
    public void setCancelledBy(String cancelledBy) { this.cancelledBy = cancelledBy; }

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


```
