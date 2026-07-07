# Knowledge Document: AttendanceService.java (Chunk 3/5)

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
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
tActualWorkHours(actualWorkHours);

        double regularHours = Math.min(actualWorkHours, 8.0);
        double overtimeHours = Math.max(0, actualWorkHours - 8.0);
        a.setRegularHours(Math.round(regularHours * 10.0) / 10.0);
        a.setOvertimeHours(Math.round(overtimeHours * 10.0) / 10.0);

        if (a.getShiftType() != null) {
            String expectedStart = a.getShiftStartTime();
            if (expectedStart != null) {
                int expectedHour = Integer.parseInt(expectedStart.split(":")[0]);
                int actualHour = a.getCheckInTime().getHour();
                if (actualHour > expectedHour) {
                    a.setAttendanceStatus(Attendance.AttendanceStatus.LATE);
                } else {
                    a.setAttendanceStatus(Attendance.AttendanceStatus.ON_TIME);
                }
            } else {
                a.setAttendanceStatus(Attendance.AttendanceStatus.ON_TIME);
            }
        } else {
            a.setAttendanceStatus(Attendance.AttendanceStatus.ON_TIME);
        }

        return toDTO(attendanceRepo.save(a));
    }

    public AttendanceDTO getTodayAttendance(UUID userId, UUID teamId) {
        LocalDate today = LocalDate.now();
        return attendanceRepo.findByUserIdAndTeamIdAndDate(userId, teamId, today)
                .map(this::toDTO)
                .orElse(null);
    }

    public List<AttendanceDTO> getAttendanceHistory(UUID userId, UUID teamId) {
        return attendanceRepo.findByUserIdAndTeamId(userId, teamId).stream()
                .sorted((a, b) -> b.getDate().compareTo(a.getDate()))
                .map(this::toDTO)
                .collect(Collectors.toList());
    }

    public List<AttendanceDTO> getTeamAttendanceToday(UUID teamId) {
        LocalDate today = LocalDate.now();
        return attendanceRepo.findByTeamIdAndDate(teamId, today).stream()
                .map(this::toDTO)
                .collect(Collectors.toList());
    }

    public List<AttendanceDTO> getTeamAttendanceHistory(UUID teamId) {
        return attendanceRepo.findByTeamId(teamId).stream()
                .sorted((a, b) -> b.getDate().compareTo(a.getDate()))
                .map(this::toDTO)
                .collect(Collectors.toList());
    }

    public AttendanceDTO updateAttendance(UUID attendanceId, UpdateAttendanceRequest req) {
        Attendance a = attendanceRepo.findById(attendanceId)

```
