# Knowledge Document: ProductionBoardService.java (Chunk 1/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ProductionBoardService.java",
  "language": "java",
  "module": "service",
  "business_domain": "attendance",
  "tags": [
    "attendance",
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
- **Tags**: attendance, production

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.DailyBoardDTO;
import org.example.backend.dto.DailyBoardDTO.OrderStageRow;
import org.example.backend.dto.DailyBoardDTO.StageSummary;
import org.example.backend.entity.*;
import org.example.backend.entity.Attendance.ProductionStage;
import org.example.backend.repository.*;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class ProductionBoardService {

    private final DailyTargetRepository targetRepo;
    private final ProductionOrderRepository orderRepo;
    private final AttendanceRepository attendanceRepo;
    private final ProductionPlanRepository planRepo;

    public ProductionBoardService(DailyTargetRepository targetRepo,
                                  ProductionOrderRepository orderRepo,
                                  AttendanceRepository attendanceRepo,
                                  ProductionPlanRepository planRepo) {
        this.targetRepo = targetRepo;
        this.orderRepo = orderRepo;
        this.attendanceRepo = attendanceRepo;
        this.planRepo = planRepo;
    }

    public DailyBoardDTO getDailyBoard(UUID teamId, LocalDate date) {
        DailyBoardDTO board = new DailyBoardDTO();
        board.setDate(date);

        List<ProductionOrder> activeOrders = orderRepo.findByTeamIdAndStatusInOrderByDeadline(teamId,
                List.of("CONFIRMED", "PLANNING", "IN_PRODUCTION"));

        List<DailyTarget> todayTargets = targetRepo.findByTeamIdAndDate(teamId, date)
                .map(t -> List.of(t))
                .orElse(List.of());

        StageSummary roast = buildStageSummary(todayTargets, "roast");
        StageSummary qc = buildStageSummary(todayTargets, "qc");
        StageSummary packaging = buildStageSummary(todayTargets, "packaging");
        board.setRoast(roast);
        board.setQc(qc);
        board.setPackaging(packaging);

        double totalTarget = roast.getTargetKg() + qc.getTargetKg() + packaging.getTargetKg();
        double totalActual = roast.getActualKg() + qc.getActualKg() + packaging.getActualKg();
        board.setTotalTargetKg(totalTarget);
        board.setTotalActualKg(totalActual);

```
