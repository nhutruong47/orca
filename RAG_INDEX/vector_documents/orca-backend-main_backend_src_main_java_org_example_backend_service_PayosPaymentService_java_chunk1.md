# Knowledge Document: PayosPaymentService.java (Chunk 2/3)

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
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
entTransaction transaction = new PaymentTransaction();
        transaction.setTxnRef(txnRef);
        transaction.setUser(user);
        transaction.setPlanId(plan.id());
        transaction.setAmount(plan.monthlyPrice());
        transaction.setStatus("PENDING");
        transaction.setBankCode("PAYOS");
        transaction.setPaymentMethod("PAYOS");
        paymentRepository.save(transaction);

        String returnUrl = frontendUrl + "/payment-result?txnRef=" + txnRef + "&planId=" + planId;
        String cancelUrl = frontendUrl + "/upgrade";

        CreatePaymentLinkRequest paymentData = CreatePaymentLinkRequest.builder()
                .orderCode(orderCode)
                .amount(plan.monthlyPrice())
                .description("Goi " + plan.name())
                .returnUrl(returnUrl)
                .cancelUrl(cancelUrl)
                .build();

        try {
            CreatePaymentLinkResponse data = payOS.paymentRequests().create(paymentData);

            Map<String, Object> response = new LinkedHashMap<>();
            response.put("checkoutUrl", data.getCheckoutUrl());
            response.put("txnRef", txnRef);
            response.put("planId", plan.id());
            response.put("planName", plan.name());
            response.put("amount", plan.monthlyPrice());
            return response;
        } catch (Exception e) {
            throw new RuntimeException("Loi khi tao link thanh toan PayOS: " + e.getMessage(), e);
        }
    }

    @Transactional
    public Map<String, Object> handleWebhook(Map<String, Object> requestBody) {
        try {
            Webhook webhookBody = objectMapper.convertValue(requestBody, Webhook.class);
            WebhookData data = payOS.webhooks().verify(webhookBody);

            if ("00".equals(webhookBody.getCode())) {
                String orderCodeStr = String.valueOf(data.getOrderCode());
                PaymentTransaction transaction = paymentRepository.findByTxnRef(orderCodeStr).orElse(null);
                if (transaction != null && !"PAID".equals(transaction.getStatus())) {
                    transaction.setStatus("PAID");
                    transaction.setPaidAt(LocalDateTime.now());
                    transaction.setVnpResponseCode("00");
                    transaction.setVnpTransactionStatus("00");
                    paymentRepository.save(transaction);


```
