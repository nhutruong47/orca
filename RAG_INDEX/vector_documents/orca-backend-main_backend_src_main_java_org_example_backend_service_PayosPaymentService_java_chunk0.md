# Knowledge Document: PayosPaymentService.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/PayosPaymentService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "payment"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.entity.PaymentTransaction;
import org.example.backend.entity.User;
import org.example.backend.repository.PaymentTransactionRepository;
import org.example.backend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import vn.payos.PayOS;
import vn.payos.model.v2.paymentRequests.CreatePaymentLinkRequest;
import vn.payos.model.v2.paymentRequests.CreatePaymentLinkResponse;
import vn.payos.model.webhooks.Webhook;
import vn.payos.model.webhooks.WebhookData;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.time.LocalDateTime;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@Service
public class PayosPaymentService {

    private final PayOS payOS;
    private final PaymentTransactionRepository paymentRepository;
    private final UserRepository userRepository;
    private final ObjectMapper objectMapper;

    @Value("${app.frontend.url:http://localhost:5173}")
    private String frontendUrl;

    private static final List<Plan> PLANS = List.of(
            new Plan("professional", "Professional", 129000, 500000),
            new Plan("enterprise", "Enterprise", 249000, 1500000)
    );

    public PayosPaymentService(PayOS payOS, PaymentTransactionRepository paymentRepository, UserRepository userRepository, ObjectMapper objectMapper) {
        this.payOS = payOS;
        this.paymentRepository = paymentRepository;
        this.userRepository = userRepository;
        this.objectMapper = objectMapper;
    }

    @Transactional
    public Map<String, Object> createPaymentLink(User user, String planId) {
        Plan plan = findPlan(planId);
        long orderCode = System.currentTimeMillis() / 1000 + (long)(Math.random() * 10000);
        String txnRef = String.valueOf(orderCode);

        PaymentTransaction transaction = new PaymentTransaction();
        transaction.setTxnRef(txnRef);
        transaction.setUser(user);
        transaction.setPlanId(plan.id());
        transaction.setAmount(plan.monthlyPrice());
        transaction.setStatus("PENDING");
        transaction.setBankCode("PAYOS");
        transaction.setPaymentMethod("PAYOS");
        paymentRepository.save(transaction);


```
