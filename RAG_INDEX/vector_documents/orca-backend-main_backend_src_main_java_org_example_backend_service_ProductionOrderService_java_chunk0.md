# Knowledge Document: ProductionOrderService.java (Chunk 1/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ProductionOrderService.java",
  "language": "java",
  "module": "service",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.ProductionOrderDTO;
import org.example.backend.entity.Attendance;
import org.example.backend.entity.ProductionBatch;
import org.example.backend.entity.ProductionOrder;
import org.example.backend.entity.ProductionPlan;
import org.example.backend.entity.Team;
import org.example.backend.repository.AttendanceRepository;
import org.example.backend.repository.DailyTargetRepository;
import org.example.backend.repository.ProductionBatchRepository;
import org.example.backend.repository.ProductionOrderRepository;
import org.example.backend.repository.ProductionPlanRepository;
import org.example.backend.repository.TeamRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.util.List;
import java.util.UUID;

@Service
public class ProductionOrderService {

    private final ProductionOrderRepository orderRepo;
    private final TeamRepository teamRepo;
    private final ProductionPlanRepository planRepo;
    private final DailyTargetRepository dailyTargetRepo;
    private final ProductionBatchRepository batchRepo;
    private final AttendanceRepository attendanceRepo;

    public ProductionOrderService(
            ProductionOrderRepository orderRepo,
            TeamRepository teamRepo,
            ProductionPlanRepository planRepo,
            DailyTargetRepository dailyTargetRepo,
            ProductionBatchRepository batchRepo,
            AttendanceRepository attendanceRepo) {
        this.orderRepo = orderRepo;
        this.teamRepo = teamRepo;
        this.planRepo = planRepo;
        this.dailyTargetRepo = dailyTargetRepo;
        this.batchRepo = batchRepo;
        this.attendanceRepo = attendanceRepo;
    }

    @Transactional
    public ProductionOrder createOrder(UUID teamId, ProductionOrder raw) {
        Team team = teamRepo.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        ProductionOrder order = new ProductionOrder();
        order.setTeam(team);
        applyEditableFields(order, raw);
        order.setStatus("PENDING");

        validateOrder(order);
        order.calculateInputRequired();

        return orderRepo.save(order);
    }

    @Transactional

```
