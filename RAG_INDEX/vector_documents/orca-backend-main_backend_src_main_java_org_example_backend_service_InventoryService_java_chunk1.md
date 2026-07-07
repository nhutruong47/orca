# Knowledge Document: InventoryService.java (Chunk 2/4)

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
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, dashboard

## Source Code Chunk
```java
w RuntimeException("Team not found"));

        String pType = dto.getProductType() != null ? dto.getProductType() : dto.getName();
        String pState = dto.getProductState() != null ? dto.getProductState() : "GREEN";

        // Check if already exists
        Optional<InventoryItem> existing = inventoryRepo.findByTeamIdAndProductTypeAndProductState(
                t.getId(), pType, pState);
        if (existing.isPresent()) {
            throw new RuntimeException("Mục kho '" + pType + " - " + pState + "' đã tồn tại.");
        }

        InventoryItem item = new InventoryItem();
        item.setTeam(t);
        item.setProductType(pType);
        item.setProductState(pState);
        item.setQuantity(dto.getQuantity() != null ? dto.getQuantity() : 0.0);
        item.setUnit(dto.getUnit() != null ? dto.getUnit() : "kg");
        item.setLowStockThreshold(dto.getLowStockThreshold() != null ? dto.getLowStockThreshold() : 100.0);

        return toDTO(inventoryRepo.save(item));
    }

    // ========== UPDATE ==========

    public InventoryItemDTO updateQuantity(UUID id, Double newQuantity) {
        InventoryItem item = inventoryRepo.findById(id)
                .orElseThrow(() -> new RuntimeException("Item not found"));
        item.setQuantity(newQuantity);
        return toDTO(inventoryRepo.save(item));
    }

    // ========== DELETE ==========

    public void delete(UUID id) {
        inventoryRepo.deleteById(id);
    }

    // ========== AUTO INVENTORY UPDATE (Production Workflow) ==========

    /**
     * Automatically adjust inventory when a production stage completes.
     * @param teamId       the team/factory
     * @param productType  e.g. "Arabica", "Robusta"
     * @param fromState    source state (e.g. "GREEN")
     * @param toState      target state (e.g. "ROASTED")
     * @param quantity     amount to transfer
     */
    @Transactional
    public void transferStock(UUID teamId, String productType, String fromState, String toState, double quantity) {
        if (quantity <= 0) return;

        Team team = teamRepo.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));

        // Deduct from source
        InventoryItem source = getOrCreate(team, productType, fromState);
        double newSourceQty = Math.max(0, source.getQuantity() - quantity);
        source.setQuantity(newSourceQty);

```
