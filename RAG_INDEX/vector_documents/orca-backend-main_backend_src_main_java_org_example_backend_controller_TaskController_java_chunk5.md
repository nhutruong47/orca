# Knowledge Document: TaskController.java (Chunk 6/7)

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
  "chunk_index": 5,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, authentication, security

## Source Code Chunk
```java
f("error", e.getMessage()));
        }
    }



    @PostMapping("/{id}/checklists")
    public ResponseEntity<?> addChecklistItem(@PathVariable UUID id, @RequestBody Map<String, String> body, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            return ResponseEntity.ok(taskService.addChecklistItem(id, body.get("content")));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    // Frontend uses /checklist/ (singular) + PATCH .../toggle
    @PatchMapping("/checklists/{checklistId}/toggle")
    public ResponseEntity<?> toggleChecklist(@PathVariable UUID checklistId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireChecklistAccess(user, checklistId);
            taskService.toggleChecklistItem(checklistId);
            return ResponseEntity.ok(Map.of("message", "Toggled"));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }



    @PatchMapping("/{id}/respond")
    public ResponseEntity<?> respondToTask(@PathVariable UUID id,
            @AuthenticationPrincipal User user,
            @RequestBody Map<String, Boolean> body) {
        try {
            boolean accepted = Boolean.TRUE.equals(body.get("accepted"));
            return ResponseEntity.ok(taskService.respondToTask(id, user.getId(), accepted));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/salary/{teamId}")
    public ResponseEntity<?> getSalaryReport(@PathVariable UUID teamId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTeamMember(user, teamId);
            return ResponseEntity.ok(taskService.getSalaryReport(teamId));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/salary/{teamId}/export-excel")
    public ResponseEntity<byte[]> exportSalaryExcel(@PathVariable UUID teamId, @AuthenticationPrincipal User user) throws Exception {
        accessControlService.requireTeamMember(user, teamId);

```
