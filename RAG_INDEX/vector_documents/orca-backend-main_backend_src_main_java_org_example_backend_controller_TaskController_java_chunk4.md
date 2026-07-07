# Knowledge Document: TaskController.java (Chunk 5/7)

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
  "chunk_index": 4,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, authentication, security

## Source Code Chunk
```java
 getTransfers(@PathVariable UUID id, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.getTransfers(id));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/dependencies")
    public ResponseEntity<?> addDependency(@PathVariable UUID id, @RequestBody Map<String, Object> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            String dependsOnTaskId = body.get("dependsOnTaskId") != null ? body.get("dependsOnTaskId").toString() : null;
            String type = body.get("dependencyType") != null ? body.get("dependencyType").toString() : "FINISH_TO_START";
            return ResponseEntity.ok(taskService.addDependency(id, UUID.fromString(dependsOnTaskId), type));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{id}/dependencies")
    public ResponseEntity<?> getDependencies(@PathVariable UUID id, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.getDependencies(id));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    // === Checklist (canonical) ===
    @GetMapping("/{id}/checklists")
    public ResponseEntity<?> getChecklist(@PathVariable UUID id, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.getChecklist(id));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }



    @PostMapping("/{id}/checklists")
    public ResponseEntity<?> addChecklistItem(@PathVariable UUID id, @RequestBody Map<String, String> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.addChecklistItem(id, body.get("content")));

```
