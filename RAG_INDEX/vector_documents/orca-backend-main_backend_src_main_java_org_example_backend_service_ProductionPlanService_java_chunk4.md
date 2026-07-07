# Knowledge Document: ProductionPlanService.java (Chunk 5/8)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ProductionPlanService.java",
  "language": "java",
  "module": "service",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Service",
  "chunk_index": 4,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
blic List<DailyTargetDTO> getDailyTargetsByPlan(UUID planId) {
        return targetRepo.findByPlanIdOrderByTargetDateAsc(planId).stream()
                .map(this::toTargetDTO)
                .collect(Collectors.toList());
    }

    public DailyTargetDTO getTodayTarget(UUID teamId) {
        return targetRepo.findByTeamIdAndDate(teamId, LocalDate.now())
                .map(this::toTargetDTO)
                .orElse(null);
    }

    private List<DailyTarget> buildDailyTargets(ProductionPlan plan, ProductionOrder order,
                                                  LocalDate startDate, LocalDate endDate,
                                                  double dailyTargetKg) {
        List<DailyTarget> targets = new ArrayList<>();
        LocalDate current = startDate;

        int packageSize = order.getPackageSize() != null ? parsePackageSize(order.getPackageSize()) : 1;
        int totalPackages = order.getTotalPackages() != null ? order.getTotalPackages() : (int) Math.ceil(order.getOutputTarget() / packageSize);

        int dayIndex = 0;
        while (!current.isAfter(endDate)) {
            DayOfWeek dow = current.getDayOfWeek();
            DailyTarget target = new DailyTarget();
            target.setPlan(plan);
            target.setOrder(order);
            target.setTargetDate(current);

            if (dow == DayOfWeek.SATURDAY || dow == DayOfWeek.SUNDAY) {
                target.setIsHoliday(true);
                target.setTargetQuantityKg(0.0);
                target.setTargetRoastKg(0.0);
                target.setTargetQcKg(0.0);
                target.setTargetPackagedKg(0.0);
                target.setTargetPackages(0);
                target.setStatus(TargetStatus.SKIPPED);
            } else {
                target.setIsHoliday(false);
                target.setTargetQuantityKg(dailyTargetKg);
                target.setStatus(TargetStatus.PENDING);

                if (dayIndex < 3) {
                    target.setTargetRoastKg(dailyTargetKg * 1.05);
                    target.setTargetQcKg(dailyTargetKg);
                    target.setTargetPackagedKg(0.0);
                } else if (dayIndex < 5) {
                    target.setTargetRoastKg(dailyTargetKg);
                    target.setTargetQcKg(dailyTargetKg * 1.05);
                    target.setTargetPackagedKg(dailyTargetKg * 0.9);
                } else {

```
