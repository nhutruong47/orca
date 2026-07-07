# Knowledge Document: InventoryService.java (Chunk 1/4)

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
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, dashboard

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.InventoryItemDTO;
import org.example.backend.entity.InventoryItem;
import org.example.backend.entity.Team;
import org.example.backend.repository.InventoryRepository;
import org.example.backend.repository.TeamRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.*;
import java.util.stream.Collectors;

@Service
public class InventoryService {

    private final InventoryRepository inventoryRepo;
    private final TeamRepository teamRepo;

    public InventoryService(InventoryRepository inventoryRepo, TeamRepository teamRepo) {
        this.inventoryRepo = inventoryRepo;
        this.teamRepo = teamRepo;
    }

    // ========== READ ==========

    public List<InventoryItemDTO> getByTeam(UUID teamId) {
        return inventoryRepo.findByTeamIdOrderByProductTypeAscProductStateAsc(teamId)
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    public List<InventoryItemDTO> getFeaturedProducts() {
        return inventoryRepo.findByIsFeaturedTrue()
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    /** Get inventory grouped by product type for dashboard display */
    public Map<String, Map<String, Double>> getInventoryMatrix(UUID teamId) {
        List<InventoryItem> items = inventoryRepo.findByTeamIdOrderByProductTypeAscProductStateAsc(teamId);
        Map<String, Map<String, Double>> matrix = new LinkedHashMap<>();
        for (InventoryItem item : items) {
            matrix.computeIfAbsent(item.getProductType(), k -> new LinkedHashMap<>())
                    .put(item.getProductState(), item.getQuantity());
        }
        return matrix;
    }

    // ========== CREATE ==========

    public InventoryItemDTO create(InventoryItemDTO dto) {
        Team t = teamRepo.findById(UUID.fromString(dto.getTeamId()))
                .orElseThrow(() -> new RuntimeException("Team not found"));

        String pType = dto.getProductType() != null ? dto.getProductType() : dto.getName();
        String pState = dto.getProductState() != null ? dto.getProductState() : "GREEN";

        // Check if already exists
        Optional<InventoryItem> existing = inventoryRepo.findByTeamIdAndProductTypeAndProductState(
                t.getId(), pType, pState);

```
