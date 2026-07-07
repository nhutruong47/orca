# Knowledge Document: PaymentController.java (Chunk 3/3)

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
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, security, authentication

## Source Code Chunk
```java
result)));
        return new ResponseEntity<>(headers, HttpStatus.FOUND);
    }

    @GetMapping("/vnpay/ipn")
    public ResponseEntity<Map<String, Object>> handleVnpayIpn(@RequestParam Map<String, String> params) {
        Map<String, Object> result = vnpayPaymentService.handleIpn(params);
        return ResponseEntity.ok(Map.of(
                "RspCode", result.getOrDefault("RspCode", "99"),
                "Message", result.getOrDefault("Message", "Unknown error")
        ));
    }
}

```
