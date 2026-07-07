# Knowledge Document: AnalyticsService.java (Chunk 5/6)

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
  "chunk_index": 4,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, attendance, production

## Source Code Chunk
```java
lse if ("DONG_GOI".equals(stages[i])) { tKg = n(t.getTargetPackagedKg()); aKg = n(t.getActualPackagedKg()); }

                targetKg += tKg;
                actualKg += aKg;
                workerHours += n(t.getTotalWorkerHours());
                if (tKg > 0 || aKg > 0) daysWithData++;
                if (t.getProductivityKgPerHour() != null) productivities.add(t.getProductivityKgPerHour());
            }

            se.setTotalTargetKg(Math.round(targetKg * 100.0) / 100.0);
            se.setTotalActualKg(Math.round(actualKg * 100.0) / 100.0);
            se.setEfficiency(targetKg > 0 ? Math.round(actualKg / targetKg * 10000.0) / 100.0 : 0);
            se.setAvgProductivity(productivities.isEmpty() ? 0 : Math.round(productivities.stream().mapToDouble(Double::doubleValue).average().orElse(0) * 100.0) / 100.0);
            se.setFailRate(actualKg > 0 ? Math.round(failKg / actualKg * 10000.0) / 100.0 : 0);
            list.add(se);
        }

        return list;
    }

    private List<OrderAnalytics> buildOrderAnalytics(UUID teamId) {
        List<ProductionOrder> orders = orderRepo.findByTeamIdAndStatusInOrderByDeadline(teamId,
                List.of("CONFIRMED", "PLANNING", "IN_PRODUCTION", "COMPLETED"));

        return orders.stream().map(o -> {
            OrderAnalytics a = new OrderAnalytics();
            a.setOrderId(o.getId().toString());
            a.setOrderCode(o.getOrderCode());
            a.setTitle(o.getTitle());
            a.setOutputTarget(o.getOutputTarget() != null ? o.getOutputTarget() : 0);
            a.setCompletedQuantity(o.getCompletedQuantity() != null ? o.getCompletedQuantity() : 0);
            a.setProgressPercent(o.getProgressPercent());
            a.setExpectedYield(o.getExpectedYield() != null ? o.getExpectedYield() : 0);
            a.setActualYield(a.getOutputTarget() > 0 && a.getCompletedQuantity() > 0
                    ? Math.round(a.getCompletedQuantity() / a.getOutputTarget() * 10000.0) / 10000.0 : 0);
            a.setStatus(o.getStatus());
            a.setRiskLevel(calcRiskLevel(o));

            if (o.getProductionStartDate() != null && o.getCustomerDeliveryDate() != null) {
                a.setLeadTimeDays((int) ChronoUnit.DAYS.between(o.getProductionStartDate(), o.getCustomerDeliveryDate()));
            }

            return a;
        }).collect(Collectors.toList());
    }


```
