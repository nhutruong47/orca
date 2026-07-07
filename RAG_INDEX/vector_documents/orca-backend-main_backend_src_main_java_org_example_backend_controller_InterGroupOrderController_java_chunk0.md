# Knowledge Document: InterGroupOrderController.java (Chunk 1/5)

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
  "chunk_index": 0,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.dto.InterGroupOrderDTO;
import org.example.backend.entity.User;
import org.example.backend.service.AccessControlService;
import org.example.backend.service.InterGroupOrderService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/inter-group-orders")
public class InterGroupOrderController {

    @Autowired
    private InterGroupOrderService orderService;

    @Autowired
    private AccessControlService accessControlService;

    @GetMapping("/outbound/{buyerTeamId}")
    public ResponseEntity<?> getOutboundOrders(@PathVariable UUID buyerTeamId,
                                               @AuthenticationPrincipal User user) {
        accessControlService.requireTeamMember(user, buyerTeamId);
        return ResponseEntity.ok(orderService.getOutboundOrders(buyerTeamId));
    }

    @GetMapping("/outbound-personal")
    public ResponseEntity<List<InterGroupOrderDTO>> getMyOutboundOrders(@AuthenticationPrincipal User user) {
        return ResponseEntity.ok(orderService.getMyOutboundOrders(user));
    }

    @GetMapping("/inbound/{sellerTeamId}")
    public ResponseEntity<?> getInboundOrders(@PathVariable UUID sellerTeamId,
                                              @AuthenticationPrincipal User user) {
        accessControlService.requireTeamMember(user, sellerTeamId);
        return ResponseEntity.ok(orderService.getInboundOrders(sellerTeamId));
    }

    @PostMapping
    public ResponseEntity<?> placeOrder(@RequestBody InterGroupOrderDTO dto, @AuthenticationPrincipal User user) {
        try {
            return ResponseEntity.ok(orderService.createOrder(dto, user));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{orderId}")
    public ResponseEntity<?> getOrder(@PathVariable UUID orderId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireInterGroupOrderAccess(user, orderId);
            return ResponseEntity.ok(orderService.getById(orderId));

```
