# Knowledge Document: AnalyticsService.java (Chunk 4/6)

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
  "chunk_index": 3,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, attendance, production

## Source Code Chunk
```java
epo.findByTeamIdAndDate(teamId, current);
            if (tOpt.isPresent()) {
                DailyTarget t = tOpt.get();
                r.setTargetKg(t.getTargetQuantityKg() != null ? t.getTargetQuantityKg() : 0);
                r.setActualKg(t.getTotalActualKg() != null ? t.getTotalActualKg() : 0);
                r.setCompletionRate(t.getCompletionRate() != null ? t.getCompletionRate() : 0);
                r.setRoastKg(t.getActualRoastKg() != null ? t.getActualRoastKg() : 0);
                r.setQcKg(t.getActualQcKg() != null ? t.getActualQcKg() : 0);
                r.setPackagingKg(t.getActualPackagedKg() != null ? t.getActualPackagedKg() : 0);
                r.setWorkerHours(t.getTotalWorkerHours() != null ? t.getTotalWorkerHours() : 0);
            }
            records.add(r);
            current = current.plusDays(1);
        }
        return records;
    }

    private List<StageEfficiency> buildStageEfficiency(UUID teamId, LocalDate start, LocalDate end) {
        List<StageEfficiency> list = new ArrayList<>();
        List<DailyTarget> targets = getTargetsInRange(teamId, start, end);

        String[] stages = {"RANG", "QC", "DONG_GOI"};
        String[] stageLabels = {"Rang", "QC", "Dong goi"};

        for (int i = 0; i < stages.length; i++) {
            StageEfficiency se = new StageEfficiency();
            se.setStage(stageLabels[i]);

            double targetKg = 0, actualKg = 0, failKg = 0, workerHours = 0;
            int daysWithData = 0;
            List<Double> productivities = new ArrayList<>();

            for (DailyTarget t : targets) {
                if (t.getIsHoliday() != null && t.getIsHoliday()) continue;
                double tKg = 0, aKg = 0;
                if ("RANG".equals(stages[i])) { tKg = n(t.getTargetRoastKg()); aKg = n(t.getActualRoastKg()); }
                else if ("QC".equals(stages[i])) { tKg = n(t.getTargetQcKg()); aKg = n(t.getActualQcKg()); failKg += n(t.getActualQcFailKg()); }
                else if ("DONG_GOI".equals(stages[i])) { tKg = n(t.getTargetPackagedKg()); aKg = n(t.getActualPackagedKg()); }

                targetKg += tKg;
                actualKg += aKg;
                workerHours += n(t.getTotalWorkerHours());
                if (tKg > 0 || aKg > 0) daysWithData++;
                if (t.getProductivityKgPerHour() != null) productivities.add(t.getProductivityKgPerHour());

```
