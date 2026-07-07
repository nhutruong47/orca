# Knowledge Document: InterGroupOrderController.java (Chunk 4/5)

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
  "chunk_index": 3,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
          String deliveryNote = payload != null && payload.get("deliveryNote") != null
                    ? payload.get("deliveryNote").toString() : null;
            return ResponseEntity.ok(orderService.deliverOrder(orderId, deliveryNote, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    /**
     * Buyer confirms the delivery, transitioning DELIVERED -> COMPLETED.
     * Validation: only the buyer (owning team / personal buyer) can confirm.
     */
    @PatchMapping("/{orderId}/confirm-delivery")
    public ResponseEntity<?> confirmDelivery(@PathVariable UUID orderId,
                                             @RequestBody(required = false) Map<String, Object> payload,
                                             @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            String deliveryStatus = payload != null && payload.get("deliveryStatus") != null
                    ? payload.get("deliveryStatus").toString() : "ON_TIME";
            Integer rating = payload != null && payload.get("rating") instanceof Number
                    ? ((Number) payload.get("rating")).intValue() : 5;
            String comment = payload != null && payload.get("comment") != null
                    ? payload.get("comment").toString() : null;
            return ResponseEntity.ok(orderService.confirmDelivery(orderId, deliveryStatus, rating, comment, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{orderId}/buyer-confirm")
    public ResponseEntity<?> buyerConfirmDelivery(@PathVariable UUID orderId,
            @AuthenticationPrincipal User user,
            @RequestBody Map<String, Object> payload) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            String deliveryStatus = (String) payload.get("deliveryStatus");
            int rating = ((Number) payload.get("rating")).intValue();
            String comment = (String) payload.get("comment");
            return ResponseEntity.ok(orderService.buyerConfirmDelivery(orderId, deliveryStatus, rating, comment, user));
        } catch (RuntimeException e) {

```
