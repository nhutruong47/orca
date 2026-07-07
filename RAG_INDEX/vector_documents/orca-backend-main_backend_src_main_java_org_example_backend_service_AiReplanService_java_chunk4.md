# Knowledge Document: AiReplanService.java (Chunk 5/6)

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
  "chunk_index": 4,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
lActualKg() != null && t.getTotalActualKg() > 0) {
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
                                               int remainingDays, int newDaysNeeded,
                                               ProductionOrder order, boolean underperforming) {
        List<String> recs = new ArrayList<>();

        if (underperforming) {
            recs.add("San luong thuc te (" + Math.round(avgActual * 100.0) / 100.0 + " kg/ngay) thap hon ke hoach (" + Math.round(originalTarget * 100.0) / 100.0 + " kg/ngay).");
        }

        if (remainingDays == 0 && remainingKg > 0) {
            recs.add("Da het han lam viec nhung con " + Math.round(remainingKg * 100.0) / 100.0 + " kg chua hoan thanh. Can gia han them " + newDaysNeeded + " ngay.");
        }

        if (remainingDays > 0 && newDaysNeeded > remainingDays) {
            int extraDays = newDaysNeeded - remainingDays;
            recs.add("Can them " + extraDays + " ngay lam viec de hoan thanh muc tieu. De xuat tang ca hoac thue them nhan su.");
        }

        if (avgActual > 0 && remainingKg / avgActual <= 2) {
            recs.add("Kha nang hoan thanh dung han: cao. Tien do hien tai on dinh.");
        }

        if (order.getInternalDeadline() != null) {
            long daysLeft = ChronoUnit.DAYS.between(LocalDate.now(), order.getInternalDeadline().toLocalDate());
            if (daysLeft <= 2) {
                recs.add("Can CHAP CANH: han noi bo chi con " + daysLeft + " ngay. Kiem tra kha nang giao hang ngay.");
            }
        }

        double shortfallPercent = originalTarget > 0 ? (originalTarget - avgActual) / originalTarget * 100 : 0;
        if (shortfallPercent > 20) {
            recs.add("Thieu " + Math.round(shortfallPercent) + "% so voi ke hoach. Xem xet tang ca 2 gio/ngay de bup gap.");
        }

        return recs;
    }

    private String calcRiskLevel(ProductionOrder order, double remainingKg, int remainingDays, double avgDailyActual) {
        if (remainingKg <= 0) return "NONE";

```
