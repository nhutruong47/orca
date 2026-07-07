# Knowledge Document: VnpayMockCheckoutPage.css (Chunk 3/4)

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
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```css
render-error {
    width: 216px;
    height: 216px;
    display: grid;
    place-items: center;
    color: #b91c1c;
    background: #fff7f7;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 800;
}

.qr-badge {
    position: absolute;
    inset: 50% auto auto 50%;
    min-width: 46px;
    min-height: 30px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    transform: translate(-50%, -50%);
    padding: 0 6px;
    color: #fff;
    background: var(--pay-primary);
    border: 3px solid #fff;
    border-radius: 8px;
    font-size: 11px;
    font-weight: 900;
}

.scan-copy,
.payment-expiry {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    max-width: 420px;
    margin: 0;
    color: #fff;
    font-size: 14px;
    line-height: 1.45;
}

.payment-expiry {
    min-height: 32px;
    margin-top: 12px;
    padding: 0 12px;
    background: rgba(255, 255, 255, 0.16);
    border-radius: 999px;
    font-weight: 800;
}

.open-wallet-link {
    min-height: 36px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-top: 12px;
    padding: 0 14px;
    color: #fff;
    border: 1px solid rgba(255, 255, 255, 0.4);
    border-radius: 8px;
    font-size: 13px;
    font-weight: 850;
    text-decoration: none;
}

.qr-placeholder {
    width: 246px;
    height: 246px;
    display: grid;
    place-items: center;
    margin: 28px 0 18px;
    color: #64748b;
    background: #fff;
    border-radius: 8px;
    font-weight: 800;
}

.vnpay-confirm,
.vnpay-cancel {
    width: min(340px, 100%);
    min-height: 48px;
    border: 0;
    border-radius: 8px;
    font: inherit;
    font-weight: 850;
    cursor: pointer;
}

.vnpay-confirm {
    margin-top: auto;
    background: #fff;
    color: var(--pay-primary-dark);
}

.vnpay-confirm:disabled {
    opacity: 0.62;
    cursor: not-allowed;
}

.vnpay-cancel {
    margin-top: 10px;
    background: rgba(255, 255, 255, 0.14);
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

```
