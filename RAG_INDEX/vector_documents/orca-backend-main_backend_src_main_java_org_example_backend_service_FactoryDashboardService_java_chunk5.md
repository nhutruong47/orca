# Knowledge Document: FactoryDashboardService.java (Chunk 6/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/FactoryDashboardService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "attendance",
    "production",
    "dashboard"
  ],
  "logical_type": "Service",
  "chunk_index": 5,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, attendance, production, dashboard

## Source Code Chunk
```java
ity", t.getProductivityKgPerHour());
                records.add(record);

                if (t.getTotalActualKg() != null) totalKg += t.getTotalActualKg();
                if (t.getTotalWorkerHours() != null) totalHours += t.getTotalWorkerHours();
            }
            current = current.plusDays(1);
        }

        summary.put("records", records);
        summary.put("totalKg", totalKg);
        summary.put("totalWorkerHours", totalHours);
        summary.put("averageProductivity", totalHours > 0 ? Math.round((totalKg / totalHours) * 100.0) / 100.0 : 0);
        summary.put("workingDays", records.size());

        return summary;
    }

    private boolean isAtRisk(ProductionOrder order) {
        if (order.getInternalDeadline() == null) return false;
        if ("COMPLETED".equals(order.getStatus()) || "DELIVERED".equals(order.getStatus())) return false;
        long daysLeft = ChronoUnit.DAYS.between(LocalDateTime.now(), order.getInternalDeadline());
        return daysLeft <= 3;
    }
}

```
