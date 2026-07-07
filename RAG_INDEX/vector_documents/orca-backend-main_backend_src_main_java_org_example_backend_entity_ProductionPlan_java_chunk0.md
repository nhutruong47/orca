# Knowledge Document: ProductionPlan.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/ProductionPlan.java",
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
import java.util.List;
import java.util.UUID;

@Entity
@Table(name = "production_plans")
public class ProductionPlan {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "order_id", nullable = false)
    private ProductionOrder order;

    @Column(name = "plan_code", unique = true)
    private String planCode;

    @Column(name = "total_days")
    private Integer totalDays;

    @Column(name = "total_working_days")
    private Integer totalWorkingDays;

    @Column(name = "daily_target_kg")
    private Double dailyTargetKg;

    @Column(name = "total_input_kg")
    private Double totalInputKg;

    @Column(name = "total_roast_kg")
    private Double totalRoastKg;

    @Column(name = "total_qc_kg")
    private Double totalQcKg;

    @Column(name = "total_packaged_kg")
    private Double totalPackagedKg;

    @Column(name = "total_packages")
    private Integer totalPackages;

    @Column(name = "ai_recommendations", columnDefinition = "TEXT")
    private String aiRecommendations;

    @Column(name = "risk_factors", columnDefinition = "TEXT")
    private String riskFactors;

    @Enumerated(EnumType.STRING)
    private PlanStatus status = PlanStatus.DRAFT;

    @OneToMany(mappedBy = "plan", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<DailyTarget> dailyTargets;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "approved_at")
    private LocalDateTime approvedAt;

    @Column(name = "approved_by")
    private UUID approvedBy;

    public enum PlanStatus {
        DRAFT,
        PENDING,
        APPROVED,
        IN_PROGRESS,
        COMPLETED
    }

    @PrePersist
    protected void onCreate() {
        this.createdAt = LocalDateTime.now();
        if (this.planCode == null || this.planCode.isBlank()) {
            this.planCode = "PLAN-" + System.currentTimeMillis();
        }
    }

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }
    public ProductionOrder getOrder() { return order; }
    public void setOrder(ProductionOrder order) { this.order = order; }

```
