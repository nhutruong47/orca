# Knowledge Document: ProductionBoardService.java (Chunk 6/6)

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
  "chunk_index": 5,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
       stageHours.put("XAY", 0.0);
        stageHours.put("DONG_GOI", 0.0);
        stageHours.put("QA", 0.0);
        for (Attendance a : attendances) {
            if (a.getStage() != null && a.getCheckOutTime() != null) {
                double hours = a.getRegularHours() + a.getOvertimeHours();
                stageHours.merge(a.getStage().name(), hours, Double::sum);
            }
        }

        List<Map<String, Object>> lateWorkers = attendances.stream()
                .filter(a -> "LATE".equals(a.getAttendanceStatus() != null ? a.getAttendanceStatus().name() : null))
                .map(a -> {
                    Map<String, Object> w = new LinkedHashMap<>();
                    w.put("userId", a.getUser().getId().toString());
                    w.put("userName", a.getUser().getFullName());
                    w.put("checkInTime", a.getCheckInTime());
                    return w;
                })
                .collect(Collectors.toList());

        long notCheckedOut = attendances.stream().filter(a -> a.getCheckOutTime() == null).count();

        result.put("totalWorkers", attendances.size());
        result.put("checkedIn", checkedIn);
        result.put("checkedOut", checkedOut);
        result.put("totalWorkHours", Math.round(totalHours * 10.0) / 10.0);
        result.put("stageHours", stageHours);
        result.put("lateWorkers", lateWorkers);
        result.put("notCheckedOut", notCheckedOut);
        result.put("activeOrders", activeOrders.stream().limit(5).map(o -> {
            Map<String, Object> m = new LinkedHashMap<>();
            m.put("id", o.getId().toString());
            m.put("title", o.getTitle());
            m.put("progressPercent", o.getProgressPercent());
            m.put("remainingQuantity", o.getRemainingQuantity());
            return m;
        }).collect(Collectors.toList()));

        return result;
    }
}

```
