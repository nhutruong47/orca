# Knowledge Document: ProductionBoardService.java (Chunk 2/6)

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
  "chunk_index": 1,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
yTargets, "packaging");
        board.setRoast(roast);
        board.setQc(qc);
        board.setPackaging(packaging);

        double totalTarget = roast.getTargetKg() + qc.getTargetKg() + packaging.getTargetKg();
        double totalActual = roast.getActualKg() + qc.getActualKg() + packaging.getActualKg();
        board.setTotalTargetKg(totalTarget);
        board.setTotalActualKg(totalActual);
        board.setCompletionRate(totalTarget > 0 ? Math.round(totalActual / totalTarget * 10000.0) / 100.0 : 0.0);

        List<OrderStageRow> orderRows = activeOrders.stream()
                .map(order -> buildOrderRow(order, date))
                .filter(r -> r.getRoastTarget() > 0 || r.getQcTarget() > 0 || r.getPackagingTarget() > 0)
                .collect(Collectors.toList());
        board.setOrderRows(orderRows);

        List<Attendance> attendances = attendanceRepo.findByTeamIdAndDate(teamId, date);
        board.setTotalWorkers(attendances.size());
        double totalHours = attendances.stream()
                .filter(a -> a.getCheckOutTime() != null)
                .mapToDouble(a -> a.getRegularHours() + a.getOvertimeHours())
                .sum();
        board.setTotalWorkerHours(Math.round(totalHours * 10.0) / 10.0);

        return board;
    }

    public List<DailyBoardDTO> getCalendarBoard(UUID teamId, LocalDate startDate, LocalDate endDate) {
        List<DailyBoardDTO> days = new ArrayList<>();
        LocalDate current = startDate;
        while (!current.isAfter(endDate)) {
            days.add(getDailyBoard(teamId, current));
            current = current.plusDays(1);
        }
        return days;
    }

    private StageSummary buildStageSummary(List<DailyTarget> targets, String stage) {
        StageSummary s = new StageSummary();
        double targetKg = 0, actualKg = 0, workerHours = 0;
        int orderCount = 0;
        Set<UUID> seenOrders = new HashSet<>();

        for (DailyTarget t : targets) {
            if (t.getIsHoliday() != null && t.getIsHoliday()) continue;

            if ("roast".equals(stage)) {
                if (t.getTargetRoastKg() != null) targetKg += t.getTargetRoastKg();
                if (t.getActualRoastKg() != null) actualKg += t.getActualRoastKg();
            } else if ("qc".equals(stage)) {
                if (t.getTargetQcKg() != null) targetKg += t.getTargetQcKg();

```
