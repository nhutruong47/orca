# Knowledge Document: ProductionOrder.java (Chunk 4/6)

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
  "chunk_index": 3,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
ageSize = packageSize; }
    public Integer getTotalPackages() { return totalPackages; }
    public void setTotalPackages(Integer totalPackages) { this.totalPackages = totalPackages; }
    public Double getOutputTarget() { return outputTarget; }
    public void setOutputTarget(Double outputTarget) { this.outputTarget = outputTarget; }
    public Double getExpectedYield() { return expectedYield; }
    public void setExpectedYield(Double expectedYield) { this.expectedYield = expectedYield; }
    public Double getExpectedLoss() { return expectedLoss; }
    public void setExpectedLoss(Double expectedLoss) { this.expectedLoss = expectedLoss; }
    public Double getInputRequired() { return inputRequired; }
    public void setInputRequired(Double inputRequired) { this.inputRequired = inputRequired; }
    public String getUnit() { return unit; }
    public void setUnit(String unit) { this.unit = unit; }
    public LocalDate getOrderDate() { return orderDate; }
    public void setOrderDate(LocalDate orderDate) { this.orderDate = orderDate; }
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

```
