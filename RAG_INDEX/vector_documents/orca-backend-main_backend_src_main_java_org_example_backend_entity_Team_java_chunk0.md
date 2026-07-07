# Knowledge Document: Team.java (Chunk 1/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/Team.java",
  "language": "java",
  "module": "entity",
  "business_domain": "factory",
  "tags": [
    "factory",
    "employee"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, employee

## Source Code Chunk
```java
package org.example.backend.entity;

import jakarta.persistence.*;
import jakarta.validation.constraints.Min;
import java.time.LocalDateTime;
import java.util.Random;
import java.util.UUID;

@Entity
@Table(name = "teams")
public class Team {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(updatable = false, nullable = false)
    private UUID id;

    @Version
    private Long version;

    @Column(nullable = false)
    private String name;

    private String description;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "owner_id", nullable = false)
    private User owner;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "is_published", nullable = false)
    private boolean isPublished = false;

    private String specialty;
    private String capacity;
    private String region;
    private String factoryType;

    @Column(name = "capacity_value")
    private Double capacityValue;

    @Column(name = "capacity_unit")
    private String capacityUnit;

    @Column(name = "factory_image_url", columnDefinition = "TEXT")
    private String factoryImageUrl;

    @Column(name = "factory_images", columnDefinition = "TEXT")
    private String factoryImages;

    @Column(name = "verification_status")
    private String verificationStatus = "NOT_SUBMITTED";

    @Column(name = "business_license", length = 1000)
    private String businessLicense;

    @Column(name = "business_address", length = 1000)
    private String businessAddress;

    @Column(name = "website_url", length = 1000)
    private String websiteUrl;

    @Column(name = "facebook_url", length = 1000)
    private String facebookUrl;

    @Column(name = "certification_document", length = 1000)
    private String certificationDocument;

    @Column(name = "certificates", length = 1000)
    private String certificates;

    @Column(name = "verification_reject_reason", length = 1000)
    private String verificationRejectReason;

    @Min(0)
    @Column(name = "completed_orders", nullable = false, columnDefinition = "integer default 0")
    private int completedOrders = 0;

    @Min(0)
    @Column(name = "cancelled_orders", nullable = false, columnDefinition = "integer default 0")
    private int cancelledOrders = 0;

    @Min(0)

```
