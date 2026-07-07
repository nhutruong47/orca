# Knowledge Document: DailyBoardDTO.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/DailyBoardDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "DTO",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
astTarget = roastTarget; }
        public double getQcTarget() { return qcTarget; }
        public void setQcTarget(double qcTarget) { this.qcTarget = qcTarget; }
        public double getPackagingTarget() { return packagingTarget; }
        public void setPackagingTarget(double packagingTarget) { this.packagingTarget = packagingTarget; }
        public String getRiskLevel() { return riskLevel; }
        public void setRiskLevel(String riskLevel) { this.riskLevel = riskLevel; }
        public String getStageStatus() { return stageStatus; }
        public void setStageStatus(String stageStatus) { this.stageStatus = stageStatus; }
        public int getDaysToDeadline() { return daysToDeadline; }
        public void setDaysToDeadline(int daysToDeadline) { this.daysToDeadline = daysToDeadline; }
    }

    public LocalDate getDate() { return date; }
    public void setDate(LocalDate date) { this.date = date; }
    public StageSummary getRoast() { return roast; }
    public void setRoast(StageSummary roast) { this.roast = roast; }
    public StageSummary getQc() { return qc; }
    public void setQc(StageSummary qc) { this.qc = qc; }
    public StageSummary getPackaging() { return packaging; }
    public void setPackaging(StageSummary packaging) { this.packaging = packaging; }
    public double getTotalTargetKg() { return totalTargetKg; }
    public void setTotalTargetKg(double totalTargetKg) { this.totalTargetKg = totalTargetKg; }
    public double getTotalActualKg() { return totalActualKg; }
    public void setTotalActualKg(double totalActualKg) { this.totalActualKg = totalActualKg; }
    public double getCompletionRate() { return completionRate; }
    public void setCompletionRate(double completionRate) { this.completionRate = completionRate; }
    public List<OrderStageRow> getOrderRows() { return orderRows; }
    public void setOrderRows(List<OrderStageRow> orderRows) { this.orderRows = orderRows; }
    public int getTotalWorkers() { return totalWorkers; }
    public void setTotalWorkers(int totalWorkers) { this.totalWorkers = totalWorkers; }
    public double getTotalWorkerHours() { return totalWorkerHours; }
    public void setTotalWorkerHours(double totalWorkerHours) { this.totalWorkerHours = totalWorkerHours; }
}

```
