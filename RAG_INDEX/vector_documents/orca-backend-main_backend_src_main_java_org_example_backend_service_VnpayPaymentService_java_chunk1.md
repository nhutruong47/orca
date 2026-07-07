# Knowledge Document: VnpayPaymentService.java (Chunk 2/11)

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
  "chunk_index": 1,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
e:DEMOV210}")
    private String tmnCode;

    @Value("${vnpay.hash-secret:}")
    private String hashSecret;

    @Value("${vnpay.return-url:http://localhost:8080/api/payments/vnpay/return}")
    private String returnUrl;

    @Value("${app.frontend.url:http://localhost:5173}")
    private String frontendUrl;

    @Value("${mbbank.account-number:0999999999}")
    private String mbAccountNumber;

    @Value("${mbbank.account-name:NGUYEN VAN A}")
    private String mbAccountName;

    @Value("${mbbank.allow-manual-confirm:true}")
    private boolean mbAllowManualConfirm;

    public VnpayPaymentService(PaymentTransactionRepository paymentRepository, UserRepository userRepository) {
        this.paymentRepository = paymentRepository;
        this.userRepository = userRepository;
    }

    @Transactional
    public Map<String, Object> createPayment(User user, String planId, String bankCode, HttpServletRequest request) {
        Plan plan = findPlan(planId);
        String txnRef = "ORCA" + System.currentTimeMillis();

        PaymentTransaction transaction = new PaymentTransaction();
        transaction.setTxnRef(txnRef);
        transaction.setUser(user);
        transaction.setPlanId(plan.id());
        transaction.setAmount(plan.monthlyPrice());
        transaction.setBankCode(bankCode);
        transaction.setPaymentMethod("VNPAY");
        paymentRepository.save(transaction);

        LocalDateTime now = LocalDateTime.now(VIETNAM_ZONE);
        LocalDateTime expireAt = now.plusMinutes(15);

        Map<String, String> params = new TreeMap<>();
        params.put("vnp_Version", "2.1.0");
        params.put("vnp_Command", "pay");
        params.put("vnp_TmnCode", tmnCode);
        params.put("vnp_Amount", String.valueOf(plan.monthlyPrice() * 100));
        params.put("vnp_CurrCode", "VND");
        params.put("vnp_TxnRef", txnRef);
        params.put("vnp_OrderInfo", "Thanh toan goi " + plan.name() + " cho ORCA");
        params.put("vnp_OrderType", "other");
        params.put("vnp_Locale", "vn");
        params.put("vnp_ReturnUrl", returnUrl);
        params.put("vnp_IpAddr", clientIp(request));
        params.put("vnp_CreateDate", now.format(VNPAY_TIME_FORMAT));
        params.put("vnp_ExpireDate", expireAt.format(VNPAY_TIME_FORMAT));
        if (bankCode != null && !bankCode.isBlank()) {
            params.put("vnp_BankCode", bankCode.trim());

```
