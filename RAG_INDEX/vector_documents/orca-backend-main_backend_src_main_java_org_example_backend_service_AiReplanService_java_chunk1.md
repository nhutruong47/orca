# Knowledge Document: AiReplanService.java (Chunk 2/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AiReplanService.java",
  "language": "java",
  "module": "service",
  "business_domain": "production",
  "tags": [
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
- **Tags**: production

## Source Code Chunk
```java
()
                .filter(t -> !t.getTargetDate().isAfter(today))
                .filter(t -> t.getIsHoliday() == null || !t.getIsHoliday())
                .toList();

        List<DailyTarget> futureTargets = allTargets.stream()
                .filter(t -> t.getTargetDate().isAfter(today))
                .filter(t -> t.getIsHoliday() == null || !t.getIsHoliday())
                .toList();

        int originalWorkingDays = (int) allTargets.stream()
                .filter(t -> t.getIsHoliday() == null || !t.getIsHoliday())
                .count();
        int remainingWorkingDays = futureTargets.size();

        double avgDailyActual = pastTargets.isEmpty() ? plan.getDailyTargetKg()
                : pastTargets.stream().filter(t -> t.getTotalActualKg() != null)
                        .mapToDouble(DailyTarget::getTotalActualKg)
                        .average().orElse(plan.getDailyTargetKg());

        boolean underperforming = avgDailyActual < plan.getDailyTargetKg() * 0.8;

        ReplanDTO dto = new ReplanDTO();
        dto.setPlanId(plan.getId());
        dto.setOrderId(orderId);
        dto.setOrderCode(order.getOrderCode());
        dto.setOriginalTargetKg(plan.getDailyTargetKg());
        dto.setCompletedKg(Math.round(completedKg * 100.0) / 100.0);
        dto.setRemainingKg(Math.round(remainingKg * 100.0) / 100.0);
        dto.setShortFall(Math.round((plan.getDailyTargetKg() - avgDailyActual) * 100.0) / 100.0);
        dto.setOriginalWorkingDays(originalWorkingDays);
        dto.setRemainingWorkingDays(remainingWorkingDays);

        int newDaysNeeded = remainingWorkingDays > 0
                ? (int) Math.ceil(remainingKg / avgDailyActual)
                : remainingWorkingDays;
        dto.setNewWorkingDaysNeeded(Math.max(0, newDaysNeeded - remainingWorkingDays));

        List<ReplanDay> revisedDays = buildRevisedDays(futureTargets, completedKg, remainingKg, avgDailyActual, plan.getDailyTargetKg());
        dto.setRevisedDays(revisedDays);

        List<String> recommendations = buildRecommendations(avgDailyActual, plan.getDailyTargetKg(), remainingKg,
                remainingWorkingDays, newDaysNeeded, order, underperforming);
        dto.setRecommendations(recommendations);

        String riskLevel = calcRiskLevel(order, remainingKg, remainingWorkingDays, avgDailyActual);
        dto.setRiskLevel(riskLevel);


```
