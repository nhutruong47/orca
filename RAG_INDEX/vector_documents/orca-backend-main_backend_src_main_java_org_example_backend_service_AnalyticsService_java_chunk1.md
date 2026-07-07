# Knowledge Document: AnalyticsService.java (Chunk 2/6)

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
  "chunk_index": 1,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, attendance, production

## Source Code Chunk
```java
m()
                .filter(a -> a.getCheckOutTime() != null)
                .mapToDouble(a -> a.getRegularHours() + a.getOvertimeHours())
                .sum();
        stats.setTotalHours(Math.round(totalHours * 10.0) / 10.0);

        Map<String, Double> stageHours = new LinkedHashMap<>();
        Map<String, Double> stageKg = new LinkedHashMap<>();
        for (Attendance a : attendances) {
            if (a.getStage() != null && a.getCheckOutTime() != null) {
                String stage = stageKey(a.getStage());
                double hours = a.getRegularHours() + a.getOvertimeHours();
                stageHours.merge(stage, hours, Double::sum);
            }
        }
        stats.setRoastHours(round(stageHours.getOrDefault("RANG", 0.0)));
        stats.setQcHours(round(stageHours.getOrDefault("QA", 0.0)));
        stats.setPackagingHours(round(stageHours.getOrDefault("DONG_GOI", 0.0)));

        List<DailyTarget> targets = getTargetsInRange(teamId, start, end);
        double roastKg = targets.stream().filter(t -> t.getActualRoastKg() != null).mapToDouble(DailyTarget::getActualRoastKg).sum();
        double qcKg = targets.stream().filter(t -> t.getActualQcKg() != null).mapToDouble(DailyTarget::getActualQcKg).sum();
        double packagingKg = targets.stream().filter(t -> t.getActualPackagedKg() != null).mapToDouble(DailyTarget::getActualPackagedKg).sum();
        stats.setRoastKg(Math.round(roastKg * 100.0) / 100.0);
        stats.setQcKg(Math.round(qcKg * 100.0) / 100.0);
        stats.setPackagingKg(Math.round(packagingKg * 100.0) / 100.0);

        double totalKg = roastKg + qcKg + packagingKg;
        stats.setRoastProductivity(stats.getRoastHours() > 0 ? Math.round(roastKg / stats.getRoastHours() * 100.0) / 100.0 : 0);
        stats.setQcProductivity(stats.getQcHours() > 0 ? Math.round(qcKg / stats.getQcHours() * 100.0) / 100.0 : 0);
        stats.setPackagingProductivity(stats.getPackagingHours() > 0 ? Math.round(packagingKg / stats.getPackagingHours() * 100.0) / 100.0 : 0);

        return stats;
    }

    private OrderStats buildOrderStats(UUID teamId) {
        OrderStats stats = new OrderStats();
        List<ProductionOrder> orders = orderRepo.findByTeamIdOrderByCreatedAtDesc(teamId);
        stats.setTotal(orders.size());

```
