# Knowledge Document: ProductionBoardService.java (Chunk 5/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ProductionBoardService.java",
  "language": "java",
  "module": "service",
  "business_domain": "attendance",
  "tags": [
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
- **Tags**: attendance, production

## Source Code Chunk
```java
ng, Object>> checkedIn = new ArrayList<>();
        List<Map<String, Object>> checkedOut = new ArrayList<>();
        List<Map<String, Object>> notCheckedIn = new ArrayList<>();

        for (Attendance a : attendances) {
            Map<String, Object> w = new LinkedHashMap<>();
            w.put("userId", a.getUser().getId().toString());
            w.put("userName", a.getUser().getFullName());
            w.put("shiftType", a.getShiftType() != null ? a.getShiftType().name() : null);
            w.put("stage", a.getStage() != null ? a.getStage().name() : null);
            w.put("checkInTime", a.getCheckInTime());
            w.put("checkOutTime", a.getCheckOutTime());
            w.put("attendanceStatus", a.getAttendanceStatus() != null ? a.getAttendanceStatus().name() : null);
            w.put("actualWorkHours", a.getActualWorkHours());
            w.put("regularHours", a.getRegularHours());
            w.put("overtimeHours", a.getOvertimeHours());
            w.put("productivity", a.getActualWorkHours() != null && a.getActualWorkHours() > 0
                    ? Math.round((a.getActualWorkHours() > 0 ? a.getActualWorkHours() : 0) * 10.0) / 10.0
                    : null);
            if (a.getProductionOrder() != null) {
                w.put("orderId", a.getProductionOrder().getId().toString());
                w.put("orderTitle", a.getProductionOrder().getTitle());
            }
            if (a.getCheckOutTime() != null) {
                checkedOut.add(w);
            } else {
                checkedIn.add(w);
            }
        }

        double totalHours = checkedOut.stream()
                .mapToDouble(w -> {
                    Double h = (Double) w.get("actualWorkHours");
                    return h != null ? h : 0;
                })
                .sum();

        Map<String, Double> stageHours = new LinkedHashMap<>();
        stageHours.put("RANG", 0.0);
        stageHours.put("RANH_VA_CHON", 0.0);
        stageHours.put("XAY", 0.0);
        stageHours.put("DONG_GOI", 0.0);
        stageHours.put("QA", 0.0);
        for (Attendance a : attendances) {
            if (a.getStage() != null && a.getCheckOutTime() != null) {
                double hours = a.getRegularHours() + a.getOvertimeHours();
                stageHours.merge(a.getStage().name(), hours, Double::sum);
            }
        }


```
