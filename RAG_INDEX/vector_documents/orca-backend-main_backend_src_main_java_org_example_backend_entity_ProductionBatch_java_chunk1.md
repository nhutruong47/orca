# Knowledge Document: ProductionBatch.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/ProductionBatch.java",
  "language": "java",
  "module": "entity",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
ic String getBatchCode() { return batchCode; }
    public void setBatchCode(String batchCode) { this.batchCode = batchCode; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Double getPlannedQuantity() { return plannedQuantity; }
    public void setPlannedQuantity(Double plannedQuantity) { this.plannedQuantity = plannedQuantity; }
    public Double getActualQuantity() { return actualQuantity; }
    public void setActualQuantity(Double actualQuantity) { this.actualQuantity = actualQuantity; }
    public String getUnit() { return unit; }
    public void setUnit(String unit) { this.unit = unit; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public LocalDateTime getStartTime() { return startTime; }
    public void setStartTime(LocalDateTime startTime) { this.startTime = startTime; }
    public LocalDateTime getDueTime() { return dueTime; }
    public void setDueTime(LocalDateTime dueTime) { this.dueTime = dueTime; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
}

```
