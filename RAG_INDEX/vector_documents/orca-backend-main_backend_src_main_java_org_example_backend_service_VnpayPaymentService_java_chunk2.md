# Knowledge Document: VnpayPaymentService.java (Chunk 3/11)

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
  "chunk_index": 2,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
");
        params.put("vnp_Locale", "vn");
        params.put("vnp_ReturnUrl", returnUrl);
        params.put("vnp_IpAddr", clientIp(request));
        params.put("vnp_CreateDate", now.format(VNPAY_TIME_FORMAT));
        params.put("vnp_ExpireDate", expireAt.format(VNPAY_TIME_FORMAT));
        if (bankCode != null && !bankCode.isBlank()) {
            params.put("vnp_BankCode", bankCode.trim());
        }

        String hashData = buildQuery(params, true);
        String query = buildQuery(params, true);
        String secureHash = hmacSha512(hashSecret, hashData);
        String paymentUrl = payUrl + "?" + query + "&vnp_SecureHash=" + secureHash;

        Map<String, Object> response = new LinkedHashMap<>();
        response.put("paymentUrl", paymentUrl);
        response.put("txnRef", txnRef);
        response.put("planId", plan.id());
        response.put("planName", plan.name());
        response.put("amount", plan.monthlyPrice());
        return response;
    }

    @Transactional
    public Map<String, Object> createMockTransfer(User user, String planId, String method) {
        Plan plan = findPlan(planId);
        String paymentMethod = normalizePaymentMethod(method);
        String txnRef = paymentMethod + System.currentTimeMillis();

        PaymentTransaction transaction = new PaymentTransaction();
        transaction.setTxnRef(txnRef);
        transaction.setUser(user);
        transaction.setPlanId(plan.id());
        transaction.setAmount(plan.monthlyPrice());
        transaction.setStatus("PAID");
        transaction.setVnpResponseCode("00");
        transaction.setVnpTransactionStatus("00");
        transaction.setVnpTransactionNo(paymentMethod + "-" + txnRef);
        transaction.setBankCode(paymentMethod + "_QR");
        transaction.setPaymentMethod(paymentMethod);
        transaction.setQrPayload(buildVirtualQrPayload(paymentMethod, txnRef, plan));
        transaction.setPaidAt(LocalDateTime.now());
        paymentRepository.save(transaction);

        activatePlan(user, plan.id());

        Map<String, Object> response = result(txnRef, plan.id(), "SUCCESS", paymentMethodLabel(paymentMethod) + " QR ao thanh cong", null);
        response.put("planName", plan.name());
        response.put("amount", plan.monthlyPrice());
        response.put("paymentMethod", paymentMethod);
        return response;
    }

    @Transactional

```
