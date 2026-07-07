# Knowledge Document: Team.java (Chunk 2/6)

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
  "chunk_index": 1,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, employee

## Source Code Chunk
```java
 = "verification_reject_reason", length = 1000)
    private String verificationRejectReason;

    @Min(0)
    @Column(name = "completed_orders", nullable = false, columnDefinition = "integer default 0")
    private int completedOrders = 0;

    @Min(0)
    @Column(name = "cancelled_orders", nullable = false, columnDefinition = "integer default 0")
    private int cancelledOrders = 0;

    @Min(0)
    @Column(name = "total_orders", nullable = false, columnDefinition = "integer default 0")
    private int totalOrders = 0;

    @Min(0)
    @Column(name = "on_time_orders", nullable = false, columnDefinition = "integer default 0")
    private int onTimeOrders = 0;

    @Min(0)
    @Column(name = "late_orders", nullable = false, columnDefinition = "integer default 0")
    private int lateOrders = 0;

    @Min(0)
    @Column(name = "total_ratings", nullable = false, columnDefinition = "integer default 0")
    private int totalRatings = 0;

    @Min(0)
    @Column(name = "sum_ratings", nullable = false, columnDefinition = "double precision default 0.0")
    private double sumRatings = 0.0;

    @Column(name = "invite_code", unique = true, length = 6)
    private String inviteCode;

    // Detailed Factory Information
    @Column(name = "moq", length = 100)
    private String moq;

    @Column(name = "lead_time", length = 100)
    private String leadTime;

    @Column(name = "years_in_operation")
    private Integer yearsInOperation;

    @Column(name = "status_badge", length = 100)
    private String statusBadge;

    @Column(name = "employee_count")
    private Integer employeeCount;

    @Column(name = "factory_size", length = 100)
    private String factorySize;

    @Column(columnDefinition = "TEXT")
    private String metadata;

    @Column(name = "rating")
    private Double rating;

    @Column(name = "review_count")
    private Integer reviewCount;

    @PrePersist
    protected void onCreate() {
        this.createdAt = LocalDateTime.now();
        if (this.inviteCode == null || this.inviteCode.isEmpty()) {
            this.inviteCode = generateInviteCode();
        }
    }

    private static String generateInviteCode() {
        String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        Random rnd = new Random();
        StringBuilder sb = new StringBuilder(6);
        for (int i = 0; i < 6; i++)

```
