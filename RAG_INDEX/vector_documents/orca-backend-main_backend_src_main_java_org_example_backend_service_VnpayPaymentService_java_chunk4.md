# Knowledge Document: VnpayPaymentService.java (Chunk 5/11)

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
  "chunk_index": 4,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
ame", paymentMethodLabel(paymentMethod));
        response.put("qrPayload", qrPayload);
        response.put("status", "PENDING");
        response.put("message", "Quet ma QR ao de thanh toan");
        response.put("expiresAt", LocalDateTime.now(VIETNAM_ZONE).plusMinutes(15).toString());
        return response;
    }

    private Map<String, Object> createMbBankQrPayment(User user, Plan plan) {
        String txnRef = "ORCAMB" + System.currentTimeMillis();
        String orderInfo = "Thanh toan goi " + plan.name();
        
        // VietQR format
        String qrCodeUrl = "https://img.vietqr.io/image/970422-" + mbAccountNumber + "-compact2.png?amount=" 
                + plan.monthlyPrice() + "&addInfo=" + urlEncode(txnRef) + "&accountName=" + urlEncode(mbAccountName);

        PaymentTransaction transaction = new PaymentTransaction();
        transaction.setTxnRef(txnRef);
        transaction.setUser(user);
        transaction.setPlanId(plan.id());
        transaction.setAmount(plan.monthlyPrice());
        transaction.setStatus("PENDING");
        transaction.setBankCode("MB_BANK_QR");
        transaction.setPaymentMethod("MB_BANK");
        transaction.setQrPayload(qrCodeUrl);
        transaction.setVnpResponseCode("PENDING");
        transaction.setVnpTransactionStatus("PENDING");
        paymentRepository.save(transaction);

        Map<String, Object> response = new LinkedHashMap<>();
        response.put("txnRef", txnRef);
        response.put("planId", plan.id());
        response.put("planName", plan.name());
        response.put("amount", plan.monthlyPrice());
        response.put("paymentMethod", "MB_BANK");
        response.put("paymentMethodName", "Chuyển khoản MB Bank");
        response.put("qrPayload", qrCodeUrl);
        response.put("qrCodeUrl", qrCodeUrl);
        response.put("status", "PENDING");
        response.put("message", "Vui lòng dùng ứng dụng ngân hàng quét mã QR để chuyển khoản. Nhập đúng nội dung chuyển khoản là: " + txnRef);
        response.put("expiresAt", LocalDateTime.now(VIETNAM_ZONE).plusMinutes(15).toString());
        return response;
    }

    @Transactional
    public Map<String, Object> confirmVirtualQrPayment(User user, String txnRef) {
        if (txnRef == null || txnRef.isBlank()) {
            throw new RuntimeException("Ma giao dich khong hop le");
        }


```
