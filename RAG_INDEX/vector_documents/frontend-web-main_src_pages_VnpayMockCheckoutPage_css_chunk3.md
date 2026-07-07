# Knowledge Document: VnpayMockCheckoutPage.css (Chunk 4/4)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/VnpayMockCheckoutPage.css",
  "language": "css",
  "module": "pages",
  "business_domain": "payment",
  "tags": [
    "payment"
  ],
  "logical_type": "Generic",
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```css
255, 0.14);
    color: #fff;
}

.vnpay-error {
    width: min(420px, 100%);
    margin: 16px 0;
    padding: 10px 12px;
    border-radius: 8px;
    background: #fee2e2;
    color: #b91c1c;
    font-size: 13px;
    text-align: left;
}

.payment-mobile-steps {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 10px;
}

.payment-mobile-steps div {
    min-height: 74px;
    display: grid;
    grid-template-columns: 18px 26px 1fr;
    align-items: center;
    gap: 8px;
    padding: 12px;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
}

.payment-mobile-steps svg {
    color: var(--pay-primary);
}

.payment-mobile-steps span {
    width: 26px;
    height: 26px;
    display: grid;
    place-items: center;
    color: #fff;
    background: var(--pay-primary);
    border-radius: 999px;
    font-size: 12px;
    font-weight: 900;
}

.payment-mobile-steps strong {
    color: #334155;
    font-size: 13px;
    line-height: 1.35;
}

@media (max-width: 860px) {
    .vnpay-mock-header {
        grid-template-columns: 120px 1fr 48px;
        padding: 0 12px;
    }

    .vnpay-brand {
        font-size: 28px;
    }

    .payment-order-card {
        grid-template-columns: 1fr;
    }

    .payment-qr-panel {
        min-height: 520px;
    }

    .payment-mobile-steps {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 520px) {
    .vnpay-mock-shell {
        width: calc(100% - 20px);
        margin-block: 18px;
    }

    .vnpay-mock-header {
        grid-template-columns: 44px 1fr 44px;
    }

    .vnpay-back span {
        display: none;
    }

    .payment-order-info,
    .payment-qr-panel {
        padding: 18px;
    }

    .payment-qr-frame,
    .qr-placeholder {
        width: 226px;
        height: 226px;
    }

    .real-qr,
    .qr-render-error {
        width: 198px;
        height: 198px;
    }
}

```
