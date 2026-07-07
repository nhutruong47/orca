# Knowledge Document: VnpayPaymentService.java (Chunk 9/11)

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
  "chunk_index": 8,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment

## Source Code Chunk
```java
               && value != null
                    && !key.equals("vnp_SecureHash")
                    && !key.equals("vnp_SecureHashType")) {
                signedParams.put(key, value);
            }
        });

        String hashData = buildQuery(signedParams, true);
        String expectedHash = hmacSha512(hashSecret, hashData);
        return expectedHash.equalsIgnoreCase(receivedHash);
    }



    private String buildQuery(Map<String, String> params, boolean encode) {
        StringBuilder builder = new StringBuilder();
        params.forEach((key, value) -> {
            if (value == null || value.isBlank()) return;
            if (!builder.isEmpty()) {
                builder.append('&');
            }
            if (encode) {
                builder.append(urlEncode(key)).append('=').append(urlEncode(value));
            } else {
                builder.append(key).append('=').append(value);
            }
        });
        return builder.toString();
    }

    private String urlEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    private String hmacSha512(String key, String data) {
        if (key == null || key.isBlank()) {
            throw new IllegalStateException("Missing VNPAY hash secret");
        }
        try {
            Mac hmac = Mac.getInstance("HmacSHA512");
            hmac.init(new SecretKeySpec(key.getBytes(StandardCharsets.UTF_8), "HmacSHA512"));
            byte[] bytes = hmac.doFinal(data.getBytes(StandardCharsets.UTF_8));
            StringBuilder hash = new StringBuilder();
            for (byte item : bytes) {
                hash.append(String.format("%02x", item));
            }
            return hash.toString();
        } catch (Exception ex) {
            throw new IllegalStateException("Cannot sign VNPAY request", ex);
        }
    }

    private Plan findPlan(String planId) {
        return PLANS.stream()
                .filter(plan -> plan.id().equalsIgnoreCase(planId))
                .findFirst()
                .orElseThrow(() -> new RuntimeException("Goi AI khong hop le"));
    }



    private String normalizePaymentMethod(String method) {
        String normalized = method == null ? "VNPAY" : method.trim().toUpperCase(Locale.ROOT);
        if (!List.of("MB_BANK", "VNPAY").contains(normalized)) {

```
