# Knowledge Document: DailyBoardDTO.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/DailyBoardDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "DTO",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
ble packagingTarget;
        private String riskLevel;
        private String stageStatus;
        private int daysToDeadline;

        public String getOrderId() { return orderId; }
        public void setOrderId(String orderId) { this.orderId = orderId; }
        public String getOrderCode() { return orderCode; }
        public void setOrderCode(String orderCode) { this.orderCode = orderCode; }
        public String getTitle() { return title; }
        public void setTitle(String title) { this.title = title; }
        public String getCustomerName() { return customerName; }
        public void setCustomerName(String customerName) { this.customerName = customerName; }
        public double getOutputTarget() { return outputTarget; }
        public void setOutputTarget(double outputTarget) { this.outputTarget = outputTarget; }
        public double getCompletedQuantity() { return completedQuantity; }
        public void setCompletedQuantity(double completedQuantity) { this.completedQuantity = completedQuantity; }
        public double getRemainingQuantity() { return remainingQuantity; }
        public void setRemainingQuantity(double remainingQuantity) { this.remainingQuantity = remainingQuantity; }
        public double getProgressPercent() { return progressPercent; }
        public void setProgressPercent(double progressPercent) { this.progressPercent = progressPercent; }
        public double getRoastActual() { return roastActual; }
        public void setRoastActual(double roastActual) { this.roastActual = roastActual; }
        public double getQcActual() { return qcActual; }
        public void setQcActual(double qcActual) { this.qcActual = qcActual; }
        public double getPackagingActual() { return packagingActual; }
        public void setPackagingActual(double packagingActual) { this.packagingActual = packagingActual; }
        public double getRoastTarget() { return roastTarget; }
        public void setRoastTarget(double roastTarget) { this.roastTarget = roastTarget; }
        public double getQcTarget() { return qcTarget; }
        public void setQcTarget(double qcTarget) { this.qcTarget = qcTarget; }
        public double getPackagingTarget() { return packagingTarget; }
        public void setPackagingTarget(double packagingTarget) { this.packagingTarget = packagingTarget; }
        public String getRiskLevel() { return riskLevel; }

```
