# Knowledge Document: AttendanceController.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/AttendanceController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "production",
  "tags": [
    "production",
    "attendance",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: production, attendance, authentication, security

## Source Code Chunk
```java
mber(currentUser, teamId);
        UUID userId = currentUser.getId();
        return ResponseEntity.ok(attendanceService.getAttendanceHistory(userId, teamId));
    }

    @GetMapping("/team-today/{teamId}")
    public ResponseEntity<?> getTeamAttendanceToday(@PathVariable UUID teamId, @AuthenticationPrincipal User currentUser) {
        accessControlService.requireTeamMember(currentUser, teamId);
        return ResponseEntity.ok(attendanceService.getTeamAttendanceToday(teamId));
    }

    @GetMapping("/team-history/{teamId}")
    public ResponseEntity<?> getTeamAttendanceHistory(@PathVariable UUID teamId, @AuthenticationPrincipal User currentUser) {
        accessControlService.requireTeamMember(currentUser, teamId);
        return ResponseEntity.ok(attendanceService.getTeamAttendanceHistory(teamId));
    }

    @PutMapping("/update/{attendanceId}")
    public ResponseEntity<?> updateAttendance(
            @PathVariable UUID attendanceId,
            @AuthenticationPrincipal User currentUser,
            @RequestBody UpdateAttendanceRequest req) {
        accessControlService.requireAttendanceAccess(currentUser, attendanceId);
        try {
            return ResponseEntity.ok(attendanceService.updateAttendance(attendanceId, req));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/stages")
    public ResponseEntity<?> getProductionStages() {
        return ResponseEntity.ok(Attendance.ProductionStage.values());
    }

    @GetMapping("/shifts")
    public ResponseEntity<?> getShiftTypes() {
        return ResponseEntity.ok(Attendance.ShiftType.values());
    }
}

```
