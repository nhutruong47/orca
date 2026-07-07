# Knowledge Document: ProductionBatch.java (Chunk 1/2)

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
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
package org.example.backend.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "production_batches")
public class ProductionBatch {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(updatable = false, nullable = false)
    private UUID id;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "team_id", nullable = false)
    private Team team;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "order_id")
    private ProductionOrder order;

    @Column(name = "batch_code", unique = true, length = 40)
    private String batchCode;

    @Column(nullable = false, length = 500)
    private String name;

    @Column(name = "planned_quantity")
    private Double plannedQuantity;

    @Column(name = "actual_quantity")
    private Double actualQuantity;

    private String unit;

    @Column(nullable = false)
    private String status = "PLANNED";

    @Column(name = "start_time")
    private LocalDateTime startTime;

    @Column(name = "due_time")
    private LocalDateTime dueTime;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    @PrePersist
    protected void onCreate() {
        this.createdAt = LocalDateTime.now();
        this.updatedAt = this.createdAt;
        if (this.batchCode == null || this.batchCode.isBlank()) {
            this.batchCode = "BAT-" + System.currentTimeMillis();
        }
    }

    @PreUpdate
    protected void onUpdate() {
        this.updatedAt = LocalDateTime.now();
    }

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }
    public Team getTeam() { return team; }
    public void setTeam(Team team) { this.team = team; }
    public ProductionOrder getOrder() { return order; }
    public void setOrder(ProductionOrder order) { this.order = order; }
    public String getBatchCode() { return batchCode; }
    public void setBatchCode(String batchCode) { this.batchCode = batchCode; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public Double getPlannedQuantity() { return plannedQuantity; }
    public void setPlannedQuantity(Double plannedQuantity) { this.plannedQuantity = plannedQuantity; }

```
