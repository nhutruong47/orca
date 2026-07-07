# Knowledge Document: FactoryDashboardService.java (Chunk 3/6)

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
  "chunk_index": 2,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, attendance, production, dashboard

## Source Code Chunk
```java
.getOvertimeHours()));
                    m.put("attendanceStatus", a.getAttendanceStatus() != null ? a.getAttendanceStatus().name() : null);
                    if (a.getProductionOrder() != null) {
                        m.put("orderTitle", a.getProductionOrder().getTitle());
                    }
                    return m;
                })
                .collect(Collectors.toList());

        double totalWorkerHours = todayAttendances.stream()
                .filter(a -> a.getCheckOutTime() != null)
                .mapToDouble(a -> a.getRegularHours() + a.getOvertimeHours())
                .sum();

        Optional<DailyTarget> todayTarget = targetRepo.findByTeamIdAndDate(teamId, today);

        List<Map<String, Object>> alerts = new ArrayList<>();

        for (ProductionOrder o : overdueOrders) {
            Map<String, Object> alert = new LinkedHashMap<>();
            alert.put("type", "ORDER_AT_RISK");
            alert.put("level", "warning");
            alert.put("message", "Don \"" + o.getTitle() + "\" sap het han noi bo!");
            alert.put("relatedId", o.getId().toString());
            alerts.add(alert);
        }

        if (todayTarget.isPresent()) {
            DailyTarget t = todayTarget.get();
            if (t.getCompletionRate() != null && t.getCompletionRate() < 80) {
                Map<String, Object> alert = new LinkedHashMap<>();
                alert.put("type", "TARGET_LOW");
                alert.put("level", "warning");
                alert.put("message", "Muc tieu hom nay moi dat " + t.getCompletionRate().intValue() + "%");
                alert.put("relatedId", t.getId().toString());
                alerts.add(alert);
            }
        }

        long notCheckedOut = attendanceRepo.countNotCheckedOut(teamId, today);
        if (notCheckedOut > 0) {
            Map<String, Object> alert = new LinkedHashMap<>();
            alert.put("type", "MISSING_CHECKOUT");
            alert.put("level", "info");
            alert.put("message", notCheckedOut + " nhan vien chua check-out");
            alerts.add(alert);
        }

        if (todayAttendances.size() < 3) {
            Map<String, Object> alert = new LinkedHashMap<>();
            alert.put("type", "STAFF_LOW");
            alert.put("level", "info");
            alert.put("message", "So nhan vien hom nay thap hon binh thuong");

```
