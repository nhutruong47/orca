# Knowledge Document: ManufacturingRequestDTO.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ManufacturingRequestDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDateTime;

public class ManufacturingRequestDTO {
    private String id;
    private String type;
    private String title;
    private String coffeeType;
    private String quantity;
    private LocalDateTime deadline;
    private String region;
    private String details;
    private String createdAt;
    private String buyerTeamId;
    
    // Getters and setters
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getType() { return type; }
    public void setType(String type) { this.type = type; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getCoffeeType() { return coffeeType; }
    public void setCoffeeType(String coffeeType) { this.coffeeType = coffeeType; }
    public String getQuantity() { return quantity; }
    public void setQuantity(String quantity) { this.quantity = quantity; }
    public LocalDateTime getDeadline() { return deadline; }
    public void setDeadline(LocalDateTime deadline) { this.deadline = deadline; }
    public String getRegion() { return region; }
    public void setRegion(String region) { this.region = region; }
    public String getDetails() { return details; }
    public void setDetails(String details) { this.details = details; }
    public String getCreatedAt() { return createdAt; }
    public void setCreatedAt(String createdAt) { this.createdAt = createdAt; }
    public String getBuyerTeamId() { return buyerTeamId; }
    public void setBuyerTeamId(String buyerTeamId) { this.buyerTeamId = buyerTeamId; }
}

```
