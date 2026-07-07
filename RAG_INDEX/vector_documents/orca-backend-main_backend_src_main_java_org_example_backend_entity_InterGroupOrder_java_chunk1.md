# Knowledge Document: InterGroupOrder.java (Chunk 2/5)

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
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, production

## Source Code Chunk
```java
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
    private LocalDateTime quotedAt;

    // === Unit ===
    @Column(length = 20)
    private String unit = "kg";

    // === Delivery Profile ===
    @Column(name = "contact_phone", length = 20)
    private String contactPhone;

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

    @Column(name = "delivery_status", length = 20)
    private String deliveryStatus;

    @Column(name = "delivery_confirmed_at")
    private LocalDateTime deliveryConfirmedAt;

    @Column(name = "delivery_confirmed")
    private Boolean deliveryConfirmed = false;

    @PrePersist
    protected void onCreate() {
        this.createdAt = LocalDateTime.now();
    }

    public InterGroupOrder() {}

    // ====== Getters and Setters ======

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }

    public Team getBuyerTeam() { return buyerTeam; }
    public void setBuyerTeam(Team buyerTeam) { this.buyerTeam = buyerTeam; }

    public User getBuyerUser() { return buyerUser; }
    public void setBuyerUser(User buyerUser) { this.buyerUser = buyerUser; }

    public Team getSellerTeam() { return sellerTeam; }
    public void setSellerTeam(Team sellerTeam) { this.sellerTeam = sellerTeam; }


```
