# Knowledge Document: InventoryItemDTO.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/InventoryItemDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "inventory",
  "tags": [
    "inventory"
  ],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDateTime;

public class InventoryItemDTO {
    private String id;
    private String teamId;
    private String productType;
    private String productState;
    private String displayName;
    private Double quantity;
    private String unit;
    private Double lowStockThreshold;
    private String status;
    private LocalDateTime lastUpdated;

    // Featured Product fields
    private String price;
    private String description;
    private String imageUrl;
    private String origin;
    private String roastLevel;
    private String processing;
    private String tasteNotes;
    private Boolean isFeatured;

    // Keep backward compat
    private String name;

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getTeamId() { return teamId; }
    public void setTeamId(String teamId) { this.teamId = teamId; }

    public String getProductType() { return productType; }
    public void setProductType(String productType) { this.productType = productType; }

    public String getProductState() { return productState; }
    public void setProductState(String productState) { this.productState = productState; }

    public String getDisplayName() { return displayName; }
    public void setDisplayName(String displayName) { this.displayName = displayName; }

    public Double getQuantity() { return quantity; }
    public void setQuantity(Double quantity) { this.quantity = quantity; }

    public String getUnit() { return unit; }
    public void setUnit(String unit) { this.unit = unit; }

    public Double getLowStockThreshold() { return lowStockThreshold; }
    public void setLowStockThreshold(Double lowStockThreshold) { this.lowStockThreshold = lowStockThreshold; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }

    public LocalDateTime getLastUpdated() { return lastUpdated; }
    public void setLastUpdated(LocalDateTime lastUpdated) { this.lastUpdated = lastUpdated; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getPrice() { return price; }
    public void setPrice(String price) { this.price = price; }

    public String getDescription() { return description; }

```
