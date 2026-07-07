# Knowledge Document: AnalyticsDTO.java (Chunk 4/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/AnalyticsDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "production"
  ],
  "logical_type": "DTO",
  "chunk_index": 3,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```java
public void setEfficiency(double efficiency) { this.efficiency = efficiency; }
        public double getAvgProductivity() { return avgProductivity; }
        public void setAvgProductivity(double avgProductivity) { this.avgProductivity = avgProductivity; }
        public double getFailRate() { return failRate; }
        public void setFailRate(double failRate) { this.failRate = failRate; }
    }

    public static class OrderAnalytics {
        private String orderId;
        private String orderCode;
        private String title;
        private double outputTarget;
        private double completedQuantity;
        private double progressPercent;
        private double expectedYield;
        private double actualYield;
        private double leadTimeDays;
        private String riskLevel;
        private String status;

        public String getOrderId() { return orderId; }
        public void setOrderId(String orderId) { this.orderId = orderId; }
        public String getOrderCode() { return orderCode; }
        public void setOrderCode(String orderCode) { this.orderCode = orderCode; }
        public String getTitle() { return title; }
        public void setTitle(String title) { this.title = title; }
        public double getOutputTarget() { return outputTarget; }
        public void setOutputTarget(double outputTarget) { this.outputTarget = outputTarget; }
        public double getCompletedQuantity() { return completedQuantity; }
        public void setCompletedQuantity(double completedQuantity) { this.completedQuantity = completedQuantity; }
        public double getProgressPercent() { return progressPercent; }
        public void setProgressPercent(double progressPercent) { this.progressPercent = progressPercent; }
        public double getExpectedYield() { return expectedYield; }
        public void setExpectedYield(double expectedYield) { this.expectedYield = expectedYield; }
        public double getActualYield() { return actualYield; }
        public void setActualYield(double actualYield) { this.actualYield = actualYield; }
        public double getLeadTimeDays() { return leadTimeDays; }
        public void setLeadTimeDays(double leadTimeDays) { this.leadTimeDays = leadTimeDays; }
        public String getRiskLevel() { return riskLevel; }
        public void setRiskLevel(String riskLevel) { this.riskLevel = riskLevel; }

```
