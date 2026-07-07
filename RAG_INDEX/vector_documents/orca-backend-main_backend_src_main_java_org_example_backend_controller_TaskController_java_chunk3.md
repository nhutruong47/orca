# Knowledge Document: TaskController.java (Chunk 4/7)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/TaskController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 3,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, authentication, security

## Source Code Chunk
```java

    }

    @PatchMapping("/{id}/backup")
    public ResponseEntity<?> setBackup(@PathVariable UUID id, @RequestBody Map<String, String> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.setBackup(id, UUID.fromString(body.get("memberId"))));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PatchMapping("/{id}/supervisor")
    public ResponseEntity<?> setSupervisor(@PathVariable UUID id, @RequestBody Map<String, String> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.setSupervisor(id, UUID.fromString(body.get("memberId"))));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PatchMapping("/{id}/transfer")
    public ResponseEntity<?> transfer(@PathVariable UUID id, @RequestBody Map<String, Object> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            String toMemberId = body.get("toMemberId") != null ? body.get("toMemberId").toString() : null;
            String reason = body.get("reason") != null ? body.get("reason").toString() : null;
            String actorType = body.get("actorType") != null ? body.get("actorType").toString() : null;
            return ResponseEntity.ok(taskService.transferTask(id, UUID.fromString(toMemberId), reason, actorType, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{id}/transfers")
    public ResponseEntity<?> getTransfers(@PathVariable UUID id, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.getTransfers(id));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/dependencies")

```
