# Knowledge Document: TeamController.java (Chunk 3/3)

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
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, authentication, security

## Source Code Chunk
```java
UUID userId,
            @RequestBody Map<String, List<String>> body,
            Authentication auth) {
        List<String> labels = body.getOrDefault("labels", List.of());
        List<String> updatedLabels = teamService.updateMemberLabels(teamId, userId, labels, auth.getName());
        return ResponseEntity.ok(updatedLabels);
    }

    /** Xóa nhóm (chỉ Owner) */
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteTeam(@PathVariable UUID id, Authentication auth) {
        teamService.deleteTeam(id, auth.getName());
        return ResponseEntity.ok().build();
    }

    /** Bật quảng cáo (Publish) */
    @PutMapping("/{id}/advertise")
    public ResponseEntity<TeamDTO> advertiseTeam(
            @PathVariable UUID id,
            @RequestBody TeamDTO dto,
            Authentication auth) {
        return ResponseEntity.ok(teamService.advertiseTeam(id, dto, auth.getName()));
    }

    /** Tắt quảng cáo (Unpublish) */
    @PutMapping("/{id}/unpublish")
    public ResponseEntity<Void> unpublishTeam(@PathVariable UUID id, Authentication auth) {
        teamService.unpublishTeam(id, auth.getName());
        return ResponseEntity.ok().build();
    }

    /** Gá»­i há»“ sÆ¡ xÃ¡c minh xÆ°á»Ÿng cho Admin duyá»‡t */
    @PutMapping("/{id}/verification")
    public ResponseEntity<?> submitVerification(
            @PathVariable UUID id,
            @RequestBody TeamDTO dto,
            Authentication auth) {
        try {
            return ResponseEntity.ok(teamService.submitVerification(id, dto, auth.getName()));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }
}

```
