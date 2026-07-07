# Knowledge Document: PaymentTransactionRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/PaymentTransactionRepository.java",
  "language": "java",
  "module": "repository",
  "business_domain": "payment",
  "tags": [
    "payment"
  ],
  "logical_type": "Repository",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Repository in repository.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```java
package org.example.backend.repository;

import org.example.backend.entity.PaymentTransaction;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;
import java.util.UUID;

public interface PaymentTransactionRepository extends JpaRepository<PaymentTransaction, UUID> {
    Optional<PaymentTransaction> findByTxnRef(String txnRef);
}

```
