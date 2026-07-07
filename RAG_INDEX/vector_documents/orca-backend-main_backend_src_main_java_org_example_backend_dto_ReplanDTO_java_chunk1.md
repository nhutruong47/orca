# Knowledge Document: ReplanDTO.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ReplanDTO.java",
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
     public void setCumulativeTarget(double cumulativeTarget) { this.cumulativeTarget = cumulativeTarget; }
        public String getStatus() { return status; }
        public void setStatus(String status) { this.status = status; }
    }

    public UUID getPlanId() { return planId; }
    public void setPlanId(UUID planId) { this.planId = planId; }
    public UUID getOrderId() { return orderId; }
    public void setOrderId(UUID orderId) { this.orderId = orderId; }
    public String getOrderCode() { return orderCode; }
    public void setOrderCode(String orderCode) { this.orderCode = orderCode; }
    public double getOriginalTargetKg() { return originalTargetKg; }
    public void setOriginalTargetKg(double originalTargetKg) { this.originalTargetKg = originalTargetKg; }
    public double getCompletedKg() { return completedKg; }
    public void setCompletedKg(double completedKg) { this.completedKg = completedKg; }
    public double getRemainingKg() { return remainingKg; }
    public void setRemainingKg(double remainingKg) { this.remainingKg = remainingKg; }
    public double getShortFall() { return shortFall; }
    public void setShortFall(double shortFall) { this.shortFall = shortFall; }
    public int getOriginalWorkingDays() { return originalWorkingDays; }
    public void setOriginalWorkingDays(int originalWorkingDays) { this.originalWorkingDays = originalWorkingDays; }
    public int getRemainingWorkingDays() { return remainingWorkingDays; }
    public void setRemainingWorkingDays(int remainingWorkingDays) { this.remainingWorkingDays = remainingWorkingDays; }
    public int getNewWorkingDaysNeeded() { return newWorkingDaysNeeded; }
    public void setNewWorkingDaysNeeded(int newWorkingDaysNeeded) { this.newWorkingDaysNeeded = newWorkingDaysNeeded; }
    public List<ReplanDay> getRevisedDays() { return revisedDays; }
    public void setRevisedDays(List<ReplanDay> revisedDays) { this.revisedDays = revisedDays; }
    public String getReplanStrategy() { return replanStrategy; }
    public void setReplanStrategy(String replanStrategy) { this.replanStrategy = replanStrategy; }
    public List<String> getRecommendations() { return recommendations; }
    public void setRecommendations(List<String> recommendations) { this.recommendations = recommendations; }
    public String getRiskLevel() { return riskLevel; }

```
