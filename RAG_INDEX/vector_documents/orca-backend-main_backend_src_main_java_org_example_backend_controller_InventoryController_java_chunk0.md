# Knowledge Document: InventoryController.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/InventoryController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory",
    "security",
    "authentication"
  ],
  "logical_type": "Controller",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, security, authentication

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.dto.InventoryItemDTO;
import org.example.backend.entity.User;
import org.example.backend.service.AccessControlService;
import org.example.backend.service.InventoryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/inventory")
public class InventoryController {

    @Autowired
    private InventoryService inventoryService;

    @Autowired
    private AccessControlService accessControlService;

    @GetMapping
    public ResponseEntity<List<InventoryItemDTO>> getByTeam(@RequestParam UUID teamId, @AuthenticationPrincipal User user) {
        accessControlService.requireTeamMember(user, teamId);
        return ResponseEntity.ok(inventoryService.getByTeam(teamId));
    }

    @GetMapping("/featured")
    public ResponseEntity<List<InventoryItemDTO>> getFeaturedProducts() {
        return ResponseEntity.ok(inventoryService.getFeaturedProducts());
    }

    @PostMapping
    public ResponseEntity<?> create(@RequestBody InventoryItemDTO dto, @AuthenticationPrincipal User user) {
        accessControlService.requireTeamMember(user, UUID.fromString(dto.getTeamId()));
        try {
            return ResponseEntity.ok(inventoryService.create(dto));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PatchMapping("/{id}/quantity")
    public ResponseEntity<?> updateQuantity(
            @PathVariable UUID id,
            @AuthenticationPrincipal User user,
            @RequestBody Map<String, Double> body) {
        accessControlService.requireInventoryItemAccess(user, id);
        try {
            Double qty = body.get("quantity");
            if (qty == null) {
                return ResponseEntity.badRequest().body(Map.of("error", "Vui lòng nhập số lượng (quantity)"));
            }
            return ResponseEntity.ok(inventoryService.updateQuantity(id, qty));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }


```
