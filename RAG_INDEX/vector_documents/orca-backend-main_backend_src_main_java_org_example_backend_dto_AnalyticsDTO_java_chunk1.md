# Knowledge Document: AnalyticsDTO.java (Chunk 2/5)

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
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```java
{ return roastProductivity; }
        public void setRoastProductivity(double roastProductivity) { this.roastProductivity = roastProductivity; }
        public double getQcProductivity() { return qcProductivity; }
        public void setQcProductivity(double qcProductivity) { this.qcProductivity = qcProductivity; }
        public double getPackagingProductivity() { return packagingProductivity; }
        public void setPackagingProductivity(double packagingProductivity) { this.packagingProductivity = packagingProductivity; }
    }

    public static class OrderStats {
        private long total;
        private long completed;
        private long inProduction;
        private long pending;
        private long atRisk;
        private double avgLeadTime;
        private double avgYield;

        public long getTotal() { return total; }
        public void setTotal(long total) { this.total = total; }
        public long getCompleted() { return completed; }
        public void setCompleted(long completed) { this.completed = completed; }
        public long getInProduction() { return inProduction; }
        public void setInProduction(long inProduction) { this.inProduction = inProduction; }
        public long getPending() { return pending; }
        public void setPending(long pending) { this.pending = pending; }
        public long getAtRisk() { return atRisk; }
        public void setAtRisk(long atRisk) { this.atRisk = atRisk; }
        public double getAvgLeadTime() { return avgLeadTime; }
        public void setAvgLeadTime(double avgLeadTime) { this.avgLeadTime = avgLeadTime; }
        public double getAvgYield() { return avgYield; }
        public void setAvgYield(double avgYield) { this.avgYield = avgYield; }
    }

    public static class DailyProductionRecord {
        private LocalDate date;
        private double targetKg;
        private double actualKg;
        private double completionRate;
        private double roastKg;
        private double qcKg;
        private double packagingKg;
        private double workerHours;

        public LocalDate getDate() { return date; }
        public void setDate(LocalDate date) { this.date = date; }
        public double getTargetKg() { return targetKg; }
        public void setTargetKg(double targetKg) { this.targetKg = targetKg; }
        public double getActualKg() { return actualKg; }

```
