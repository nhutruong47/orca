# Knowledge Document: ProductionPlanService.java (Chunk 6/8)

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
  "chunk_index": 5,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
astKg(dailyTargetKg * 1.05);
                    target.setTargetQcKg(dailyTargetKg);
                    target.setTargetPackagedKg(0.0);
                } else if (dayIndex < 5) {
                    target.setTargetRoastKg(dailyTargetKg);
                    target.setTargetQcKg(dailyTargetKg * 1.05);
                    target.setTargetPackagedKg(dailyTargetKg * 0.9);
                } else {
                    target.setTargetRoastKg(0.0);
                    target.setTargetQcKg(0.0);
                    target.setTargetPackagedKg(dailyTargetKg);
                }
                target.setTargetPackages((int) Math.ceil(totalPackages * dailyTargetKg / order.getOutputTarget()));
            }

            targets.add(target);
            current = current.plusDays(1);
            dayIndex++;
        }
        return targets;
    }

    private int countWorkingDays(LocalDate start, LocalDate end) {
        int count = 0;
        LocalDate current = start;
        while (!current.isAfter(end)) {
            DayOfWeek dow = current.getDayOfWeek();
            if (dow != DayOfWeek.SATURDAY && dow != DayOfWeek.SUNDAY) count++;
            current = current.plusDays(1);
        }
        return count;
    }

    private String buildAiRecommendations(double outputTarget, double dailyTargetKg,
                                          int workingDays, ProductionOrder order) {
        StringBuilder sb = new StringBuilder();
        sb.append("- Muc tieu san xuat: ").append(outputTarget).append(" kg\n");
        sb.append("- Ngay lam viec: ").append(workingDays).append(" ngay\n");
        sb.append("- Muc tieu moi ngay: ").append(dailyTargetKg).append(" kg\n");
        if (order.getExpectedYield() != null) {
            sb.append("- Ty le thu hoi: ").append((order.getExpectedYield() * 100)).append("%\n");
        }
        if (order.getInputRequired() != null) {
            sb.append("- Nguyen lieu can: ").append(order.getInputRequired()).append(" kg\n");
        }
        sb.append("- Ngay bat dau: ").append(order.getProductionStartDate()).append("\n");
        sb.append("- Han noi bo: ").append(order.getInternalDeadline()).append("\n");
        return sb.toString();
    }

    private int parsePackageSize(String packageSize) {
        try {
            if (packageSize == null) return 1;
            String num = packageSize.replaceAll("[^0-9]", "");

```
