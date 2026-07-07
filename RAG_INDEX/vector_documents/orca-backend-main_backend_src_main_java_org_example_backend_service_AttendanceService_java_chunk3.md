# Knowledge Document: AttendanceService.java (Chunk 4/5)

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
  "chunk_index": 3,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
ndanceHistory(UUID teamId) {
        return attendanceRepo.findByTeamId(teamId).stream()
                .sorted((a, b) -> b.getDate().compareTo(a.getDate()))
                .map(this::toDTO)
                .collect(Collectors.toList());
    }

    public AttendanceDTO updateAttendance(UUID attendanceId, UpdateAttendanceRequest req) {
        Attendance a = attendanceRepo.findById(attendanceId)
                .orElseThrow(() -> new RuntimeException("Attendance record not found"));
        
        if (req.getCheckInTime() != null) {
            a.setCheckInTime(req.getCheckInTime());
        }
        if (req.getCheckOutTime() != null) {
            a.setCheckOutTime(req.getCheckOutTime());
        }

        if (a.getCheckInTime() != null && a.getCheckOutTime() != null) {
            Duration workDuration = Duration.between(a.getCheckInTime(), a.getCheckOutTime());
            double totalMinutes = workDuration.toMinutes();
            double breakMins = a.getBreakMinutes() != null ? a.getBreakMinutes() : 30;
            double actualWorkMinutes = Math.max(0, totalMinutes - breakMins);
            double actualWorkHours = Math.round(actualWorkMinutes / 60.0 * 10.0) / 10.0;
            a.setActualWorkHours(actualWorkHours);

            double regularHours = Math.min(actualWorkHours, 8.0);
            double overtimeHours = Math.max(0, actualWorkHours - 8.0);
            a.setRegularHours(Math.round(regularHours * 10.0) / 10.0);
            a.setOvertimeHours(Math.round(overtimeHours * 10.0) / 10.0);
        } else {
            a.setActualWorkHours(0.0);
            a.setRegularHours(0.0);
            a.setOvertimeHours(0.0);
        }

        attendanceRepo.save(a);
        return toDTO(a);
    }

    public Map<String, Double> getStageWorkerHours(UUID teamId, LocalDate date) {
        List<Attendance> attendances = attendanceRepo.findByTeamIdAndDate(teamId, date);
        return attendances.stream()
                .filter(a -> a.getStage() != null)
                .collect(Collectors.groupingBy(
                        a -> a.getStage().name(),
                        Collectors.summingDouble(a -> a.getRegularHours() + a.getOvertimeHours())
                ));
    }

    public Double getOrderWorkerHours(UUID orderId) {
        List<Attendance> attendances = attendanceRepo.findByOrderId(orderId);
        return attendances.stream()

```
