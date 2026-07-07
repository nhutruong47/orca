# Knowledge Document: ProductionOrderDTO.java (Chunk 1/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ProductionOrderDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
package org.example.backend.dto;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;

public class ProductionOrderDTO {
    private String id;
    private String teamId;
    private String orderCode;
    private String title;
    private String description;
    private String customerName;
    private String productType;
    private String processType;
    private String roastLevel;
    private String packageSize;
    private Integer totalPackages;
    private Double outputTarget;
    private Double expectedYield;
    private Double expectedLoss;
    private Double inputRequired;
    private String unit;
    private LocalDate orderDate;
    private LocalDate confirmDate;
    private LocalDate productionStartDate;
    private LocalDateTime internalDeadline;
    private LocalDate customerDeliveryDate;
    private Integer safetyBufferDays;
    private String recipientName;
    private String recipientPhone;
    private String shippingNote;
    private String status;
    private Double completedQuantity;
    private Double progressPercent;
    private Double remainingQuantity;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    
    private String contactPhoneAlt;
    private String deliveryAddress;
    private LocalDateTime preferredDeliveryFrom;
    private LocalDateTime preferredDeliveryTo;
    private String deliveryFailureAction;
    private String deliveryNote;
    private Boolean cancelRequested;
    private Boolean buyerViewed;
    private Boolean sellerViewed;

    // Getters and setters
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getTeamId() { return teamId; }
    public void setTeamId(String teamId) { this.teamId = teamId; }
    public String getOrderCode() { return orderCode; }
    public void setOrderCode(String orderCode) { this.orderCode = orderCode; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getCustomerName() { return customerName; }
    public void setCustomerName(String customerName) { this.customerName = customerName; }

```
