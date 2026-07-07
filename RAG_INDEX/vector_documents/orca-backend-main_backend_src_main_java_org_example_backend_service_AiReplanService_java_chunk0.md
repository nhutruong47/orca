# Knowledge Document: AiReplanService.java (Chunk 1/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AiReplanService.java",
  "language": "java",
  "module": "service",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.ReplanDTO;
import org.example.backend.dto.ReplanDTO.ReplanDay;
import org.example.backend.entity.*;
import org.example.backend.entity.DailyTarget.TargetStatus;
import org.example.backend.entity.ProductionPlan.PlanStatus;
import org.example.backend.repository.*;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.*;

@Service
public class AiReplanService {

    private final ProductionPlanRepository planRepo;
    private final ProductionOrderRepository orderRepo;
    private final DailyTargetRepository targetRepo;

    public AiReplanService(ProductionPlanRepository planRepo,
                           ProductionOrderRepository orderRepo,
                           DailyTargetRepository targetRepo) {
        this.planRepo = planRepo;
        this.orderRepo = orderRepo;
        this.targetRepo = targetRepo;
    }

    public ReplanDTO analyzeReplan(UUID orderId) {
        ProductionOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Khong tim thay don hang"));

        ProductionPlan plan = planRepo.findTopByOrderIdOrderByCreatedAtDesc(orderId)
                .orElseThrow(() -> new RuntimeException("Chua co ke hoach san xuat"));

        List<DailyTarget> allTargets = targetRepo.findByOrderIdOrderByTargetDateAsc(orderId);
        LocalDate today = LocalDate.now();

        double completedKg = allTargets.stream()
                .filter(t -> t.getTotalActualKg() != null)
                .mapToDouble(DailyTarget::getTotalActualKg)
                .sum();

        double outputTarget = order.getOutputTarget() != null ? order.getOutputTarget() : 0;
        double remainingKg = Math.max(0, outputTarget - completedKg);

        List<DailyTarget> pastTargets = allTargets.stream()
                .filter(t -> !t.getTargetDate().isAfter(today))
                .filter(t -> t.getIsHoliday() == null || !t.getIsHoliday())
                .toList();

        List<DailyTarget> futureTargets = allTargets.stream()
                .filter(t -> t.getTargetDate().isAfter(today))
                .filter(t -> t.getIsHoliday() == null || !t.getIsHoliday())
                .toList();


```
