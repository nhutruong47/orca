# Knowledge Document: api.ts (Chunk 2/2)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/services/api.ts",
  "language": "ts",
  "module": "services",
  "business_domain": "payment",
  "tags": [
    "payment",
    "authorization"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in services.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, authorization

## Source Code Chunk
```ts
ông ở trang auth
            if (!window.location.pathname.includes('/login') && !window.location.pathname.includes('/register')) {
                window.location.href = '/login';
            }
        }

        if (isPaymentRequiredError(error)) {
            error.code = 'PAYMENT_REQUIRED';
            if (error.response?.data) {
                error.response.data.error = 'PAYMENT_REQUIRED';
                error.response.data.message = 'Gói miễn phí đã hết hạn.';
            }
            window.dispatchEvent(new CustomEvent('payment-required'));
            return Promise.reject(error);
        }

        return Promise.reject(sanitizeApiError(error));
    }
);

export default api;

```
