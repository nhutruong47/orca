# Knowledge Document: VnpayPaymentService.java (Chunk 7/11)

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
  "chunk_index": 6,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
tion.setBankCode(paymentMethod + "_QR");
        transaction.setPaymentMethod(paymentMethod);
        transaction.setPaidAt(LocalDateTime.now());
        paymentRepository.save(transaction);

        activatePlan(user, transaction.getPlanId());

        Map<String, Object> response = result(txnRef, transaction.getPlanId(), "SUCCESS", paymentMethodLabel(paymentMethod) + " QR ao thanh cong", null);
        response.put("planName", findPlan(transaction.getPlanId()).name());
        response.put("amount", transaction.getAmount());
        response.put("paymentMethod", paymentMethod);
        return response;
    }

    @Transactional
    public Map<String, Object> handleReturn(Map<String, String> params) {
        return processVnpayResult(params, false);
    }

    @Transactional
    public Map<String, Object> handleIpn(Map<String, String> params) {
        return processVnpayResult(params, true);
    }

    @Transactional
    public Map<String, Object> handleMbBankReturn(Map<String, String> params) {
        return new HashMap<>(); // Thường không dùng return trực tiếp cho chuyển khoản ngân hàng
    }

    @Transactional
    public Map<String, Object> handleMbBankIpn(Map<String, Object> body) {
        // Có thể tích hợp webhook SePay/Casso ở đây
        return new HashMap<>();
    }

    public String buildFrontendRedirect(Map<String, Object> result) {
        return UriComponentsBuilder.fromUriString(frontendUrl)
                .path("/payment-result")
                .queryParam("status", result.get("status"))
                .queryParam("txnRef", result.get("txnRef"))
                .queryParam("planId", result.get("planId"))
                .queryParam("message", result.get("message"))
                .build()
                .encode(StandardCharsets.UTF_8)
                .toUriString();
    }

    private Map<String, Object> processVnpayResult(Map<String, String> params, boolean ipn) {
        String txnRef = params.get("vnp_TxnRef");
        PaymentTransaction transaction = paymentRepository.findByTxnRef(txnRef)
                .orElse(null);

        if (!verifySecureHash(params)) {
            return result(txnRef, null, "INVALID_SIGNATURE", "Chu ky VNPAY khong hop le", ipn ? "97" : null);
        }
        if (transaction == null) {
            return result(txnRef, null, "NOT_FOUND", "Khong tim thay giao dich", ipn ? "01" : null);
        }


```
