# Knowledge Document: ProductionPlanDTO.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ProductionPlanDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDateTime;
import java.util.List;

public class ProductionPlanDTO {
    private String id;
    private String orderId;
    private String orderTitle;
    private String planCode;
    private Integer totalDays;
    private Integer totalWorkingDays;
    private Double dailyTargetKg;
    private Double totalInputKg;
    private Double totalRoastKg;
    private Double totalQcKg;
    private Double totalPackagedKg;
    private Integer totalPackages;
    private String aiRecommendations;
    private String riskFactors;
    private String status;
    private List<DailyTargetDTO> dailyTargets;
    private LocalDateTime createdAt;
    private LocalDateTime approvedAt;
    private String approvedBy;

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getOrderId() { return orderId; }
    public void setOrderId(String orderId) { this.orderId = orderId; }
    public String getOrderTitle() { return orderTitle; }
    public void setOrderTitle(String orderTitle) { this.orderTitle = orderTitle; }
    public String getPlanCode() { return planCode; }
    public void setPlanCode(String planCode) { this.planCode = planCode; }
    public Integer getTotalDays() { return totalDays; }
    public void setTotalDays(Integer totalDays) { this.totalDays = totalDays; }
    public Integer getTotalWorkingDays() { return totalWorkingDays; }
    public void setTotalWorkingDays(Integer totalWorkingDays) { this.totalWorkingDays = totalWorkingDays; }
    public Double getDailyTargetKg() { return dailyTargetKg; }
    public void setDailyTargetKg(Double dailyTargetKg) { this.dailyTargetKg = dailyTargetKg; }
    public Double getTotalInputKg() { return totalInputKg; }
    public void setTotalInputKg(Double totalInputKg) { this.totalInputKg = totalInputKg; }
    public Double getTotalRoastKg() { return totalRoastKg; }
    public void setTotalRoastKg(Double totalRoastKg) { this.totalRoastKg = totalRoastKg; }
    public Double getTotalQcKg() { return totalQcKg; }
    public void setTotalQcKg(Double totalQcKg) { this.totalQcKg = totalQcKg; }
    public Double getTotalPackagedKg() { return totalPackagedKg; }
    public void setTotalPackagedKg(Double totalPackagedKg) { this.totalPackagedKg = totalPackagedKg; }
    public Integer getTotalPackages() { return totalPackages; }

```
