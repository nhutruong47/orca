# Knowledge Document: InventoryService.java (Chunk 3/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/InventoryService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory",
    "production",
    "dashboard"
  ],
  "logical_type": "Service",
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, dashboard

## Source Code Chunk
```java
double quantity) {
        if (quantity <= 0) return;

        Team team = teamRepo.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        // Deduct from source
        InventoryItem source = getOrCreate(team, productType, fromState);
        double newSourceQty = Math.max(0, source.getQuantity() - quantity);
        source.setQuantity(newSourceQty);
        inventoryRepo.save(source);

        // Add to target
        InventoryItem target = getOrCreate(team, productType, toState);
        target.setQuantity(target.getQuantity() + quantity);
        inventoryRepo.save(target);
    }

    /**
     * Deduct from packaged stock when order is delivered.
     */
    @Transactional
    public void deductPackagedStock(UUID teamId, String productType, double quantity) {
        if (quantity <= 0) return;

        InventoryItem item = inventoryRepo.findByTeamIdAndProductTypeAndProductState(teamId, productType, "PACKAGED")
                .orElse(null);
        if (item != null) {
            item.setQuantity(Math.max(0, item.getQuantity() - quantity));
            inventoryRepo.save(item);
        }
    }

    /**
     * Initialize default inventory items for a team (4 types x 4 states).
     */
    @Transactional
    public void initializeDefaultInventory(UUID teamId) {
        if (inventoryRepo.existsByTeamId(teamId)) {
            return;
        }
        Team team = teamRepo.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));
        String[] types = {"Arabica", "Robusta", "Culi", "Blend"};
        String[] states = {"GREEN", "ROASTED", "GROUND", "PACKAGED"};
        for (String type : types) {
            for (String state : states) {
                Optional<InventoryItem> existing = inventoryRepo.findByTeamIdAndProductTypeAndProductState(teamId, type, state);
                if (existing.isEmpty()) {
                    InventoryItem item = new InventoryItem();
                    item.setTeam(team);
                    item.setProductType(type);
                    item.setProductState(state);
                    item.setQuantity(0.0);
                    item.setUnit("kg");
                    inventoryRepo.save(item);
                }
            }
        }
    }

    // ========== HELPERS ==========


```
