# Knowledge Document: ProductionOrderController.java (Chunk 2/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/ProductionOrderController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "production",
  "tags": [
    "production",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: production, authentication, security

## Source Code Chunk
```java
ControlService.requireTeamMember(user, teamId);
        try {
            ProductionOrder raw = mapToOrder(body);
            ProductionOrder created = orderService.createOrder(teamId, raw);
            return ResponseEntity.ok(orderService.toDTO(created));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/orders/{orderId}")
    public ResponseEntity<?> getOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {
        accessControlService.requireProductionOrderAccess(user, orderId);
        try {
            ProductionOrder order = orderService.getById(orderId);
            return ResponseEntity.ok(orderService.toDTO(order));
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }

    @PatchMapping("/orders/{orderId}")
    public ResponseEntity<?> updateOrder(
            @PathVariable UUID orderId,
            @AuthenticationPrincipal User user,
            @RequestBody Map<String, Object> body) {
        accessControlService.requireProductionOrderAccess(user, orderId);
        try {
            ProductionOrder raw = mapToOrder(body);
            raw.setStatus(getString(body, "status"));
            ProductionOrder updated = orderService.updateOrder(orderId, raw);
            return ResponseEntity.ok(orderService.toDTO(updated));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PatchMapping("/orders/{orderId}/status")
    public ResponseEntity<?> updateStatus(
            @PathVariable UUID orderId,
            @AuthenticationPrincipal User user,
            @RequestBody Map<String, String> body) {
        accessControlService.requireProductionOrderAccess(user, orderId);
        try {
            ProductionOrder updated = orderService.updateStatus(orderId, body.get("status"));
            return ResponseEntity.ok(orderService.toDTO(updated));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @DeleteMapping("/orders/{orderId}")
    public ResponseEntity<?> deleteOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {

```
