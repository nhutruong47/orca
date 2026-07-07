# Knowledge Document: PaymentController.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/PaymentController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "payment",
  "tags": [
    "payment",
    "security",
    "authentication"
  ],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, security, authentication

## Source Code Chunk
```java
   public ResponseEntity<Map<String, Object>> createVirtualQrPayment(
            @AuthenticationPrincipal User user,
            @RequestBody Map<String, String> body) {
        return ResponseEntity.ok(vnpayPaymentService.createVirtualQrPayment(
                user,
                body.get("planId"),
                body.get("method")
        ));
    }

    @PostMapping("/virtual-qr/confirm")
    public ResponseEntity<Map<String, Object>> confirmVirtualQrPayment(
            @AuthenticationPrincipal User user,
            @RequestBody Map<String, String> body) {
        return ResponseEntity.ok(vnpayPaymentService.confirmVirtualQrPayment(user, body.get("txnRef")));
    }

    @GetMapping("/mbbank/return")
    public ResponseEntity<Void> handleMbBankReturn(@RequestParam Map<String, String> params) {
        Map<String, Object> result = vnpayPaymentService.handleMbBankReturn(params);
        HttpHeaders headers = new HttpHeaders();
        // MB Bank không có return url theo chuẩn ví điện tử, có thể chuyển về trang frontend báo đang xử lý
        headers.setLocation(URI.create(vnpayPaymentService.buildFrontendRedirect(result)));
        return new ResponseEntity<>(headers, HttpStatus.FOUND);
    }

    @PostMapping("/mbbank/ipn")
    public ResponseEntity<Map<String, Object>> handleMbBankIpn(@RequestBody Map<String, Object> body) {
        Map<String, Object> result = vnpayPaymentService.handleMbBankIpn(body);
        return ResponseEntity.ok(Map.of(
                "resultCode", "SUCCESS".equals(result.get("status")) ? 0 : 1,
                "message", result.getOrDefault("message", "Processed")
        ));
    }

    @GetMapping("/vnpay/return")
    public ResponseEntity<Void> handleVnpayReturn(@RequestParam Map<String, String> params) {
        Map<String, Object> result = vnpayPaymentService.handleReturn(params);
        HttpHeaders headers = new HttpHeaders();
        headers.setLocation(URI.create(vnpayPaymentService.buildFrontendRedirect(result)));
        return new ResponseEntity<>(headers, HttpStatus.FOUND);
    }

    @GetMapping("/vnpay/ipn")
    public ResponseEntity<Map<String, Object>> handleVnpayIpn(@RequestParam Map<String, String> params) {
        Map<String, Object> result = vnpayPaymentService.handleIpn(params);
        return ResponseEntity.ok(Map.of(
                "RspCode", result.getOrDefault("RspCode", "99"),

```
