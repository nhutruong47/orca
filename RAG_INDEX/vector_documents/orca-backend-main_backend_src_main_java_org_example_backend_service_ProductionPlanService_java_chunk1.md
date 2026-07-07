# Knowledge Document: ProductionPlanService.java (Chunk 2/8)

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
  "chunk_index": 1,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
() - startDate.toEpochDay()) + 1;
        int workingDays = countWorkingDays(startDate, endDate);

        double dailyTargetKg = workingDays > 0
                ? Math.ceil((outputTarget / workingDays) * 100.0) / 100.0
                : outputTarget;

        double inputRequired = order.getInputRequired() != null ? order.getInputRequired() : outputTarget;
        double roastKg = inputRequired;
        double qcKg = outputTarget * 1.05;
        double packagedKg = outputTarget;
        int packages = order.getTotalPackages() != null ? order.getTotalPackages()
                : (int) Math.ceil(outputTarget / (order.getPackageSize() != null ? parsePackageSize(order.getPackageSize()) : 1.0));

        List<String> riskFactors = new ArrayList<>();
        if (dailyTargetKg > 100) {
            riskFactors.add("Muc tieu ngay cao (" + dailyTargetKg + " kg). Can kiem tra cong suat may.");
        }
        if (workingDays < 5) {
            riskFactors.add("So ngay lam viec it, can tang ca hoac them nhan su.");
        }

        String aiRecs = buildAiRecommendations(outputTarget, dailyTargetKg, workingDays, order);

        ProductionPlan plan = new ProductionPlan();
        plan.setOrder(order);
        plan.setTotalDays(totalDays);
        plan.setTotalWorkingDays(workingDays);
        plan.setDailyTargetKg(dailyTargetKg);
        plan.setTotalInputKg(inputRequired);
        plan.setTotalRoastKg(roastKg);
        plan.setTotalQcKg(qcKg);
        plan.setTotalPackagedKg(packagedKg);
        plan.setTotalPackages(packages);
        plan.setAiRecommendations(aiRecs);
        plan.setRiskFactors(riskFactors.isEmpty() ? null : String.join("; ", riskFactors));
        plan.setStatus(PlanStatus.DRAFT);

        List<DailyTarget> targets = buildDailyTargets(plan, order, startDate, endDate, dailyTargetKg);
        plan.setDailyTargets(targets);

        ProductionPlan savedPlan = planRepo.save(plan);
        targetRepo.saveAll(targets);
        return toPlanDTO(savedPlan);
    }

    public ProductionPlanDTO getPlanById(UUID planId) {
        ProductionPlan plan = planRepo.findById(planId)
                .orElseThrow(() -> new RuntimeException("Khong tim thay ke hoach"));
        return toPlanDTO(plan);
    }

    public List<ProductionPlanDTO> getPlansByOrder(UUID orderId) {
        return planRepo.findByOrderIdOrderByCreatedAtDesc(orderId).stream()

```
