# Knowledge Document: AnalyticsDTO.java (Chunk 1/5)

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
  "chunk_index": 0,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDate;
import java.util.List;
import java.util.Map;

public class AnalyticsDTO {

    private WorkerStatsByStage workerStats;
    private OrderStats orderStats;
    private List<DailyProductionRecord> dailyTrend;
    private List<StageEfficiency> stageEfficiency;
    private List<OrderAnalytics> orderAnalytics;
    private double overallProductivity;
    private double totalKgThisWeek;
    private double totalHoursThisWeek;

    public static class WorkerStatsByStage {
        private double roastHours;
        private double qcHours;
        private double packagingHours;
        private double totalHours;
        private double roastKg;
        private double qcKg;
        private double packagingKg;
        private double roastProductivity;
        private double qcProductivity;
        private double packagingProductivity;

        public double getRoastHours() { return roastHours; }
        public void setRoastHours(double roastHours) { this.roastHours = roastHours; }
        public double getQcHours() { return qcHours; }
        public void setQcHours(double qcHours) { this.qcHours = qcHours; }
        public double getPackagingHours() { return packagingHours; }
        public void setPackagingHours(double packagingHours) { this.packagingHours = packagingHours; }
        public double getTotalHours() { return totalHours; }
        public void setTotalHours(double totalHours) { this.totalHours = totalHours; }
        public double getRoastKg() { return roastKg; }
        public void setRoastKg(double roastKg) { this.roastKg = roastKg; }
        public double getQcKg() { return qcKg; }
        public void setQcKg(double qcKg) { this.qcKg = qcKg; }
        public double getPackagingKg() { return packagingKg; }
        public void setPackagingKg(double packagingKg) { this.packagingKg = packagingKg; }
        public double getRoastProductivity() { return roastProductivity; }
        public void setRoastProductivity(double roastProductivity) { this.roastProductivity = roastProductivity; }
        public double getQcProductivity() { return qcProductivity; }
        public void setQcProductivity(double qcProductivity) { this.qcProductivity = qcProductivity; }
        public double getPackagingProductivity() { return packagingProductivity; }

```
