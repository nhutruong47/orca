# Knowledge Document: TeamController.java (Chunk 2/3)

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
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, authentication, security

## Source Code Chunk
```java
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
            TeamDTO team = teamService.joinByCode(code, auth.getName());
            return ResponseEntity.ok(team);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/members")
    public ResponseEntity<Map<String, String>> addMember(
            @PathVariable UUID id,
            @RequestBody Map<String, String> body,
            Authentication auth) {
        String email = body.get("email");
        if (email == null || email.isBlank()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Email is required"));
        }
        try {
            Map<String, String> result = teamService.addMemberByEmail(id, email, auth.getName());
            return ResponseEntity.ok(result);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    /** Xóa thành viên (chỉ Owner) */
    @DeleteMapping("/{teamId}/members/{userId}")
    public ResponseEntity<Void> removeMember(
            @PathVariable UUID teamId,
            @PathVariable UUID userId,
            Authentication auth) {
        teamService.removeMember(teamId, userId, auth.getName());
        return ResponseEntity.ok().build();
    }

    /** Cập nhật nhãn công việc của thành viên */
    @PutMapping("/{teamId}/members/{userId}/labels")
    public ResponseEntity<List<String>> updateMemberLabels(
            @PathVariable UUID teamId,
            @PathVariable UUID userId,
            @RequestBody Map<String, List<String>> body,
            Authentication auth) {
        List<String> labels = body.getOrDefault("labels", List.of());
        List<String> updatedLabels = teamService.updateMemberLabels(teamId, userId, labels, auth.getName());
        return ResponseEntity.ok(updatedLabels);
    }

    /** Xóa nhóm (chỉ Owner) */
    @DeleteMapping("/{id}")

```
