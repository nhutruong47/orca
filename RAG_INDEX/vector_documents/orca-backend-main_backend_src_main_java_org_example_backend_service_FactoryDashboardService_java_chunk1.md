# Knowledge Document: FactoryDashboardService.java (Chunk 2/6)

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
  "chunk_index": 1,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, attendance, production, dashboard

## Source Code Chunk
```java
 Object>> activeOrdersData = activeOrders.stream()
                .limit(10)
                .map(o -> {
                    Map<String, Object> m = new LinkedHashMap<>();
                    m.put("id", o.getId().toString());
                    m.put("orderCode", o.getOrderCode());
                    m.put("title", o.getTitle());
                    m.put("customerName", o.getCustomerName());
                    m.put("outputTarget", o.getOutputTarget());
                    m.put("completedQuantity", o.getCompletedQuantity());
                    m.put("remainingQuantity", o.getRemainingQuantity());
                    m.put("progressPercent", o.getProgressPercent());
                    m.put("internalDeadline", o.getInternalDeadline());
                    m.put("customerDeliveryDate", o.getCustomerDeliveryDate());
                    m.put("status", o.getStatus());
                    m.put("productType", o.getProductType());
                    m.put("isAtRisk", isAtRisk(o));
                    return m;
                })
                .collect(Collectors.toList());

        List<Attendance> todayAttendances = attendanceRepo.findByTeamIdAndDate(teamId, today);
        List<Map<String, Object>> staffData = todayAttendances.stream()
                .map(a -> {
                    Map<String, Object> m = new LinkedHashMap<>();
                    m.put("userId", a.getUser().getId().toString());
                    m.put("userName", a.getUser().getFullName());
                    m.put("shiftType", a.getShiftType() != null ? a.getShiftType().name() : null);
                    m.put("stage", a.getStage() != null ? a.getStage().name() : null);
                    m.put("checkInTime", a.getCheckInTime());
                    m.put("checkOutTime", a.getCheckOutTime());
                    m.put("workHours", a.getActualWorkHours() != null ? a.getActualWorkHours()
                            : (a.getRegularHours() + a.getOvertimeHours()));
                    m.put("attendanceStatus", a.getAttendanceStatus() != null ? a.getAttendanceStatus().name() : null);
                    if (a.getProductionOrder() != null) {
                        m.put("orderTitle", a.getProductionOrder().getTitle());
                    }
                    return m;
                })
                .collect(Collectors.toList());


```
