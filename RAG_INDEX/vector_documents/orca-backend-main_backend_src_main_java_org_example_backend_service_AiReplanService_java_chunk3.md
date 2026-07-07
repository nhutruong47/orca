# Knowledge Document: AiReplanService.java (Chunk 4/6)

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
  "chunk_index": 3,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
RoastKg(((Number) revised.get("targetRoastKg")).doubleValue());
            }
            if (revised.get("targetQcKg") != null) {
                t.setTargetQcKg(((Number) revised.get("targetQcKg")).doubleValue());
            }
            if (revised.get("targetPackagedKg") != null) {
                t.setTargetPackagedKg(((Number) revised.get("targetPackagedKg")).doubleValue());
            }
            targetRepo.save(t);
        }

        plan.setDailyTargetKg(plan.getDailyTargetKg());
        plan.setRiskFactors("Da duoc AI replan luc " + LocalDate.now());
        planRepo.save(plan);

        order.setStatus("IN_PRODUCTION");
        orderRepo.save(order);
    }

    private List<ReplanDay> buildRevisedDays(List<DailyTarget> futureTargets,
                                              double completedKg, double remainingKg,
                                              double avgDailyActual, double originalTarget) {
        List<ReplanDay> days = new ArrayList<>();
        double cumulativeActual = completedKg;

        for (int i = 0; i < futureTargets.size(); i++) {
            DailyTarget t = futureTargets.get(i);
            ReplanDay r = new ReplanDay();
            r.setDayIndex(i + 1);
            r.setDate(t.getTargetDate().toString());
            r.setOriginalTargetKg(t.getTargetQuantityKg() != null ? t.getTargetQuantityKg() : 0);
            r.setActualKg(t.getTotalActualKg() != null ? t.getTotalActualKg() : 0);
            r.setCumulativeActual(Math.round(cumulativeActual * 100.0) / 100.0);
            r.setCumulativeTarget(Math.round(r.getOriginalTargetKg() * (i + 1) * 100.0) / 100.0);

            double revised = Math.min(avgDailyActual * 1.2, remainingKg / Math.max(1, futureTargets.size()));
            r.setRevisedTargetKg(Math.round(revised * 100.0) / 100.0);

            if (t.getStatus() == TargetStatus.COMPLETED) {
                r.setStatus("DA_HOAN_THANH");
            } else if (t.getTotalActualKg() != null && t.getTotalActualKg() > 0) {
                r.setStatus("DANG_THUC_HIEN");
            } else {
                r.setStatus("CHUA_THUC_HIEN");
            }

            cumulativeActual += r.getActualKg();
            days.add(r);
        }
        return days;
    }

    private List<String> buildRecommendations(double avgActual, double originalTarget, double remainingKg,

```
