# Knowledge Document: FactoryDashboardService.java (Chunk 1/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/FactoryDashboardService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "attendance",
    "production",
    "dashboard"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, attendance, production, dashboard

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.AttendanceDTO;
import org.example.backend.dto.DailyTargetDTO;
import org.example.backend.dto.ProductionOrderDTO;
import org.example.backend.entity.Attendance;
import org.example.backend.entity.DailyTarget;
import org.example.backend.entity.ProductionOrder;
import org.example.backend.repository.*;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class FactoryDashboardService {

    private final ProductionOrderRepository orderRepo;
    private final AttendanceRepository attendanceRepo;
    private final DailyTargetRepository targetRepo;
    private final ProductionPlanRepository planRepo;
    private final ProductionOrderService orderService;

    public FactoryDashboardService(ProductionOrderRepository orderRepo,
                                   AttendanceRepository attendanceRepo,
                                   DailyTargetRepository targetRepo,
                                   ProductionPlanRepository planRepo,
                                   ProductionOrderService orderService) {
        this.orderRepo = orderRepo;
        this.attendanceRepo = attendanceRepo;
        this.targetRepo = targetRepo;
        this.planRepo = planRepo;
        this.orderService = orderService;
    }

    public Map<String, Object> getDashboard(UUID teamId) {
        Map<String, Object> dashboard = new LinkedHashMap<>();
        LocalDate today = LocalDate.now();
        LocalDateTime now = LocalDateTime.now();

        List<ProductionOrder> activeOrders = orderRepo.findByTeamIdAndStatusInOrderByDeadline(teamId,
                List.of("CONFIRMED", "PLANNING", "IN_PRODUCTION"));
        List<ProductionOrder> overdueOrders = orderRepo.findOverdueOrders(teamId, now);

        List<Map<String, Object>> activeOrdersData = activeOrders.stream()
                .limit(10)
                .map(o -> {
                    Map<String, Object> m = new LinkedHashMap<>();
                    m.put("id", o.getId().toString());
                    m.put("orderCode", o.getOrderCode());
                    m.put("title", o.getTitle());
                    m.put("customerName", o.getCustomerName());

```
