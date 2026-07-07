# Knowledge Document: DailyTargetDTO.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/DailyTargetDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 2
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
import java.time.LocalDateTime;
import java.util.List;

public class DailyTargetDTO {
    private String id;
    private String planId;
    private String orderId;
    private String orderTitle;
    private LocalDate targetDate;
    private Double targetQuantityKg;
    private Double targetRoastKg;
    private Double targetQcKg;
    private Double targetPackagedKg;
    private Integer targetPackages;
    private Double actualRoastKg;
    private Double actualQcKg;
    private Double actualQcFailKg;
    private Double actualPackagedKg;
    private Integer actualPackages;
    private Double totalActualKg;
    private Double completionRate;
    private Boolean isHoliday;
    private String notes;
    private String issues;
    private String status;
    private Double totalWorkerHours;
    private Double productivityKgPerHour;

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getPlanId() { return planId; }
    public void setPlanId(String planId) { this.planId = planId; }
    public String getOrderId() { return orderId; }
    public void setOrderId(String orderId) { this.orderId = orderId; }
    public String getOrderTitle() { return orderTitle; }
    public void setOrderTitle(String orderTitle) { this.orderTitle = orderTitle; }
    public LocalDate getTargetDate() { return targetDate; }
    public void setTargetDate(LocalDate targetDate) { this.targetDate = targetDate; }
    public Double getTargetQuantityKg() { return targetQuantityKg; }
    public void setTargetQuantityKg(Double targetQuantityKg) { this.targetQuantityKg = targetQuantityKg; }
    public Double getTargetRoastKg() { return targetRoastKg; }
    public void setTargetRoastKg(Double targetRoastKg) { this.targetRoastKg = targetRoastKg; }
    public Double getTargetQcKg() { return targetQcKg; }
    public void setTargetQcKg(Double targetQcKg) { this.targetQcKg = targetQcKg; }
    public Double getTargetPackagedKg() { return targetPackagedKg; }
    public void setTargetPackagedKg(Double targetPackagedKg) { this.targetPackagedKg = targetPackagedKg; }
    public Integer getTargetPackages() { return targetPackages; }
    public void setTargetPackages(Integer targetPackages) { this.targetPackages = targetPackages; }
    public Double getActualRoastKg() { return actualRoastKg; }

```
