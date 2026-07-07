# Knowledge Document: PaymentController.java (Chunk 1/3)

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
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, security, authentication

## Source Code Chunk
```java
package org.example.backend.controller;

import jakarta.servlet.http.HttpServletRequest;
import org.example.backend.entity.User;
import org.example.backend.service.VnpayPaymentService;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.net.URI;
import java.util.Map;

@RestController
@RequestMapping("/api/payments")
public class PaymentController {

    private final VnpayPaymentService vnpayPaymentService;

    public PaymentController(VnpayPaymentService vnpayPaymentService) {
        this.vnpayPaymentService = vnpayPaymentService;
    }

    @PostMapping("/vnpay/create")
    public ResponseEntity<Map<String, Object>> createVnpayPayment(
            @AuthenticationPrincipal User user,
            @RequestBody Map<String, String> body,
            HttpServletRequest request) {
        return ResponseEntity.ok(vnpayPaymentService.createPayment(
                user,
                body.get("planId"),
                body.get("bankCode"),
                request
        ));
    }

    @PostMapping("/mock/transfer")
    public ResponseEntity<Map<String, Object>> createMockTransfer(
            @AuthenticationPrincipal User user,
            @RequestBody Map<String, String> body) {
        return ResponseEntity.ok(vnpayPaymentService.createMockTransfer(
                user,
                body.get("planId"),
                body.get("method")
        ));
    }

    @PostMapping("/virtual-qr/create")
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

```
