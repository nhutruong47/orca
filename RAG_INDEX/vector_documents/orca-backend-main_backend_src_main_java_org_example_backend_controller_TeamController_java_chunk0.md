# Knowledge Document: TeamController.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/TeamController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "factory",
  "tags": [
    "factory",
    "admin",
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
- **Tags**: factory, admin, authentication, security

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.dto.TeamDTO;
import org.example.backend.service.TeamService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/teams")
public class TeamController {

    @Autowired
    private TeamService teamService;

    /** Lấy danh sách nhóm của user hiện tại */
    @GetMapping
    public ResponseEntity<?> getMyTeams(Authentication auth) {
        try {
            return ResponseEntity.ok(teamService.getTeamsForUser(auth.getName()));
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.badRequest().body(Map.of("error", e.getClass().getSimpleName() + ": " + e.getMessage()));
        }
    }

    /** Lấy danh sách tất cả các nhóm (cho Marketplace) */
    @GetMapping("/all")
    public ResponseEntity<List<TeamDTO>> getAllTeams() {
        return ResponseEntity.ok(teamService.getAllTeams());
    }

    /** Xem chi tiết nhóm */
    @GetMapping("/{id}")
    public ResponseEntity<TeamDTO> getTeamDetail(@PathVariable UUID id) {
        return ResponseEntity.ok(teamService.getTeamDetail(id));
    }

    /** Tạo nhóm mới */
    @PostMapping
    public ResponseEntity<TeamDTO> createTeam(@RequestBody TeamDTO dto, Authentication auth) {
        return ResponseEntity.ok(teamService.createTeam(dto, auth.getName()));
    }

    @PutMapping("/{id}")
    public ResponseEntity<?> updateTeam(@PathVariable UUID id, @RequestBody TeamDTO dto, Authentication auth) {
        try {
            return ResponseEntity.ok(teamService.updateTeam(id, dto, auth.getName()));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    /** Tham gia nhóm bằng Invite Code */
    @PostMapping("/join")
    public ResponseEntity<?> joinByCode(@RequestBody Map<String, String> body, Authentication auth) {
        String code = body.get("inviteCode");
        if (code == null || code.isBlank()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Mã mời không được để trống"));
        }
        try {

```
