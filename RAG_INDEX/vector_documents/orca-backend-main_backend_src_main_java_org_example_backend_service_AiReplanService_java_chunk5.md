# Knowledge Document: AiReplanService.java (Chunk 6/6)

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
  "chunk_index": 5,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
tual) / originalTarget * 100 : 0;
        if (shortfallPercent > 20) {
            recs.add("Thieu " + Math.round(shortfallPercent) + "% so voi ke hoach. Xem xet tang ca 2 gio/ngay de bup gap.");
        }

        return recs;
    }

    private String calcRiskLevel(ProductionOrder order, double remainingKg, int remainingDays, double avgDailyActual) {
        if (remainingKg <= 0) return "NONE";
        if (order.getInternalDeadline() == null) return avgDailyActual < 50 ? "HIGH" : "MEDIUM";

        long daysLeft = ChronoUnit.DAYS.between(LocalDate.now(), order.getInternalDeadline().toLocalDate());
        if (daysLeft <= 0) return "CRITICAL";
        if (daysLeft <= 2) return "HIGH";
        if (daysLeft <= 5) return "MEDIUM";

        double projectedCompletion = remainingDays * avgDailyActual;
        if (projectedCompletion < remainingKg) return "HIGH";
        return "LOW";
    }
}

```
