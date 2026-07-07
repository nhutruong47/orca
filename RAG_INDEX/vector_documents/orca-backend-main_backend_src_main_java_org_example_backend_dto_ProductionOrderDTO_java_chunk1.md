# Knowledge Document: ProductionOrderDTO.java (Chunk 2/4)

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
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
ic String getTitle() { return title; }
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

```
