# Knowledge Document: AnalyticsService.java (Chunk 1/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AnalyticsService.java",
  "language": "java",
  "module": "service",
  "business_domain": "analytics",
  "tags": [
    "analytics",
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
- **Tags**: analytics, attendance, production

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.AnalyticsDTO;
import org.example.backend.dto.AnalyticsDTO.*;
import org.example.backend.entity.*;
import org.example.backend.repository.*;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class AnalyticsService {

    private final DailyTargetRepository targetRepo;
    private final ProductionOrderRepository orderRepo;
    private final AttendanceRepository attendanceRepo;

    public AnalyticsService(DailyTargetRepository targetRepo,
                           ProductionOrderRepository orderRepo,
                           AttendanceRepository attendanceRepo) {
        this.targetRepo = targetRepo;
        this.orderRepo = orderRepo;
        this.attendanceRepo = attendanceRepo;
    }

    public AnalyticsDTO getAnalytics(UUID teamId, LocalDate startDate, LocalDate endDate) {
        AnalyticsDTO analytics = new AnalyticsDTO();
        WorkerStatsByStage ws = buildWorkerStats(teamId, startDate, endDate);
        analytics.setWorkerStats(ws);
        analytics.setOrderStats(buildOrderStats(teamId));
        analytics.setDailyTrend(buildDailyTrend(teamId, startDate, endDate));
        analytics.setStageEfficiency(buildStageEfficiency(teamId, startDate, endDate));
        analytics.setOrderAnalytics(buildOrderAnalytics(teamId));
        analytics.setOverallProductivity(ws.getTotalHours() > 0
                ? Math.round(ws.getRoastKg() + ws.getQcKg() + ws.getPackagingKg() / ws.getTotalHours() * 100.0) / 100.0 : 0);
        return analytics;
    }

    private WorkerStatsByStage buildWorkerStats(UUID teamId, LocalDate start, LocalDate end) {
        WorkerStatsByStage stats = new WorkerStatsByStage();
        List<Attendance> attendances = attendanceRepo.findByTeamIdAndDateBetween(teamId, start, end);

        double totalHours = attendances.stream()
                .filter(a -> a.getCheckOutTime() != null)
                .mapToDouble(a -> a.getRegularHours() + a.getOvertimeHours())
                .sum();
        stats.setTotalHours(Math.round(totalHours * 10.0) / 10.0);

        Map<String, Double> stageHours = new LinkedHashMap<>();
        Map<String, Double> stageKg = new LinkedHashMap<>();
        for (Attendance a : attendances) {

```
