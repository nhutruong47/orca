# Knowledge Document: InventoryItem.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/InventoryItem.java",
  "language": "java",
  "module": "entity",
  "business_domain": "inventory",
  "tags": [
    "inventory"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory

## Source Code Chunk
```java
) {
        if (this.quantity <= 0) return "OUT_OF_STOCK";
        if (this.quantity <= this.lowStockThreshold) return "LOW_STOCK";
        return "IN_STOCK";
    }

    /** Convenience: human-readable name combining type + state */
    public String getDisplayName() {
        String stateVi = switch (productState) {
            case "GREEN" -> "Hạt xanh";
            case "ROASTED" -> "Đã rang";
            case "GROUND" -> "Đã xay";
            case "PACKAGED" -> "Đã đóng gói";
            default -> productState;
        };
        return productType + " - " + stateVi;
    }

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }

    public Team getTeam() { return team; }
    public void setTeam(Team team) { this.team = team; }

    public String getProductType() { return productType; }
    public void setProductType(String productType) { this.productType = productType; }

    public String getProductState() { return productState; }
    public void setProductState(String productState) { this.productState = productState; }

    public Double getQuantity() { return quantity; }
    public void setQuantity(Double quantity) { this.quantity = quantity; }

    public String getUnit() { return unit; }
    public void setUnit(String unit) { this.unit = unit; }

    public Double getLowStockThreshold() { return lowStockThreshold; }
    public void setLowStockThreshold(Double lowStockThreshold) { this.lowStockThreshold = lowStockThreshold; }

    public LocalDateTime getLastUpdated() { return lastUpdated; }
    public void setLastUpdated(LocalDateTime lastUpdated) { this.lastUpdated = lastUpdated; }

    /** @deprecated Use productType instead */
    @Transient
    public String getName() {
        return getDisplayName();
    }

    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public void setImageUrl(String imageUrl) {
        this.imageUrl = imageUrl;
    }

    public String getOrigin() {
        return origin;
    }

    public void setOrigin(String origin) {
        this.origin = origin;
    }


```
