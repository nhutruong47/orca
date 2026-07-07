# Knowledge Document: ProductionOrderDTO.java (Chunk 3/4)

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
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
Date orderDate) { this.orderDate = orderDate; }
    public LocalDate getConfirmDate() { return confirmDate; }
    public void setConfirmDate(LocalDate confirmDate) { this.confirmDate = confirmDate; }
    public LocalDate getProductionStartDate() { return productionStartDate; }
    public void setProductionStartDate(LocalDate productionStartDate) { this.productionStartDate = productionStartDate; }
    public LocalDateTime getInternalDeadline() { return internalDeadline; }
    public void setInternalDeadline(LocalDateTime internalDeadline) { this.internalDeadline = internalDeadline; }
    public LocalDate getCustomerDeliveryDate() { return customerDeliveryDate; }
    public void setCustomerDeliveryDate(LocalDate customerDeliveryDate) { this.customerDeliveryDate = customerDeliveryDate; }
    public Integer getSafetyBufferDays() { return safetyBufferDays; }
    public void setSafetyBufferDays(Integer safetyBufferDays) { this.safetyBufferDays = safetyBufferDays; }
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
    public Double getProgressPercent() { return progressPercent; }
    public void setProgressPercent(Double progressPercent) { this.progressPercent = progressPercent; }
    public Double getRemainingQuantity() { return remainingQuantity; }
    public void setRemainingQuantity(Double remainingQuantity) { this.remainingQuantity = remainingQuantity; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }


```
