# Knowledge Document: AttendanceController.java (Chunk 1/3)

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
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: production, attendance, authentication, security

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.dto.AttendanceDTO;
import org.example.backend.dto.UpdateAttendanceRequest;
import org.example.backend.entity.Attendance;
import org.example.backend.entity.User;
import org.example.backend.service.AccessControlService;
import org.example.backend.service.AttendanceService;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/attendance")
@CrossOrigin("*")
public class AttendanceController {

    private final AttendanceService attendanceService;
    private final AccessControlService accessControlService;

    public AttendanceController(AttendanceService attendanceService, AccessControlService accessControlService) {
        this.attendanceService = attendanceService;
        this.accessControlService = accessControlService;
    }

    @PostMapping("/check-in/{teamId}")
    public ResponseEntity<?> checkIn(
            @PathVariable UUID teamId,
            @AuthenticationPrincipal User currentUser,
            @RequestBody(required = false) Map<String, Object> body) {

        accessControlService.requireTeamMember(currentUser, teamId);
        UUID userId = currentUser.getId();
        try {
            Attendance.ShiftType shiftType = Attendance.ShiftType.SANG;
            Attendance.ProductionStage stage = null;
            UUID orderId = null;
            Integer breakMinutes = 30;

            if (body != null) {
                if (body.get("shiftType") != null) {
                    shiftType = Attendance.ShiftType.valueOf(body.get("shiftType").toString());
                }
                if (body.get("stage") != null) {
                    stage = Attendance.ProductionStage.valueOf(body.get("stage").toString());
                }
                if (body.get("orderId") != null) {
                    orderId = UUID.fromString(body.get("orderId").toString());
                }
                if (body.get("breakMinutes") != null) {
                    breakMinutes = Integer.parseInt(body.get("breakMinutes").toString());
                }
            }


```
