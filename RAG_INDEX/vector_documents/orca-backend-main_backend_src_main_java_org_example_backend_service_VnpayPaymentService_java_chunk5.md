# Knowledge Document: VnpayPaymentService.java (Chunk 6/11)

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
  "chunk_index": 5,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
g nội dung chuyển khoản là: " + txnRef);
        response.put("expiresAt", LocalDateTime.now(VIETNAM_ZONE).plusMinutes(15).toString());
        return response;
    }

    @Transactional
    public Map<String, Object> confirmVirtualQrPayment(User user, String txnRef) {
        if (txnRef == null || txnRef.isBlank()) {
            throw new RuntimeException("Ma giao dich khong hop le");
        }

        PaymentTransaction transaction = paymentRepository.findByTxnRef(txnRef)
                .orElseThrow(() -> new RuntimeException("Khong tim thay giao dich"));

        if (transaction.getUser() == null || !transaction.getUser().getId().equals(user.getId())) {
            throw new RuntimeException("Ban khong co quyen xac nhan giao dich nay");
        }

        String paymentMethod = normalizePaymentMethod(transaction.getPaymentMethod());
        if ("MB_BANK".equals(paymentMethod) && !mbAllowManualConfirm) {
            Map<String, Object> pendingResponse = new LinkedHashMap<>();
            pendingResponse.put("status", "PENDING");
            pendingResponse.put("message", "Giao dịch đang chờ xác nhận tự động từ ngân hàng qua hệ thống. Vui lòng đợi trong giây lát.");
            pendingResponse.put("txnRef", txnRef);
            return pendingResponse;
        }

        if ("PAID".equalsIgnoreCase(transaction.getStatus())) {
            Map<String, Object> alreadyPaid = result(txnRef, transaction.getPlanId(), "SUCCESS", "Giao dich da duoc thanh toan", null);
            alreadyPaid.put("planName", findPlan(transaction.getPlanId()).name());
            alreadyPaid.put("amount", transaction.getAmount());
            alreadyPaid.put("paymentMethod", paymentMethod);
            return alreadyPaid;
        }

        transaction.setStatus("PAID");
        transaction.setVnpResponseCode("00");
        transaction.setVnpTransactionStatus("00");
        transaction.setVnpTransactionNo(paymentMethod + "-" + txnRef);
        transaction.setBankCode(paymentMethod + "_QR");
        transaction.setPaymentMethod(paymentMethod);
        transaction.setPaidAt(LocalDateTime.now());
        paymentRepository.save(transaction);

        activatePlan(user, transaction.getPlanId());

        Map<String, Object> response = result(txnRef, transaction.getPlanId(), "SUCCESS", paymentMethodLabel(paymentMethod) + " QR ao thanh cong", null);

```
