# Knowledge Document: ProductionPlanController.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/ProductionPlanController.java",
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
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: production, authentication, security

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.dto.DailyTargetDTO;
import org.example.backend.dto.ProductionPlanDTO;
import org.example.backend.service.ProductionPlanService;
import org.example.backend.entity.User;
import org.example.backend.service.AccessControlService;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/production/plans")
@CrossOrigin("*")
public class ProductionPlanController {

    private final ProductionPlanService planService;
    private final AccessControlService accessControlService;

    public ProductionPlanController(ProductionPlanService planService, AccessControlService accessControlService) {
        this.planService = planService;
        this.accessControlService = accessControlService;
    }

    @PostMapping("/orders/{orderId}/generate")
    public ResponseEntity<?> generatePlan(
            @PathVariable UUID orderId,
            @AuthenticationPrincipal User currentUser) {
        accessControlService.requireProductionOrderAccess(currentUser, orderId);
        try {
            ProductionPlanDTO plan = planService.generatePlan(orderId);
            return ResponseEntity.ok(plan);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{planId}")
    public ResponseEntity<?> getPlan(
            @PathVariable UUID planId,
            @AuthenticationPrincipal User currentUser) {
        accessControlService.requireProductionPlanAccess(currentUser, planId);
        try {
            return ResponseEntity.ok(planService.getPlanById(planId));
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }

    @GetMapping("/orders/{orderId}")
    public ResponseEntity<?> getPlansByOrder(
            @PathVariable UUID orderId,
            @AuthenticationPrincipal User currentUser) {
        accessControlService.requireProductionOrderAccess(currentUser, orderId);
        return ResponseEntity.ok(planService.getPlansByOrder(orderId));
    }

    @PatchMapping("/{planId}/approve")
    public ResponseEntity<?> approvePlan(

```
