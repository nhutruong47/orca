# Knowledge Document: AttendanceService.java (Chunk 5/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AttendanceService.java",
  "language": "java",
  "module": "service",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Service",
  "chunk_index": 4,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
!= null)
                .collect(Collectors.groupingBy(
                        a -> a.getStage().name(),
                        Collectors.summingDouble(a -> a.getRegularHours() + a.getOvertimeHours())
                ));
    }

    public Double getOrderWorkerHours(UUID orderId) {
        List<Attendance> attendances = attendanceRepo.findByOrderId(orderId);
        return attendances.stream()
                .mapToDouble(a -> a.getRegularHours() + a.getOvertimeHours())
                .sum();
    }

    private AttendanceDTO toDTO(Attendance a) {
        AttendanceDTO dto = new AttendanceDTO();
        dto.setId(a.getId().toString());
        dto.setUserId(a.getUser().getId().toString());
        dto.setUserName(a.getUser().getFullName());
        dto.setTeamId(a.getTeam().getId().toString());
        dto.setDate(a.getDate());
        dto.setShiftType(a.getShiftType() != null ? a.getShiftType().name() : null);
        dto.setShiftStartTime(a.getShiftStartTime());
        dto.setShiftEndTime(a.getShiftEndTime());
        dto.setCheckInTime(a.getCheckInTime());
        dto.setCheckOutTime(a.getCheckOutTime());
        dto.setProductionStage(a.getStage() != null ? a.getStage().name() : null);
        if (a.getProductionOrder() != null) {
            dto.setOrderId(a.getProductionOrder().getId().toString());
            dto.setOrderTitle(a.getProductionOrder().getTitle());
        }
        dto.setBreakMinutes(a.getBreakMinutes());
        dto.setActualWorkHours(a.getActualWorkHours());
        dto.setRegularHours(a.getRegularHours());
        dto.setOvertimeHours(a.getOvertimeHours());
        dto.setAttendanceStatus(a.getAttendanceStatus() != null ? a.getAttendanceStatus().name() : null);
        dto.setNotes(a.getNotes());
        return dto;
    }
}

```
