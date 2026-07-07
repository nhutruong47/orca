# Knowledge Document: ProductionOrder.java (Chunk 2/6)

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
  "chunk_index": 1,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```java
eliveryDate;

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
    @Column(nullable = false)
    private String status = "PENDING";

    @Column(name = "completed_quantity")
    private Double completedQuantity;

    @Column(name = "contact_phone_alt", length = 20)
    private String contactPhoneAlt;

    @Column(name = "delivery_address")
    private String deliveryAddress;

    @Column(name = "preferred_delivery_from")
    private LocalDateTime preferredDeliveryFrom;

    @Column(name = "preferred_delivery_to")
    private LocalDateTime preferredDeliveryTo;

    @Column(name = "delivery_failure_action", length = 30)
    private String deliveryFailureAction;

    @Column(name = "delivery_note", columnDefinition = "TEXT")
    private String deliveryNote;

    @Column(name = "cancel_requested")
    private Boolean cancelRequested = false;

    @Column(name = "buyer_viewed")
    private Boolean buyerViewed = true;

    @Column(name = "seller_viewed")
    private Boolean sellerViewed = false;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    @PrePersist
    protected void onCreate() {
        this.createdAt = LocalDateTime.now();
        this.updatedAt = this.createdAt;
        if (this.orderCode == null || this.orderCode.isBlank()) {
            this.orderCode = "PO-" + System.currentTimeMillis();
        }
        if (this.safetyBufferDays == null) {
            this.safetyBufferDays = 2;
        }
        calculateInternalDeadline();
    }

    @PreUpdate
    protected void onUpdate() {
        this.updatedAt = LocalDateTime.now();
        calculateInternalDeadline();
    }

    private void calculateInternalDeadline() {
        if (this.customerDeliveryDate != null && this.safetyBufferDays != null) {
            this.internalDeadline = this.customerDeliveryDate
                    .atStartOfDay()
                    .minusDays(this.safetyBufferDays);
        }
    }


```
