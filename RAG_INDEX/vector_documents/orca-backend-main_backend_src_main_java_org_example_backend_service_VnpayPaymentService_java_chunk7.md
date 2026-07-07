# Knowledge Document: VnpayPaymentService.java (Chunk 8/11)

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
  "chunk_index": 7,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
action transaction = paymentRepository.findByTxnRef(txnRef)
                .orElse(null);

        if (!verifySecureHash(params)) {
            return result(txnRef, null, "INVALID_SIGNATURE", "Chu ky VNPAY khong hop le", ipn ? "97" : null);
        }
        if (transaction == null) {
            return result(txnRef, null, "NOT_FOUND", "Khong tim thay giao dich", ipn ? "01" : null);
        }

        long vnpAmount = parseLong(params.get("vnp_Amount"));
        if (vnpAmount != transaction.getAmount() * 100) {
            return result(txnRef, transaction.getPlanId(), "INVALID_AMOUNT", "So tien khong khop", ipn ? "04" : null);
        }

        String responseCode = params.get("vnp_ResponseCode");
        String transactionStatus = params.get("vnp_TransactionStatus");
        boolean paid = "00".equals(responseCode) && "00".equals(transactionStatus);

        transaction.setVnpResponseCode(responseCode);
        transaction.setVnpTransactionStatus(transactionStatus);
        transaction.setVnpTransactionNo(params.get("vnp_TransactionNo"));

        if (paid) {
            transaction.setStatus("PAID");
            transaction.setPaidAt(LocalDateTime.now());
            activatePlan(transaction.getUser(), transaction.getPlanId());
        } else {
            transaction.setStatus("FAILED");
        }
        paymentRepository.save(transaction);

        return result(
                txnRef,
                transaction.getPlanId(),
                paid ? "SUCCESS" : "FAILED",
                paid ? "Thanh toan thanh cong" : "Thanh toan khong thanh cong",
                ipn ? "00" : null
        );
    }

    private boolean verifySecureHash(Map<String, String> params) {
        String receivedHash = params.get("vnp_SecureHash");
        if (receivedHash == null || receivedHash.isBlank()) {
            return false;
        }

        Map<String, String> signedParams = new TreeMap<>();
        params.forEach((key, value) -> {
            if (key != null
                    && value != null
                    && !key.equals("vnp_SecureHash")
                    && !key.equals("vnp_SecureHashType")) {
                signedParams.put(key, value);
            }
        });

        String hashData = buildQuery(signedParams, true);
        String expectedHash = hmacSha512(hashSecret, hashData);
        return expectedHash.equalsIgnoreCase(receivedHash);

```
