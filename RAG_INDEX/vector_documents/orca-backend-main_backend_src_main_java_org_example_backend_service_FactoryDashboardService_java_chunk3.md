# Knowledge Document: FactoryDashboardService.java (Chunk 4/6)

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
  "chunk_index": 3,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, attendance, production, dashboard

## Source Code Chunk
```java
 "info");
            alert.put("message", notCheckedOut + " nhan vien chua check-out");
            alerts.add(alert);
        }

        if (todayAttendances.size() < 3) {
            Map<String, Object> alert = new LinkedHashMap<>();
            alert.put("type", "STAFF_LOW");
            alert.put("level", "info");
            alert.put("message", "So nhan vien hom nay thap hon binh thuong");
            alerts.add(alert);
        }

        dashboard.put("activeOrdersCount", activeOrders.size());
        dashboard.put("activeOrders", activeOrdersData);
        dashboard.put("todayTarget", todayTarget.map(t -> {
            Map<String, Object> m = new LinkedHashMap<>();
            m.put("id", t.getId().toString());
            m.put("targetQuantityKg", t.getTargetQuantityKg());
            m.put("targetRoastKg", t.getTargetRoastKg());
            m.put("targetQcKg", t.getTargetQcKg());
            m.put("targetPackagedKg", t.getTargetPackagedKg());
            m.put("actualRoastKg", t.getActualRoastKg());
            m.put("actualQcKg", t.getActualQcKg());
            m.put("actualPackagedKg", t.getActualPackagedKg());
            m.put("totalActualKg", t.getTotalActualKg());
            m.put("completionRate", t.getCompletionRate());
            m.put("status", t.getStatus().name());
            m.put("totalWorkerHours", t.getTotalWorkerHours());
            m.put("productivityKgPerHour", t.getProductivityKgPerHour());
            return m;
        }).orElse(null));

        dashboard.put("staffToday", todayAttendances.size());
        dashboard.put("staffDetails", staffData);
        dashboard.put("totalWorkerHoursToday", totalWorkerHours);
        dashboard.put("alerts", alerts);

        Map<String, Long> stats = new LinkedHashMap<>();
        stats.put("completedOrders", orderRepo.countByTeamIdAndStatus(teamId, "COMPLETED"));
        stats.put("inProductionOrders", orderRepo.countByTeamIdAndStatus(teamId, "IN_PRODUCTION"));
        stats.put("pendingOrders", orderRepo.countByTeamIdAndStatus(teamId, "PENDING"));
        stats.put("totalOrders", (long) orderRepo.findByTeamIdOrderByCreatedAtDesc(teamId).size());
        dashboard.put("stats", stats);

        dashboard.put("upcomingDeadlines", activeOrders.stream()
                .filter(o -> o.getInternalDeadline() != null)

```
