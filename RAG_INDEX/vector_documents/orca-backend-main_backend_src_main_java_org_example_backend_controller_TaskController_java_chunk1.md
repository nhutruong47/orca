# Knowledge Document: TaskController.java (Chunk 2/7)

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
  "chunk_index": 1,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, authentication, security

## Source Code Chunk
```java
tity<?> getMyKpi(@AuthenticationPrincipal User user) {
        return ResponseEntity.ok(taskService.getMemberKpi(user.getId()));
    }

    @GetMapping("/member/{memberId}")
    public ResponseEntity<?> getByMember(@PathVariable UUID memberId, @AuthenticationPrincipal User user) {
        return ResponseEntity.ok(taskService.getByMember(memberId));
    }

    @GetMapping("/member/{memberId}/kpi")
    public ResponseEntity<?> getMemberKpi(@PathVariable UUID memberId, @AuthenticationPrincipal User user) {
        return ResponseEntity.ok(taskService.getMemberKpi(memberId));
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getTaskDetail(@PathVariable UUID id, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.getById(id));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping
    public ResponseEntity<?> create(@RequestBody TaskDTO dto, @AuthenticationPrincipal User user) {
        try {
            if (dto != null && dto.getGoalId() != null) {
                accessControlService.requireGoalAccess(user, UUID.fromString(dto.getGoalId()));
            }
            return ResponseEntity.ok(taskService.create(dto));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PatchMapping("/{id}")
    public ResponseEntity<?> updateTask(@PathVariable UUID id, @RequestBody Map<String, Object> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.update(id, body));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PatchMapping("/{id}/status")
    public ResponseEntity<?> updateStatus(@PathVariable UUID id, @RequestBody Map<String, String> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.updateStatus(id, body.get("status")));
        } catch (RuntimeException e) {

```
