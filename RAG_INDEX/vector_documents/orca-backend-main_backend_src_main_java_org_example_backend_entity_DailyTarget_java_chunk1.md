# Knowledge Document: DailyTarget.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/DailyTarget.java",
  "language": "java",
  "module": "entity",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
mn(name = "productivity_kg_per_hour")
    private Double productivityKgPerHour;

    public enum TargetStatus {
        PENDING,
        IN_PROGRESS,
        COMPLETED,
        PARTIAL,
        SKIPPED
    }

    @PrePersist
    protected void onCreate() {}

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }
    public ProductionPlan getPlan() { return plan; }
    public void setPlan(ProductionPlan plan) { this.plan = plan; }
    public ProductionOrder getOrder() { return order; }
    public void setOrder(ProductionOrder order) { this.order = order; }
    public LocalDate getTargetDate() { return targetDate; }
    public void setTargetDate(LocalDate targetDate) { this.targetDate = targetDate; }
    public Double getTargetQuantityKg() { return targetQuantityKg; }
    public void setTargetQuantityKg(Double targetQuantityKg) { this.targetQuantityKg = targetQuantityKg; }
    public Double getTargetRoastKg() { return targetRoastKg; }
    public void setTargetRoastKg(Double targetRoastKg) { this.targetRoastKg = targetRoastKg; }
    public Double getTargetQcKg() { return targetQcKg; }
    public void setTargetQcKg(Double targetQcKg) { this.targetQcKg = targetQcKg; }
    public Double getTargetPackagedKg() { return targetPackagedKg; }
    public void setTargetPackagedKg(Double targetPackagedKg) { this.targetPackagedKg = targetPackagedKg; }
    public Integer getTargetPackages() { return targetPackages; }
    public void setTargetPackages(Integer targetPackages) { this.targetPackages = targetPackages; }
    public Double getActualRoastKg() { return actualRoastKg; }
    public void setActualRoastKg(Double actualRoastKg) { this.actualRoastKg = actualRoastKg; }
    public Double getActualQcKg() { return actualQcKg; }
    public void setActualQcKg(Double actualQcKg) { this.actualQcKg = actualQcKg; }
    public Double getActualQcFailKg() { return actualQcFailKg; }
    public void setActualQcFailKg(Double actualQcFailKg) { this.actualQcFailKg = actualQcFailKg; }
    public Double getActualPackagedKg() { return actualPackagedKg; }
    public void setActualPackagedKg(Double actualPackagedKg) { this.actualPackagedKg = actualPackagedKg; }
    public Integer getActualPackages() { return actualPackages; }
    public void setActualPackages(Integer actualPackages) { this.actualPackages = actualPackages; }

```
