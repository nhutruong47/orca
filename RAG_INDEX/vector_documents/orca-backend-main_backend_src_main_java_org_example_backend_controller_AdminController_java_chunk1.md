# Knowledge Document: AdminController.java (Chunk 2/3)

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
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, authentication, admin, payment, security

## Source Code Chunk
```java
<List<Map<String, Object>>> getTasks() {
        return ResponseEntity.ok(adminService.getTasks());
    }

    @GetMapping("/payments")
    public ResponseEntity<List<Map<String, Object>>> getPayments() {
        return ResponseEntity.ok(adminService.getPayments());
    }

    @PostMapping("/users")
    public ResponseEntity<Map<String, Object>> createUser(@RequestBody Map<String, String> body) {
        return ResponseEntity.ok(adminService.createUser(body));
    }

    @PutMapping("/users/{id}")
    public ResponseEntity<Map<String, Object>> updateUser(
            @PathVariable UUID id,
            @RequestBody Map<String, String> body) {
        return ResponseEntity.ok(adminService.updateUser(id, body));
    }

    @PostMapping("/users/{id}/reset-password")
    public ResponseEntity<Map<String, String>> resetUserPassword(@PathVariable UUID id) {
        String newPassword = adminService.resetUserPassword(id);
        return ResponseEntity.ok(Map.of("password", newPassword));
    }

    @PatchMapping("/users/{id}/role")
    public ResponseEntity<Map<String, Object>> updateUserRole(
            @PathVariable UUID id,
            @RequestBody Map<String, String> body,
            @AuthenticationPrincipal User currentUser) {
        return ResponseEntity.ok(adminService.updateUserRole(id, body.get("role"), currentUser));
    }

    @PatchMapping("/users/{id}/lock")
    public ResponseEntity<Map<String, Object>> updateUserLock(
            @PathVariable UUID id,
            @RequestBody Map<String, Boolean> body,
            @AuthenticationPrincipal User currentUser) {
        return ResponseEntity.ok(adminService.updateUserLock(id, Boolean.TRUE.equals(body.get("locked")), currentUser));
    }

    @PutMapping("/teams/{id}")
    public ResponseEntity<Map<String, Object>> updateTeam(
            @PathVariable UUID id,
            @RequestBody Map<String, String> body) {
        return ResponseEntity.ok(adminService.updateTeam(id, body));
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

```
