# Knowledge Document: VnpayPaymentService.java (Chunk 4/11)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/VnpayPaymentService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "payment"
  ],
  "logical_type": "Service",
  "chunk_index": 3,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
transaction);

        activatePlan(user, plan.id());

        Map<String, Object> response = result(txnRef, plan.id(), "SUCCESS", paymentMethodLabel(paymentMethod) + " QR ao thanh cong", null);
        response.put("planName", plan.name());
        response.put("amount", plan.monthlyPrice());
        response.put("paymentMethod", paymentMethod);
        return response;
    }

    @Transactional
    public Map<String, Object> createVirtualQrPayment(User user, String planId, String method) {
        Plan plan = findPlan(planId);
        String paymentMethod = normalizePaymentMethod(method);
        if ("MB_BANK".equals(paymentMethod)) {
            if (mbAllowManualConfirm) {
                return createMbBankQrPayment(user, plan);
            }
            return createLocalVirtualQrPayment(user, plan, paymentMethod);
        }

        return createLocalVirtualQrPayment(user, plan, paymentMethod);
    }

    private Map<String, Object> createLocalVirtualQrPayment(User user, Plan plan, String paymentMethod) {
        String txnRef = paymentMethod + System.currentTimeMillis();
        String qrPayload = buildVirtualQrPayload(paymentMethod, txnRef, plan);

        PaymentTransaction transaction = new PaymentTransaction();
        transaction.setTxnRef(txnRef);
        transaction.setUser(user);
        transaction.setPlanId(plan.id());
        transaction.setAmount(plan.monthlyPrice());
        transaction.setStatus("PENDING");
        transaction.setBankCode(paymentMethod + "_QR");
        transaction.setPaymentMethod(paymentMethod);
        transaction.setQrPayload(qrPayload);
        paymentRepository.save(transaction);

        Map<String, Object> response = new LinkedHashMap<>();
        response.put("txnRef", txnRef);
        response.put("planId", plan.id());
        response.put("planName", plan.name());
        response.put("amount", plan.monthlyPrice());
        response.put("paymentMethod", paymentMethod);
        response.put("paymentMethodName", paymentMethodLabel(paymentMethod));
        response.put("qrPayload", qrPayload);
        response.put("status", "PENDING");
        response.put("message", "Quet ma QR ao de thanh toan");
        response.put("expiresAt", LocalDateTime.now(VIETNAM_ZONE).plusMinutes(15).toString());
        return response;
    }

    private Map<String, Object> createMbBankQrPayment(User user, Plan plan) {

```
