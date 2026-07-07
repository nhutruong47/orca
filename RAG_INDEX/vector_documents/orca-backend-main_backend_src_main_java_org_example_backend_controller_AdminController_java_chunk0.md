# Knowledge Document: AdminController.java (Chunk 1/3)

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
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, authentication, admin, payment, security

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.entity.User;
import org.example.backend.entity.SubscriptionPlan;
import org.example.backend.service.AdminService;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/admin")
@PreAuthorize("hasRole('ADMIN')")
public class AdminController {

    private final AdminService adminService;

    public AdminController(AdminService adminService) {
        this.adminService = adminService;
    }

    @GetMapping("/overview")
    public ResponseEntity<Map<String, Object>> getOverview() {
        return ResponseEntity.ok(adminService.getOverview());
    }

    @GetMapping("/users")
    public ResponseEntity<List<Map<String, Object>>> getUsers() {
        return ResponseEntity.ok(adminService.getUsers());
    }

    @GetMapping("/teams")
    public ResponseEntity<List<Map<String, Object>>> getTeams() {
        return ResponseEntity.ok(adminService.getTeams());
    }

    @GetMapping("/orders")
    public ResponseEntity<List<Map<String, Object>>> getOrders() {
        return ResponseEntity.ok(adminService.getOrders());
    }

    @GetMapping("/tasks")
    public ResponseEntity<List<Map<String, Object>>> getTasks() {
        return ResponseEntity.ok(adminService.getTasks());
    }

    @GetMapping("/payments")
    public ResponseEntity<List<Map<String, Object>>> getPayments() {
        return ResponseEntity.ok(adminService.getPayments());
    }

    @PostMapping("/users")
    public ResponseEntity<Map<String, Object>> createUser(@RequestBody Map<String, String> body) {

```
