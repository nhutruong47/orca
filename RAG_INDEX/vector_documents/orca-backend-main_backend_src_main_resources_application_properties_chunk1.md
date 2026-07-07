# Knowledge Document: application.properties (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/resources/application.properties",
  "language": "properties",
  "module": "resources",
  "business_domain": "admin",
  "tags": [
    "admin",
    "payment",
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in resources.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, payment, security

## Source Code Chunk
```properties

ai.v2.service-url=${AI_V2_SERVICE_URL:http://127.0.0.1:8000}

# ===== VNPAY Sandbox =====
app.frontend.url=http://localhost:5173
vnpay.pay-url=${VNPAY_PAY_URL:https://sandbox.vnpayment.vn/paymentv2/vpcpay.html}
vnpay.tmn-code=${VNPAY_TMN_CODE:DEMOV210}
vnpay.hash-secret=${VNPAY_HASH_SECRET:}
vnpay.return-url=${VNPAY_RETURN_URL:http://localhost:8080/api/payments/vnpay/return}

# ===== PayOS =====
payos.client-id=${PAYOS_CLIENT_ID:888e5af2-f3c1-40f1-8249-b54d9089eabc}
payos.api-key=${PAYOS_API_KEY:7dcf2463-f99c-4c51-92c8-1c8d3b6f8512}
payos.checksum-key=${PAYOS_CHECKSUM_KEY:0cf889febacff30e5bf36527af3b537572cba0b345797a7c50c935e68c4b3c03}

```
