# Knowledge Document: ProductionPlanService.java (Chunk 3/8)

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
  "chunk_index": 2,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
O(savedPlan);
    }

    public ProductionPlanDTO getPlanById(UUID planId) {
        ProductionPlan plan = planRepo.findById(planId)
                .orElseThrow(() -> new RuntimeException("Khong tim thay ke hoach"));
        return toPlanDTO(plan);
    }

    public List<ProductionPlanDTO> getPlansByOrder(UUID orderId) {
        return planRepo.findByOrderIdOrderByCreatedAtDesc(orderId).stream()
                .map(this::toPlanDTO)
                .collect(Collectors.toList());
    }

    @Transactional
    public ProductionPlanDTO approvePlan(UUID planId, UUID approvedBy) {
        ProductionPlan plan = planRepo.findById(planId)
                .orElseThrow(() -> new RuntimeException("Khong tim thay ke hoach"));
        plan.setStatus(PlanStatus.APPROVED);
        plan.setApprovedAt(LocalDateTime.now());
        plan.setApprovedBy(approvedBy);

        ProductionOrder order = plan.getOrder();
        order.setStatus("PLANNING");
        orderRepo.save(order);

        return toPlanDTO(planRepo.save(plan));
    }

    @Transactional
    public DailyTargetDTO updateDailyActual(UUID targetId, Double actualRoastKg, Double actualQcKg,
                                            Double actualQcFailKg, Double actualPackagedKg,
                                            Integer actualPackages, String notes, String issues) {
        DailyTarget target = targetRepo.findById(targetId)
                .orElseThrow(() -> new RuntimeException("Khong tim thay muc tieu ngay"));

        if (actualRoastKg != null) target.setActualRoastKg(actualRoastKg);
        if (actualQcKg != null) target.setActualQcKg(actualQcKg);
        if (actualQcFailKg != null) target.setActualQcFailKg(actualQcFailKg);
        if (actualPackagedKg != null) target.setActualPackagedKg(actualPackagedKg);
        if (actualPackages != null) target.setActualPackages(actualPackages);
        if (notes != null) target.setNotes(notes);
        if (issues != null) target.setIssues(issues);

        double totalActual = 0.0;
        if (target.getActualRoastKg() != null) totalActual += target.getActualRoastKg();
        if (target.getActualPackagedKg() != null) totalActual += target.getActualPackagedKg();
        else if (target.getActualQcKg() != null) totalActual += target.getActualQcKg();
        target.setTotalActualKg(totalActual);
        target.calculateCompletionRate();


```
