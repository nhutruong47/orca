# Knowledge Document: ProductionOrder.java (Chunk 1/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/ProductionOrder.java",
  "language": "java",
  "module": "entity",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 6
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
@Table(name = "production_orders")
public class ProductionOrder {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(updatable = false, nullable = false)
    private UUID id;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "team_id", nullable = false)
    private Team team;

    @Column(name = "order_code", unique = true, length = 40)
    private String orderCode;

    @Column(nullable = false, length = 500)
    private String title;

    @Column(columnDefinition = "TEXT")
    private String description;

    @Column(name = "customer_name")
    private String customerName;

    // === THONG TIN SAN PHAM ===
    @Column(name = "product_type", length = 100)
    private String productType;

    @Column(name = "process_type", length = 100)
    private String processType;

    @Column(name = "roast_level", length = 50)
    private String roastLevel;

    @Column(name = "package_size", length = 100)
    private String packageSize;

    @Column(name = "total_packages")
    private Integer totalPackages;

    // === YIELD & INPUT ===
    @Column(name = "output_target")
    private Double outputTarget;

    @Column(name = "expected_yield")
    private Double expectedYield;

    @Column(name = "expected_loss")
    private Double expectedLoss;

    @Column(name = "input_required")
    private Double inputRequired;

    private String unit;

    // === CAC NGAY QUAN TRONG ===
    @Column(name = "order_date")
    private LocalDate orderDate;

    @Column(name = "confirm_date")
    private LocalDate confirmDate;

    @Column(name = "production_start_date")
    private LocalDate productionStartDate;

    @Column(name = "internal_deadline")
    private LocalDateTime internalDeadline;

    @Column(name = "customer_delivery_date")
    private LocalDate customerDeliveryDate;

    @Column(name = "safety_buffer_days")
    private Integer safetyBufferDays;

    // === GIAO HANG ===
    @Column(name = "recipient_name")
    private String recipientName;

    @Column(name = "recipient_phone")
    private String recipientPhone;

    @Column(name = "shipping_note", columnDefinition = "TEXT")
    private String shippingNote;

    // === TRANG THAI & SẢN LƯỢNG ===

```
