# Knowledge Document: InterGroupOrder.java (Chunk 1/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/InterGroupOrder.java",
  "language": "java",
  "module": "entity",
  "business_domain": "factory",
  "tags": [
    "factory",
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, production

## Source Code Chunk
```java
package org.example.backend.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;
import java.util.UUID;

/**
 * Marketplace order (RFQ flow).
 * Status flow: RFQ_CREATED → QUOTED → CONFIRMED → IN_PRODUCTION → QC → COMPLETED → SHIPPING → DELIVERED → REVIEWED
 * Legacy statuses (PENDING, ACCEPTED, REJECTED, CANCELED) are still supported for backward compat.
 */
@Entity
@Table(name = "inter_group_orders")
public class InterGroupOrder {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(updatable = false, nullable = false)
    private UUID id;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "buyer_team_id")
    private Team buyerTeam;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "buyer_user_id")
    private User buyerUser;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "seller_team_id", nullable = false)
    private Team sellerTeam;

    @Column(nullable = false)
    private String title;

    @Column(columnDefinition = "TEXT")
    private String description;

    @Column(nullable = false)
    private Integer quantity;

    private LocalDateTime deadline;

    /**
     * New marketplace status flow:
     * RFQ_CREATED, QUOTED, CONFIRMED, IN_PRODUCTION, QC, COMPLETED, SHIPPING, DELIVERED, REVIEWED
     * Legacy: PENDING (=RFQ_CREATED), ACCEPTED (=CONFIRMED), REJECTED, CANCELED
     */
    @Column(nullable = false)
    private String status = "RFQ_CREATED";

    @Column(name = "linked_goal_id")
    private UUID linkedGoalId;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "cancelled_by")
    private String cancelledBy;

    // === Nguồn nguyên liệu ===
    /** CUSTOMER_PROVIDED, FACTORY_PROVIDED, COMBINED */
    @Column(name = "material_source", length = 30)
    private String materialSource;

    // === Dịch vụ yêu cầu (comma-separated) ===
    /** e.g. "ROASTING,PACKAGING,QC" or "FULL_SERVICE" */
    @Column(name = "services", length = 500)
    private String services;

    // === Loại cà phê ===
    @Column(name = "product_type", length = 100)
    private String productType;

    // === Báo giá ===
    @Column(name = "quoted_price")
    private Double quotedPrice;

    @Column(name = "quoted_note", columnDefinition = "TEXT")
    private String quotedNote;

    @Column(name = "quoted_at")

```
