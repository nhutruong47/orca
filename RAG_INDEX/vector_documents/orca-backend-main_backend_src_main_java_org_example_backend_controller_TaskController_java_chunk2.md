# Knowledge Document: TaskController.java (Chunk 3/7)

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
  "chunk_index": 2,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, authentication, security

## Source Code Chunk
```java
));
        }
    }

    @PatchMapping("/{id}/status")
    public ResponseEntity<?> updateStatus(@PathVariable UUID id, @RequestBody Map<String, String> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.updateStatus(id, body.get("status")));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PatchMapping("/{id}/progress")
    public ResponseEntity<?> updateProgress(@PathVariable UUID id, @RequestBody Map<String, Integer> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.updateProgress(id, body.get("percentage")));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PatchMapping("/{id}/workload")
    public ResponseEntity<?> updateWorkload(@PathVariable UUID id, @RequestBody Map<String, Double> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.updateWorkload(id, body.get("actualWorkload")));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PatchMapping("/{id}/assign")
    public ResponseEntity<?> assign(@PathVariable UUID id, @RequestBody Map<String, String> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.assign(id, UUID.fromString(body.get("memberId"))));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PatchMapping("/{id}/backup")
    public ResponseEntity<?> setBackup(@PathVariable UUID id, @RequestBody Map<String, String> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.setBackup(id, UUID.fromString(body.get("memberId"))));
        } catch (RuntimeException e) {

```
