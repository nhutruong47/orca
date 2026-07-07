# Knowledge Document: ProductionBoardService.java (Chunk 4/6)

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
  "chunk_index": 3,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
etRepo.findByOrderIdAndTargetDate(order.getId(), date);
        if (targetOpt.isPresent()) {
            DailyTarget t = targetOpt.get();
            r.setRoastTarget(t.getTargetRoastKg() != null ? t.getTargetRoastKg() : 0);
            r.setQcTarget(t.getTargetQcKg() != null ? t.getTargetQcKg() : 0);
            r.setPackagingTarget(t.getTargetPackagedKg() != null ? t.getTargetPackagedKg() : 0);
            r.setRoastActual(t.getActualRoastKg() != null ? t.getActualRoastKg() : 0);
            r.setQcActual(t.getActualQcKg() != null ? t.getActualQcKg() : 0);
            r.setPackagingActual(t.getActualPackagedKg() != null ? t.getActualPackagedKg() : 0);
            r.setStageStatus(t.getStatus() != null ? t.getStatus().name() : "PENDING");
        }

        if (order.getInternalDeadline() != null) {
            r.setDaysToDeadline((int) ChronoUnit.DAYS.between(date, order.getInternalDeadline().toLocalDate()));
        } else {
            r.setDaysToDeadline(-1);
        }

        return r;
    }

    private String calcRiskLevel(ProductionOrder order) {
        if (order.getInternalDeadline() == null) return "NONE";
        if ("COMPLETED".equals(order.getStatus()) || "DELIVERED".equals(order.getStatus())) return "NONE";
        long daysLeft = ChronoUnit.DAYS.between(LocalDateTime.now(), order.getInternalDeadline());
        if (daysLeft <= 0) return "CRITICAL";
        if (daysLeft <= 2) return "HIGH";
        if (daysLeft <= 5) return "MEDIUM";
        return "LOW";
    }

    public Map<String, Object> getWorkforceToday(UUID teamId) {
        Map<String, Object> result = new LinkedHashMap<>();
        LocalDate today = LocalDate.now();

        List<Attendance> attendances = attendanceRepo.findByTeamIdAndDate(teamId, today);

        List<ProductionOrder> activeOrders = orderRepo.findByTeamIdAndStatusInOrderByDeadline(teamId,
                List.of("CONFIRMED", "PLANNING", "IN_PRODUCTION"));

        List<Map<String, Object>> checkedIn = new ArrayList<>();
        List<Map<String, Object>> checkedOut = new ArrayList<>();
        List<Map<String, Object>> notCheckedIn = new ArrayList<>();

        for (Attendance a : attendances) {
            Map<String, Object> w = new LinkedHashMap<>();
            w.put("userId", a.getUser().getId().toString());
            w.put("userName", a.getUser().getFullName());

```
