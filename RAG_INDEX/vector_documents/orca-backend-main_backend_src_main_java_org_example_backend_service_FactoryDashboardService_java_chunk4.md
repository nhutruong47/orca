# Knowledge Document: FactoryDashboardService.java (Chunk 5/6)

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
  "chunk_index": 4,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, attendance, production, dashboard

## Source Code Chunk
```java
yTeamIdAndStatus(teamId, "IN_PRODUCTION"));
        stats.put("pendingOrders", orderRepo.countByTeamIdAndStatus(teamId, "PENDING"));
        stats.put("totalOrders", (long) orderRepo.findByTeamIdOrderByCreatedAtDesc(teamId).size());
        dashboard.put("stats", stats);

        dashboard.put("upcomingDeadlines", activeOrders.stream()
                .filter(o -> o.getInternalDeadline() != null)
                .sorted(Comparator.comparing(ProductionOrder::getInternalDeadline))
                .limit(5)
                .map(o -> {
                    Map<String, Object> m = new LinkedHashMap<>();
                    m.put("id", o.getId().toString());
                    m.put("title", o.getTitle());
                    m.put("internalDeadline", o.getInternalDeadline());
                    m.put("daysRemaining", ChronoUnit.DAYS.between(now, o.getInternalDeadline()));
                    return m;
                })
                .collect(Collectors.toList()));

        return dashboard;
    }

    public Map<String, Object> getProductivitySummary(UUID teamId, LocalDate startDate, LocalDate endDate) {
        Map<String, Object> summary = new LinkedHashMap<>();
        List<Map<String, Object>> records = new ArrayList<>();
        double totalKg = 0;
        double totalHours = 0;

        LocalDate current = startDate;
        while (!current.isAfter(endDate)) {
            Optional<DailyTarget> targetOpt = targetRepo.findByTeamIdAndDate(teamId, current);
            if (targetOpt.isPresent()) {
                DailyTarget t = targetOpt.get();
                Map<String, Object> record = new LinkedHashMap<>();
                record.put("date", current.toString());
                record.put("targetKg", t.getTargetQuantityKg());
                record.put("actualKg", t.getTotalActualKg());
                record.put("completionRate", t.getCompletionRate());
                record.put("workerHours", t.getTotalWorkerHours());
                record.put("productivity", t.getProductivityKgPerHour());
                records.add(record);

                if (t.getTotalActualKg() != null) totalKg += t.getTotalActualKg();
                if (t.getTotalWorkerHours() != null) totalHours += t.getTotalWorkerHours();
            }
            current = current.plusDays(1);
        }

        summary.put("records", records);
        summary.put("totalKg", totalKg);

```
