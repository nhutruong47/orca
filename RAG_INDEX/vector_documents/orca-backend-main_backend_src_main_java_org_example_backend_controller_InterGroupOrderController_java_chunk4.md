# Knowledge Document: InterGroupOrderController.java (Chunk 5/5)

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
  "chunk_index": 4,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
roupOrderAccess(user, orderId);
            String deliveryStatus = (String) payload.get("deliveryStatus");
            int rating = ((Number) payload.get("rating")).intValue();
            String comment = (String) payload.get("comment");
            return ResponseEntity.ok(orderService.buyerConfirmDelivery(orderId, deliveryStatus, rating, comment, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/mark-viewed")
    public ResponseEntity<?> markViewed(@RequestBody Map<String, Object> payload,
                                        @AuthenticationPrincipal User user) {
        try {
            List<String> orderIdsStr = (List<String>) payload.get("orderIds");
            List<UUID> orderIds = orderIdsStr.stream().map(UUID::fromString).collect(java.util.stream.Collectors.toList());
            String role = (String) payload.get("role");
            // Ensure current user has access to every order being marked
            for (UUID orderId : orderIds) {
                accessControlService.requireInterGroupOrderAccess(user, orderId);
            }
            orderService.markOrdersAsViewed(orderIds, role);
            return ResponseEntity.ok(Map.of("message", "Success"));
        } catch (Exception e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }
}

```
