# Knowledge Document: ProductionPlanService.java (Chunk 4/8)

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
  "chunk_index": 3,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
s);

        double totalActual = 0.0;
        if (target.getActualRoastKg() != null) totalActual += target.getActualRoastKg();
        if (target.getActualPackagedKg() != null) totalActual += target.getActualPackagedKg();
        else if (target.getActualQcKg() != null) totalActual += target.getActualQcKg();
        target.setTotalActualKg(totalActual);
        target.calculateCompletionRate();

        UUID orderId = target.getOrder().getId();
        Double workerHours = attendanceRepo.sumWorkerHoursByTeamAndDate(
                target.getOrder().getTeam().getId(), target.getTargetDate());
        if (workerHours != null && workerHours > 0) {
            target.setTotalWorkerHours(workerHours);
            target.calculateProductivity();
        }

        if (target.getCompletionRate() != null) {
            if (target.getCompletionRate() >= 100) {
                target.setStatus(TargetStatus.COMPLETED);
            } else if (target.getCompletionRate() > 0) {
                target.setStatus(TargetStatus.PARTIAL);
            } else {
                target.setStatus(TargetStatus.IN_PROGRESS);
            }
        }

        updateOrderCompletedQuantity(orderId);

        return toTargetDTO(targetRepo.save(target));
    }

    private void updateOrderCompletedQuantity(UUID orderId) {
        List<DailyTarget> allTargets = targetRepo.findByOrderIdOrderByTargetDateAsc(orderId);
        double totalCompleted = allTargets.stream()
                .filter(t -> t.getTotalActualKg() != null)
                .mapToDouble(DailyTarget::getTotalActualKg)
                .sum();
        ProductionOrder order = orderRepo.findById(orderId).orElse(null);
        if (order != null) {
            order.setCompletedQuantity(totalCompleted);
            if (totalCompleted >= (order.getOutputTarget() != null ? order.getOutputTarget() : 0)) {
                order.setStatus("COMPLETED");
            }
            orderRepo.save(order);
        }
    }

    public List<DailyTargetDTO> getDailyTargetsByPlan(UUID planId) {
        return targetRepo.findByPlanIdOrderByTargetDateAsc(planId).stream()
                .map(this::toTargetDTO)
                .collect(Collectors.toList());
    }

    public DailyTargetDTO getTodayTarget(UUID teamId) {
        return targetRepo.findByTeamIdAndDate(teamId, LocalDate.now())
                .map(this::toTargetDTO)

```
