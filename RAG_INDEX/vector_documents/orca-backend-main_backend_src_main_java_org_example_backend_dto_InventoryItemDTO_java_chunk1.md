# Knowledge Document: InventoryItemDTO.java (Chunk 2/2)

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
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory

## Source Code Chunk
```java
ted() { return lastUpdated; }
    public void setLastUpdated(LocalDateTime lastUpdated) { this.lastUpdated = lastUpdated; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getPrice() { return price; }
    public void setPrice(String price) { this.price = price; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }

    public String getOrigin() { return origin; }
    public void setOrigin(String origin) { this.origin = origin; }

    public String getRoastLevel() { return roastLevel; }
    public void setRoastLevel(String roastLevel) { this.roastLevel = roastLevel; }

    public String getProcessing() { return processing; }
    public void setProcessing(String processing) { this.processing = processing; }

    public String getTasteNotes() { return tasteNotes; }
    public void setTasteNotes(String tasteNotes) { this.tasteNotes = tasteNotes; }

    public Boolean getIsFeatured() { return isFeatured; }
    public void setIsFeatured(Boolean isFeatured) { this.isFeatured = isFeatured; }
}

```
