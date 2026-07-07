# Knowledge Document: AnalyticsDTO.java (Chunk 5/5)

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
  "chunk_index": 4,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```java
eld; }
        public void setActualYield(double actualYield) { this.actualYield = actualYield; }
        public double getLeadTimeDays() { return leadTimeDays; }
        public void setLeadTimeDays(double leadTimeDays) { this.leadTimeDays = leadTimeDays; }
        public String getRiskLevel() { return riskLevel; }
        public void setRiskLevel(String riskLevel) { this.riskLevel = riskLevel; }
        public String getStatus() { return status; }
        public void setStatus(String status) { this.status = status; }
    }

    public WorkerStatsByStage getWorkerStats() { return workerStats; }
    public void setWorkerStats(WorkerStatsByStage workerStats) { this.workerStats = workerStats; }
    public OrderStats getOrderStats() { return orderStats; }
    public void setOrderStats(OrderStats orderStats) { this.orderStats = orderStats; }
    public List<DailyProductionRecord> getDailyTrend() { return dailyTrend; }
    public void setDailyTrend(List<DailyProductionRecord> dailyTrend) { this.dailyTrend = dailyTrend; }
    public List<StageEfficiency> getStageEfficiency() { return stageEfficiency; }
    public void setStageEfficiency(List<StageEfficiency> stageEfficiency) { this.stageEfficiency = stageEfficiency; }
    public List<OrderAnalytics> getOrderAnalytics() { return orderAnalytics; }
    public void setOrderAnalytics(List<OrderAnalytics> orderAnalytics) { this.orderAnalytics = orderAnalytics; }
    public double getOverallProductivity() { return overallProductivity; }
    public void setOverallProductivity(double overallProductivity) { this.overallProductivity = overallProductivity; }
    public double getTotalKgThisWeek() { return totalKgThisWeek; }
    public void setTotalKgThisWeek(double totalKgThisWeek) { this.totalKgThisWeek = totalKgThisWeek; }
    public double getTotalHoursThisWeek() { return totalHoursThisWeek; }
    public void setTotalHoursThisWeek(double totalHoursThisWeek) { this.totalHoursThisWeek = totalHoursThisWeek; }
}

```
