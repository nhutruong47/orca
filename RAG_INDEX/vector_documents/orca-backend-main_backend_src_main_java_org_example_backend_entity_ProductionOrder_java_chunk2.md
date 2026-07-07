# Knowledge Document: ProductionOrder.java (Chunk 3/6)

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
  "chunk_index": 2,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
Update() {
        this.updatedAt = LocalDateTime.now();
        calculateInternalDeadline();
    }

    private void calculateInternalDeadline() {
        if (this.customerDeliveryDate != null && this.safetyBufferDays != null) {
            this.internalDeadline = this.customerDeliveryDate
                    .atStartOfDay()
                    .minusDays(this.safetyBufferDays);
        }
    }

    public void calculateInputRequired() {
        if (this.outputTarget != null && this.expectedYield != null && this.expectedYield > 0) {
            this.inputRequired = Math.ceil((this.outputTarget / this.expectedYield) * 100.0) / 100.0;
        }
    }

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }
    public Team getTeam() { return team; }
    public void setTeam(Team team) { this.team = team; }
    public String getOrderCode() { return orderCode; }
    public void setOrderCode(String orderCode) { this.orderCode = orderCode; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getCustomerName() { return customerName; }
    public void setCustomerName(String customerName) { this.customerName = customerName; }
    public String getProductType() { return productType; }
    public void setProductType(String productType) { this.productType = productType; }
    public String getProcessType() { return processType; }
    public void setProcessType(String processType) { this.processType = processType; }
    public String getRoastLevel() { return roastLevel; }
    public void setRoastLevel(String roastLevel) { this.roastLevel = roastLevel; }
    public String getPackageSize() { return packageSize; }
    public void setPackageSize(String packageSize) { this.packageSize = packageSize; }
    public Integer getTotalPackages() { return totalPackages; }
    public void setTotalPackages(Integer totalPackages) { this.totalPackages = totalPackages; }
    public Double getOutputTarget() { return outputTarget; }
    public void setOutputTarget(Double outputTarget) { this.outputTarget = outputTarget; }
    public Double getExpectedYield() { return expectedYield; }

```
