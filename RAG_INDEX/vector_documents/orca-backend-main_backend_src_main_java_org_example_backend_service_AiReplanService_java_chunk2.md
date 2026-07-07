# Knowledge Document: AiReplanService.java (Chunk 3/6)

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
  "chunk_index": 2,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
Days(revisedDays);

        List<String> recommendations = buildRecommendations(avgDailyActual, plan.getDailyTargetKg(), remainingKg,
                remainingWorkingDays, newDaysNeeded, order, underperforming);
        dto.setRecommendations(recommendations);

        String riskLevel = calcRiskLevel(order, remainingKg, remainingWorkingDays, avgDailyActual);
        dto.setRiskLevel(riskLevel);

        boolean needsReplan = underperforming
                || remainingKg > 0 && remainingWorkingDays == 0
                || (remainingWorkingDays > 0 && newDaysNeeded > remainingWorkingDays);
        dto.setNeedsReplan(needsReplan);

        if (needsReplan) {
            dto.setReplanStrategy(underperforming ? "TANG_NGAY_CONG"
                    : remainingWorkingDays == 0 ? "KE_DAIL"
                    : "CAN_CHINH_MUC_TIEU");
        } else {
            dto.setReplanStrategy("KHONG_CAN");
        }

        return dto;
    }

    @Transactional
    public void applyReplan(UUID orderId, List<Map<String, Object>> revisedTargets) {
        ProductionOrder order = orderRepo.findById(orderId)
                .orElseThrow(() -> new RuntimeException("Khong tim thay don hang"));

        ProductionPlan plan = planRepo.findTopByOrderIdOrderByCreatedAtDesc(orderId)
                .orElseThrow(() -> new RuntimeException("Chua co ke hoach"));

        for (Map<String, Object> revised : revisedTargets) {
            String targetIdStr = (String) revised.get("targetId");
            if (targetIdStr == null) continue;
            UUID targetId = UUID.fromString(targetIdStr);
            Optional<DailyTarget> tOpt = targetRepo.findById(targetId);
            if (tOpt.isEmpty()) continue;
            DailyTarget t = tOpt.get();

            if (revised.get("targetQuantityKg") != null) {
                t.setTargetQuantityKg(((Number) revised.get("targetQuantityKg")).doubleValue());
            }
            if (revised.get("targetRoastKg") != null) {
                t.setTargetRoastKg(((Number) revised.get("targetRoastKg")).doubleValue());
            }
            if (revised.get("targetQcKg") != null) {
                t.setTargetQcKg(((Number) revised.get("targetQcKg")).doubleValue());
            }
            if (revised.get("targetPackagedKg") != null) {
                t.setTargetPackagedKg(((Number) revised.get("targetPackagedKg")).doubleValue());
            }

```
