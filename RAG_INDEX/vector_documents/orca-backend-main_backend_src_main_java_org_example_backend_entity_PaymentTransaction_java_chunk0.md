# Knowledge Document: PaymentTransaction.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/PaymentTransaction.java",
  "language": "java",
  "module": "entity",
  "business_domain": "payment",
  "tags": [
    "payment"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```java
package org.example.backend.entity;

import jakarta.persistence.*;

import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "payment_transactions")
public class PaymentTransaction {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(updatable = false, nullable = false)
    private UUID id;

    @Column(name = "txn_ref", nullable = false, unique = true, length = 100)
    private String txnRef;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @Column(name = "plan_id", nullable = false, length = 32)
    private String planId;

    @Column(nullable = false)
    private long amount;

    @Column(nullable = false, length = 24)
    private String status = "PENDING";

    @Column(name = "vnp_transaction_no")
    private String vnpTransactionNo;

    @Column(name = "vnp_response_code")
    private String vnpResponseCode;

    @Column(name = "vnp_transaction_status")
    private String vnpTransactionStatus;

    @Column(name = "bank_code")
    private String bankCode;

    @Column(name = "payment_method", length = 24)
    private String paymentMethod;

    @Column(name = "qr_payload", length = 512)
    private String qrPayload;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "paid_at")
    private LocalDateTime paidAt;

    @PrePersist
    protected void onCreate() {
        this.createdAt = LocalDateTime.now();
    }

    public UUID getId() {
        return id;
    }

    public String getTxnRef() {
        return txnRef;
    }

    public void setTxnRef(String txnRef) {
        this.txnRef = txnRef;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public String getPlanId() {
        return planId;
    }

    public void setPlanId(String planId) {
        this.planId = planId;
    }

    public long getAmount() {
        return amount;
    }

    public void setAmount(long amount) {
        this.amount = amount;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getVnpTransactionNo() {
        return vnpTransactionNo;
    }


```
