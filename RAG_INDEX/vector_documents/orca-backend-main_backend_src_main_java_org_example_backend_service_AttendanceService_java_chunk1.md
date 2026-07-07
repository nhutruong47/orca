# Knowledge Document: AttendanceService.java (Chunk 2/5)

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
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```java
ow();
        Optional<Attendance> existing = attendanceRepo.findByUserIdAndTeamIdAndDate(userId, teamId, today);
        if (existing.isPresent()) {
            throw new RuntimeException("Ban da check-in hom nay roi");
        }

        User user = userRepo.findById(userId)
                .orElseThrow(() -> new RuntimeException("User not found"));
        Team team = teamRepo.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        Attendance a = new Attendance();
        a.setUser(user);
        a.setTeam(team);
        a.setDate(today);
        a.setCheckInTime(LocalDateTime.now());
        a.setShiftType(shiftType);
        a.setStage(stage);
        a.setBreakMinutes(breakMinutes != null ? breakMinutes : 30);

        String[] hours = SHIFT_HOURS.get(shiftType);
        a.setShiftStartTime(hours[0]);
        a.setShiftEndTime(hours[1]);

        if (orderId != null) {
            ProductionOrder order = orderRepo.findById(orderId).orElse(null);
            a.setProductionOrder(order);
        }

        return toDTO(attendanceRepo.save(a));
    }

    public AttendanceDTO checkOut(UUID userId, UUID teamId) {
        LocalDate today = LocalDate.now();
        Attendance a = attendanceRepo.findByUserIdAndTeamIdAndDate(userId, teamId, today)
                .orElseThrow(() -> new RuntimeException("Ban chua check-in hom nay"));

        if (a.getCheckOutTime() != null) {
            throw new RuntimeException("Ban da check-out hom nay roi");
        }

        a.setCheckOutTime(LocalDateTime.now());

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

        if (a.getShiftType() != null) {
            String expectedStart = a.getShiftStartTime();

```
