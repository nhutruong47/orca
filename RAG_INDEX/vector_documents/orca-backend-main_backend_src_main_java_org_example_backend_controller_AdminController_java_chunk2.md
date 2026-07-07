# Knowledge Document: AdminController.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/AdminController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "authentication",
    "admin",
    "payment",
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
- **Tags**: subscription, authentication, admin, payment, security

## Source Code Chunk
```java
   }

    @DeleteMapping("/teams/{id}")
    public ResponseEntity<Void> deleteTeam(@PathVariable UUID id) {
        adminService.deleteTeam(id);
        return ResponseEntity.ok().build();
    }

    @PatchMapping("/teams/{id}/publication")
    public ResponseEntity<Map<String, Object>> updateTeamPublication(
            @PathVariable UUID id,
            @RequestBody Map<String, Boolean> body) {
        return ResponseEntity.ok(adminService.updateTeamPublication(id, Boolean.TRUE.equals(body.get("published"))));
    }

    @PatchMapping("/teams/{id}/verification")
    public ResponseEntity<Map<String, Object>> updateTeamVerification(
            @PathVariable UUID id,
            @RequestBody Map<String, String> body) {
        return ResponseEntity.ok(adminService.updateTeamVerification(id, body.get("status"), body.get("rejectReason")));
    }

    @PatchMapping("/tasks/{id}/status")
    public ResponseEntity<Map<String, Object>> updateTaskStatus(
            @PathVariable UUID id,
            @RequestBody Map<String, String> body) {
        return ResponseEntity.ok(adminService.updateTaskStatus(id, body.get("status")));
    }

    @GetMapping("/plans")
    public ResponseEntity<List<SubscriptionPlan>> getPlans() {
        return ResponseEntity.ok(adminService.getPlans());
    }

    @PostMapping("/plans")
    public ResponseEntity<SubscriptionPlan> createPlan(@RequestBody SubscriptionPlan plan) {
        return ResponseEntity.ok(adminService.createPlan(plan));
    }

    @PutMapping("/plans/{id}")
    public ResponseEntity<SubscriptionPlan> updatePlan(
            @PathVariable UUID id,
            @RequestBody SubscriptionPlan plan) {
        return ResponseEntity.ok(adminService.updatePlan(id, plan));
    }

    @DeleteMapping("/plans/{id}")
    public ResponseEntity<Void> deletePlan(@PathVariable UUID id) {
        adminService.deletePlan(id);
        return ResponseEntity.ok().build();
    }

    @GetMapping("/ai-configs")
    public ResponseEntity<Map<String, String>> getAiConfigs() {
        return ResponseEntity.ok(adminService.getAiConfigs());
    }

    @PutMapping("/ai-configs")
    public ResponseEntity<Void> updateAiConfigs(@RequestBody Map<String, String> configs) {
        adminService.updateAiConfigs(configs);
        return ResponseEntity.ok().build();
    }
}

```
