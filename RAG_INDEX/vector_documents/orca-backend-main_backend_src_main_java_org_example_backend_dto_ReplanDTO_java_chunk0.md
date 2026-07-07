# Knowledge Document: ReplanDTO.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ReplanDTO.java",
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

import java.util.List;
import java.util.UUID;

public class ReplanDTO {

    private UUID planId;
    private UUID orderId;
    private String orderCode;
    private double originalTargetKg;
    private double completedKg;
    private double remainingKg;
    private double shortFall;
    private int originalWorkingDays;
    private int remainingWorkingDays;
    private int newWorkingDaysNeeded;
    private List<ReplanDay> revisedDays;
    private String replanStrategy;
    private List<String> recommendations;
    private String riskLevel;
    private boolean needsReplan;

    public static class ReplanDay {
        private int dayIndex;
        private String date;
        private double originalTargetKg;
        private double revisedTargetKg;
        private double actualKg;
        private double cumulativeActual;
        private double cumulativeTarget;
        private String status;

        public int getDayIndex() { return dayIndex; }
        public void setDayIndex(int dayIndex) { this.dayIndex = dayIndex; }
        public String getDate() { return date; }
        public void setDate(String date) { this.date = date; }
        public double getOriginalTargetKg() { return originalTargetKg; }
        public void setOriginalTargetKg(double originalTargetKg) { this.originalTargetKg = originalTargetKg; }
        public double getRevisedTargetKg() { return revisedTargetKg; }
        public void setRevisedTargetKg(double revisedTargetKg) { this.revisedTargetKg = revisedTargetKg; }
        public double getActualKg() { return actualKg; }
        public void setActualKg(double actualKg) { this.actualKg = actualKg; }
        public double getCumulativeActual() { return cumulativeActual; }
        public void setCumulativeActual(double cumulativeActual) { this.cumulativeActual = cumulativeActual; }
        public double getCumulativeTarget() { return cumulativeTarget; }
        public void setCumulativeTarget(double cumulativeTarget) { this.cumulativeTarget = cumulativeTarget; }
        public String getStatus() { return status; }
        public void setStatus(String status) { this.status = status; }
    }

    public UUID getPlanId() { return planId; }
    public void setPlanId(UUID planId) { this.planId = planId; }
    public UUID getOrderId() { return orderId; }

```
