# Knowledge Document: ProductionPlanService.java (Chunk 1/8)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ProductionPlanService.java",
  "language": "java",
  "module": "service",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.DailyTargetDTO;
import org.example.backend.dto.ProductionPlanDTO;
import org.example.backend.entity.*;
import org.example.backend.entity.DailyTarget.TargetStatus;
import org.example.backend.entity.ProductionPlan.PlanStatus;
import org.example.backend.repository.*;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class ProductionPlanService {

    private final ProductionPlanRepository planRepo;
    private final ProductionOrderRepository orderRepo;
    private final DailyTargetRepository targetRepo;
    private final AttendanceRepository attendanceRepo;

    public ProductionPlanService(ProductionPlanRepository planRepo, ProductionOrderRepository orderRepo,
                                 DailyTargetRepository targetRepo, AttendanceRepository attendanceRepo) {
        this.planRepo = planRepo;
        this.orderRepo = orderRepo;
        this.targetRepo = targetRepo;
        this.attendanceRepo = attendanceRepo;
    }

    @Transactional
    public ProductionPlanDTO generatePlan(UUID orderId) {
        ProductionOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Khong tim thay don hang"));

        double outputTarget = order.getOutputTarget() != null ? order.getOutputTarget() : 0;
        LocalDate startDate = order.getProductionStartDate() != null
                ? order.getProductionStartDate()
                : LocalDate.now();
        LocalDate endDate = order.getInternalDeadline() != null
                ? order.getInternalDeadline().toLocalDate()
                : startDate.plusDays(30);

        int totalDays = (int) (endDate.toEpochDay() - startDate.toEpochDay()) + 1;
        int workingDays = countWorkingDays(startDate, endDate);

        double dailyTargetKg = workingDays > 0
                ? Math.ceil((outputTarget / workingDays) * 100.0) / 100.0
                : outputTarget;

        double inputRequired = order.getInputRequired() != null ? order.getInputRequired() : outputTarget;
        double roastKg = inputRequired;

```
