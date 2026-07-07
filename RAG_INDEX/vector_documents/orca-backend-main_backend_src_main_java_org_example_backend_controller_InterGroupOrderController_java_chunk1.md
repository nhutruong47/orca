# Knowledge Document: InterGroupOrderController.java (Chunk 2/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/InterGroupOrderController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "factory",
  "tags": [
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
{
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{orderId}")
    public ResponseEntity<?> getOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            return ResponseEntity.ok(orderService.getById(orderId));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{orderId}/accept")
    public ResponseEntity<?> acceptOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            return ResponseEntity.ok(orderService.acceptOrder(orderId, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{orderId}/reject")
    public ResponseEntity<?> rejectOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            return ResponseEntity.ok(orderService.rejectOrder(orderId, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{orderId}/cancel")
    public ResponseEntity<?> cancelOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            return ResponseEntity.ok(orderService.cancelOrder(orderId, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{orderId}/approve-cancel")
    public ResponseEntity<?> approveCancelOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            return ResponseEntity.ok(orderService.approveCancelOrder(orderId, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }


```
