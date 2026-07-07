# Knowledge Document: DailyBoardDTO.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/DailyBoardDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDate;
import java.util.List;
import java.util.Map;

public class DailyBoardDTO {

    private LocalDate date;
    private StageSummary roast;
    private StageSummary qc;
    private StageSummary packaging;
    private double totalTargetKg;
    private double totalActualKg;
    private double completionRate;
    private List<OrderStageRow> orderRows;
    private int totalWorkers;
    private double totalWorkerHours;

    public static class StageSummary {
        private double targetKg;
        private double actualKg;
        private double completionRate;
        private int orderCount;
        private double workerHours;

        public double getTargetKg() { return targetKg; }
        public void setTargetKg(double targetKg) { this.targetKg = targetKg; }
        public double getActualKg() { return actualKg; }
        public void setActualKg(double actualKg) { this.actualKg = actualKg; }
        public double getCompletionRate() { return completionRate; }
        public void setCompletionRate(double completionRate) { this.completionRate = completionRate; }
        public int getOrderCount() { return orderCount; }
        public void setOrderCount(int orderCount) { this.orderCount = orderCount; }
        public double getWorkerHours() { return workerHours; }
        public void setWorkerHours(double workerHours) { this.workerHours = workerHours; }
    }

    public static class OrderStageRow {
        private String orderId;
        private String orderCode;
        private String title;
        private String customerName;
        private double outputTarget;
        private double completedQuantity;
        private double remainingQuantity;
        private double progressPercent;
        private double roastActual;
        private double qcActual;
        private double packagingActual;
        private double roastTarget;
        private double qcTarget;
        private double packagingTarget;
        private String riskLevel;
        private String stageStatus;
        private int daysToDeadline;

        public String getOrderId() { return orderId; }
        public void setOrderId(String orderId) { this.orderId = orderId; }
        public String getOrderCode() { return orderCode; }
        public void setOrderCode(String orderCode) { this.orderCode = orderCode; }

```
