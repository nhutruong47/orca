# Knowledge Document: InventoryService.java (Chunk 4/4)

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
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, dashboard

## Source Code Chunk
```java
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

    private InventoryItem getOrCreate(Team team, String productType, String productState) {
        return inventoryRepo.findByTeamIdAndProductTypeAndProductState(team.getId(), productType, productState)
                .orElseGet(() -> {
                    InventoryItem newItem = new InventoryItem();
                    newItem.setTeam(team);
                    newItem.setProductType(productType);
                    newItem.setProductState(productState);
                    newItem.setQuantity(0.0);
                    newItem.setUnit("kg");
                    return inventoryRepo.save(newItem);
                });
    }

    public InventoryItemDTO toDTO(InventoryItem i) {
        InventoryItemDTO dto = new InventoryItemDTO();
        dto.setId(i.getId().toString());
        dto.setTeamId(i.getTeam().getId().toString());
        dto.setProductType(i.getProductType());
        dto.setProductState(i.getProductState());
        dto.setDisplayName(i.getDisplayName());
        dto.setName(i.getDisplayName());
        dto.setQuantity(i.getQuantity());
        dto.setUnit(i.getUnit());
        dto.setLowStockThreshold(i.getLowStockThreshold());
        dto.setStatus(i.getStockStatus());
        dto.setLastUpdated(i.getLastUpdated());

        // Featured fields
        dto.setPrice(i.getPrice());
        dto.setDescription(i.getDescription());
        dto.setImageUrl(i.getImageUrl());
        dto.setOrigin(i.getOrigin());
        dto.setRoastLevel(i.getRoastLevel());
        dto.setProcessing(i.getProcessing());
        dto.setTasteNotes(i.getTasteNotes());
        dto.setIsFeatured(i.getIsFeatured());

        return dto;
    }
}

```
