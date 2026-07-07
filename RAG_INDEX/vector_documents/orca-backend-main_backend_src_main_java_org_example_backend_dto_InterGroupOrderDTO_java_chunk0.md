# Knowledge Document: InterGroupOrderDTO.java (Chunk 1/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/InterGroupOrderDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "factory",
  "tags": [
    "factory"
  ],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: factory

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDateTime;
import java.util.UUID;

public class InterGroupOrderDTO {

    private String id;
    private String buyerTeamId;
    private String buyerTeamName;
    private String buyerUserId;
    private String buyerUserName;
    private String sellerTeamId;
    private String sellerTeamName;
    private String title;
    private String description;
    private Integer quantity;
    private LocalDateTime deadline;
    private String status;
    private String linkedGoalId;
    private LocalDateTime createdAt;
    private int buyerTrustScore;
    private String cancelledBy;

    // === Delivery Profile ===
    private String contactPhone;
    private String contactPhoneAlt;
    private String deliveryAddress;
    private LocalDateTime preferredDeliveryFrom;
    private LocalDateTime preferredDeliveryTo;
    private String deliveryFailureAction;
    private String deliveryNote;
    private Boolean cancelRequested;
    private Boolean buyerViewed;
    private Boolean sellerViewed;

    // === Delivery Confirmation ===
    private Boolean deliveryConfirmed;
    private String deliveryStatus; // ON_TIME, LATE, NOT_DELIVERED
    private LocalDateTime deliveryConfirmedAt;

    // === Marketplace RFQ Fields ===
    private String materialSource; // CUSTOMER_PROVIDED, FACTORY_PROVIDED, COMBINED
    private String services; // comma-separated: ROASTING, PACKAGING, QC, etc.
    private String productType; // ARABICA, ROBUSTA, CULI, BLEND
    private Double quotedPrice;
    private String quotedNote;
    private LocalDateTime quotedAt;
    private String unit;

    public InterGroupOrderDTO() {
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getBuyerTeamId() {
        return buyerTeamId;
    }

    public void setBuyerTeamId(String buyerTeamId) {
        this.buyerTeamId = buyerTeamId;
    }

    public String getBuyerTeamName() {
        return buyerTeamName;
    }

    public void setBuyerTeamName(String buyerTeamName) {
        this.buyerTeamName = buyerTeamName;
    }

    public String getBuyerUserId() {
        return buyerUserId;
    }

    public void setBuyerUserId(String buyerUserId) {
        this.buyerUserId = buyerUserId;
    }

    public String getBuyerUserName() {
        return buyerUserName;
    }


```
