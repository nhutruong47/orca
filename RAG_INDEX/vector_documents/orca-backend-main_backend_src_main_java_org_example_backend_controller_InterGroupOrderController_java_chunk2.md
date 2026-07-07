# Knowledge Document: InterGroupOrderController.java (Chunk 3/5)

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
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
veCancelOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            return ResponseEntity.ok(orderService.approveCancelOrder(orderId, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{orderId}/reject-cancel")
    public ResponseEntity<?> rejectCancelOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            return ResponseEntity.ok(orderService.rejectCancelOrder(orderId, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    /**
     * Seller transitions the order from CONFIRMED -> SHIPPING.
     */
    @PatchMapping("/{orderId}/ship")
    public ResponseEntity<?> shipOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            return ResponseEntity.ok(orderService.shipOrder(orderId, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    /**
     * Seller transitions the order from CONFIRMED -> SHIPPING -> DELIVERED.
     * Validation: only the seller (receiving team owner) can mark delivered.
     */
    @PatchMapping("/{orderId}/deliver")
    public ResponseEntity<?> deliverOrder(@PathVariable UUID orderId,
                                          @RequestBody(required = false) Map<String, Object> payload,
                                          @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            String deliveryNote = payload != null && payload.get("deliveryNote") != null
                    ? payload.get("deliveryNote").toString() : null;
            return ResponseEntity.ok(orderService.deliverOrder(orderId, deliveryNote, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    /**

```
