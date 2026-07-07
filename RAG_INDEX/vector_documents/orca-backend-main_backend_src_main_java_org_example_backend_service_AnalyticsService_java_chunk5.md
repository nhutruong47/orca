# Knowledge Document: AnalyticsService.java (Chunk 6/6)

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
  "chunk_index": 5,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, attendance, production

## Source Code Chunk
```java
000.0 : 0);
            a.setStatus(o.getStatus());
            a.setRiskLevel(calcRiskLevel(o));

            if (o.getProductionStartDate() != null && o.getCustomerDeliveryDate() != null) {
                a.setLeadTimeDays((int) ChronoUnit.DAYS.between(o.getProductionStartDate(), o.getCustomerDeliveryDate()));
            }

            return a;
        }).collect(Collectors.toList());
    }

    private List<DailyTarget> getTargetsInRange(UUID teamId, LocalDate start, LocalDate end) {
        List<ProductionOrder> orders = orderRepo.findByTeamIdOrderByCreatedAtDesc(teamId);
        List<DailyTarget> all = new ArrayList<>();
        for (ProductionOrder o : orders) {
            all.addAll(targetRepo.findByOrderIdAndDateRange(o.getId(), start, end));
        }
        return all;
    }

    private String stageKey(Attendance.ProductionStage stage) {
        if (stage == null) return "OTHER";
        return switch (stage) {
            case RANH_VA_CHON, RANG -> "RANG";
            case QA, XAY -> "QC";
            case DONG_GOI -> "DONG_GOI";
        };
    }

    private String calcRiskLevel(ProductionOrder o) {
        if (o.getInternalDeadline() == null) return "NONE";
        if ("COMPLETED".equals(o.getStatus()) || "DELIVERED".equals(o.getStatus())) return "NONE";
        long days = ChronoUnit.DAYS.between(LocalDate.now(), o.getInternalDeadline().toLocalDate());
        if (days <= 0) return "CRITICAL";
        if (days <= 2) return "HIGH";
        if (days <= 5) return "MEDIUM";
        return "LOW";
    }

    private double n(Double v) { return v != null ? v : 0; }
    private double round(double v) { return Math.round(v * 10.0) / 10.0; }
}

```
