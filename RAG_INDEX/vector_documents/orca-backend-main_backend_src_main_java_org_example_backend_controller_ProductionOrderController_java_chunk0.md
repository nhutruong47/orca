# Knowledge Document: ProductionOrderController.java (Chunk 1/4)

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
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: production, authentication, security

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.dto.ProductionOrderDTO;
import org.example.backend.entity.ProductionOrder;
import org.example.backend.entity.User;
import org.example.backend.service.AccessControlService;
import org.example.backend.service.ProductionOrderService;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/production")
@CrossOrigin("*")
public class ProductionOrderController {

    private final ProductionOrderService orderService;
    private final AccessControlService accessControlService;

    public ProductionOrderController(ProductionOrderService orderService, AccessControlService accessControlService) {
        this.orderService = orderService;
        this.accessControlService = accessControlService;
    }

    @GetMapping("/teams/{teamId}/orders")
    public ResponseEntity<?> getOrders(
            @PathVariable UUID teamId,
            @AuthenticationPrincipal User user,
            @RequestParam(required = false) String status) {
        accessControlService.requireTeamMember(user, teamId);
        List<ProductionOrder> orders;
        if (status != null && !status.isBlank()) {
            orders = orderService.getActiveOrders(teamId);
        } else {
            orders = orderService.getOrdersByTeam(teamId);
        }
        List<ProductionOrderDTO> dtos = orders.stream()
                .map(orderService::toDTO)
                .collect(Collectors.toList());
        return ResponseEntity.ok(dtos);
    }

    @PostMapping("/teams/{teamId}/orders")
    public ResponseEntity<?> createOrder(
            @PathVariable UUID teamId,
            @AuthenticationPrincipal User user,
            @RequestBody Map<String, Object> body) {
        accessControlService.requireTeamMember(user, teamId);
        try {
            ProductionOrder raw = mapToOrder(body);
            ProductionOrder created = orderService.createOrder(teamId, raw);
            return ResponseEntity.ok(orderService.toDTO(created));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }


```
