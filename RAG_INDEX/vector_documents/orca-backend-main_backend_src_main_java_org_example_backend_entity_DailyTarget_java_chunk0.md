# Knowledge Document: DailyTarget.java (Chunk 1/3)

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
  "chunk_index": 0,
  "total_chunks": 3
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
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "daily_targets")
public class DailyTarget {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "plan_id", nullable = false)
    private ProductionPlan plan;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "order_id", nullable = false)
    private ProductionOrder order;

    @Column(name = "target_date", nullable = false)
    private LocalDate targetDate;

    @Column(name = "target_quantity_kg")
    private Double targetQuantityKg;

    @Column(name = "target_roast_kg")
    private Double targetRoastKg;

    @Column(name = "target_qc_kg")
    private Double targetQcKg;

    @Column(name = "target_packaged_kg")
    private Double targetPackagedKg;

    @Column(name = "target_packages")
    private Integer targetPackages;

    @Column(name = "actual_roast_kg")
    private Double actualRoastKg;

    @Column(name = "actual_qc_kg")
    private Double actualQcKg;

    @Column(name = "actual_qc_fail_kg")
    private Double actualQcFailKg;

    @Column(name = "actual_packaged_kg")
    private Double actualPackagedKg;

    @Column(name = "actual_packages")
    private Integer actualPackages;

    @Column(name = "total_actual_kg")
    private Double totalActualKg;

    @Column(name = "completion_rate")
    private Double completionRate;

    @Column(name = "is_holiday")
    private Boolean isHoliday = false;

    @Column(name = "notes", columnDefinition = "TEXT")
    private String notes;

    @Column(name = "issues", columnDefinition = "TEXT")
    private String issues;

    @Enumerated(EnumType.STRING)
    private TargetStatus status = TargetStatus.PENDING;

    @Column(name = "total_worker_hours")
    private Double totalWorkerHours;

    @Column(name = "productivity_kg_per_hour")
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

```
