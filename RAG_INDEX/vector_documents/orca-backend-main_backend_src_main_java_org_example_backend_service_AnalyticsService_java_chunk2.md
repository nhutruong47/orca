# Knowledge Document: AnalyticsService.java (Chunk 3/6)

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
  "chunk_index": 2,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, attendance, production

## Source Code Chunk
```java
    stats.setPackagingProductivity(stats.getPackagingHours() > 0 ? Math.round(packagingKg / stats.getPackagingHours() * 100.0) / 100.0 : 0);

        return stats;
    }

    private OrderStats buildOrderStats(UUID teamId) {
        OrderStats stats = new OrderStats();
        List<ProductionOrder> orders = orderRepo.findByTeamIdOrderByCreatedAtDesc(teamId);
        stats.setTotal(orders.size());
        stats.setCompleted(orders.stream().filter(o -> "COMPLETED".equals(o.getStatus()) || "DELIVERED".equals(o.getStatus())).count());
        stats.setInProduction(orders.stream().filter(o -> "IN_PRODUCTION".equals(o.getStatus())).count());
        stats.setPending(orders.stream().filter(o -> "PENDING".equals(o.getStatus()) || "CONFIRMED".equals(o.getStatus()) || "PLANNING".equals(o.getStatus())).count());

        long atRisk = orders.stream().filter(o -> {
            if (o.getInternalDeadline() == null) return false;
            if ("COMPLETED".equals(o.getStatus()) || "DELIVERED".equals(o.getStatus())) return false;
            return ChronoUnit.DAYS.between(LocalDate.now(), o.getInternalDeadline().toLocalDate()) <= 3;
        }).count();
        stats.setAtRisk(atRisk);

        double avgYield = orders.stream()
                .filter(o -> o.getExpectedYield() != null && o.getExpectedYield() > 0)
                .mapToDouble(ProductionOrder::getExpectedYield)
                .average()
                .orElse(0);
        stats.setAvgYield(Math.round(avgYield * 10000.0) / 10000.0);

        return stats;
    }

    private List<DailyProductionRecord> buildDailyTrend(UUID teamId, LocalDate start, LocalDate end) {
        List<DailyProductionRecord> records = new ArrayList<>();
        LocalDate current = start;
        while (!current.isAfter(end)) {
            DailyProductionRecord r = new DailyProductionRecord();
            r.setDate(current);
            Optional<DailyTarget> tOpt = targetRepo.findByTeamIdAndDate(teamId, current);
            if (tOpt.isPresent()) {
                DailyTarget t = tOpt.get();
                r.setTargetKg(t.getTargetQuantityKg() != null ? t.getTargetQuantityKg() : 0);
                r.setActualKg(t.getTotalActualKg() != null ? t.getTotalActualKg() : 0);
                r.setCompletionRate(t.getCompletionRate() != null ? t.getCompletionRate() : 0);

```
