# Knowledge Document: AnalyticsDTO.java (Chunk 3/5)

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
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```java
te double qcKg;
        private double packagingKg;
        private double workerHours;

        public LocalDate getDate() { return date; }
        public void setDate(LocalDate date) { this.date = date; }
        public double getTargetKg() { return targetKg; }
        public void setTargetKg(double targetKg) { this.targetKg = targetKg; }
        public double getActualKg() { return actualKg; }
        public void setActualKg(double actualKg) { this.actualKg = actualKg; }
        public double getCompletionRate() { return completionRate; }
        public void setCompletionRate(double completionRate) { this.completionRate = completionRate; }
        public double getRoastKg() { return roastKg; }
        public void setRoastKg(double roastKg) { this.roastKg = roastKg; }
        public double getQcKg() { return qcKg; }
        public void setQcKg(double qcKg) { this.qcKg = qcKg; }
        public double getPackagingKg() { return packagingKg; }
        public void setPackagingKg(double packagingKg) { this.packagingKg = packagingKg; }
        public double getWorkerHours() { return workerHours; }
        public void setWorkerHours(double workerHours) { this.workerHours = workerHours; }
    }

    public static class StageEfficiency {
        private String stage;
        private double totalTargetKg;
        private double totalActualKg;
        private double efficiency;
        private double avgProductivity;
        private double failRate;

        public String getStage() { return stage; }
        public void setStage(String stage) { this.stage = stage; }
        public double getTotalTargetKg() { return totalTargetKg; }
        public void setTotalTargetKg(double totalTargetKg) { this.totalTargetKg = totalTargetKg; }
        public double getTotalActualKg() { return totalActualKg; }
        public void setTotalActualKg(double totalActualKg) { this.totalActualKg = totalActualKg; }
        public double getEfficiency() { return efficiency; }
        public void setEfficiency(double efficiency) { this.efficiency = efficiency; }
        public double getAvgProductivity() { return avgProductivity; }
        public void setAvgProductivity(double avgProductivity) { this.avgProductivity = avgProductivity; }
        public double getFailRate() { return failRate; }
        public void setFailRate(double failRate) { this.failRate = failRate; }
    }


```
