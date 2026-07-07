# Knowledge Document: AttendanceController.java (Chunk 2/3)

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
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: production, attendance, authentication, security

## Source Code Chunk
```java
ProductionStage.valueOf(body.get("stage").toString());
                }
                if (body.get("orderId") != null) {
                    orderId = UUID.fromString(body.get("orderId").toString());
                }
                if (body.get("breakMinutes") != null) {
                    breakMinutes = Integer.parseInt(body.get("breakMinutes").toString());
                }
            }

            AttendanceDTO dto = attendanceService.checkIn(userId, teamId, shiftType, stage, orderId, breakMinutes);
            return ResponseEntity.ok(dto);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/check-out/{teamId}")
    public ResponseEntity<?> checkOut(
            @PathVariable UUID teamId,
            @AuthenticationPrincipal User currentUser) {
        accessControlService.requireTeamMember(currentUser, teamId);
        UUID userId = currentUser.getId();
        try {
            return ResponseEntity.ok(attendanceService.checkOut(userId, teamId));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/today/{teamId}")
    public ResponseEntity<?> getTodayAttendance(
            @PathVariable UUID teamId,
            @AuthenticationPrincipal User currentUser) {
        accessControlService.requireTeamMember(currentUser, teamId);
        UUID userId = currentUser.getId();
        AttendanceDTO dto = attendanceService.getTodayAttendance(userId, teamId);
        if (dto != null) {
            return ResponseEntity.ok(dto);
        }
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/history/{teamId}")
    public ResponseEntity<?> getAttendanceHistory(
            @PathVariable UUID teamId,
            @AuthenticationPrincipal User currentUser) {
        accessControlService.requireTeamMember(currentUser, teamId);
        UUID userId = currentUser.getId();
        return ResponseEntity.ok(attendanceService.getAttendanceHistory(userId, teamId));
    }

    @GetMapping("/team-today/{teamId}")
    public ResponseEntity<?> getTeamAttendanceToday(@PathVariable UUID teamId, @AuthenticationPrincipal User currentUser) {
        accessControlService.requireTeamMember(currentUser, teamId);

```
