# Knowledge Document: VnpayMockCheckoutPage.css (Chunk 2/4)

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
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```css
ary-dark);
    background: var(--pay-soft);
    border-radius: 999px;
    font-size: 12px;
    font-weight: 800;
}

.payment-order-info h1 {
    margin: 18px 0;
    color: #111827;
    font-size: 22px;
    line-height: 1.2;
}

.payment-order-info dl {
    display: grid;
    gap: 14px;
    margin: 0;
}

.payment-order-info dl div {
    padding-bottom: 14px;
    border-bottom: 1px solid #edf1f5;
}

.payment-order-info dt {
    margin-bottom: 5px;
    color: #64748b;
    font-size: 12px;
    font-weight: 800;
}

.payment-order-info dd {
    margin: 0;
    color: #111827;
    font-size: 14px;
    font-weight: 850;
    word-break: break-word;
}

.payment-amount {
    color: var(--pay-primary) !important;
    font-size: 24px !important;
}

.copy-txn {
    width: 100%;
    min-height: 42px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-top: 18px;
    border: 1px solid #d7dee8;
    border-radius: 8px;
    background: #fff;
    color: #334155;
    font: inherit;
    font-size: 13px;
    font-weight: 800;
    cursor: pointer;
}

.copy-txn:disabled {
    opacity: 0.55;
    cursor: not-allowed;
}

.payment-qr-panel {
    min-height: 560px;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 28px;
    text-align: center;
    background:
        linear-gradient(135deg, color-mix(in srgb, var(--pay-primary) 90%, #ffffff), var(--pay-primary-dark));
}

.payment-qr-head {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    color: #fff;
}

.payment-qr-head h2 {
    margin: 0;
    font-size: 24px;
    line-height: 1.2;
}

.payment-qr-frame {
    position: relative;
    width: 246px;
    height: 246px;
    display: grid;
    place-items: center;
    margin: 28px 0 18px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 18px 42px rgba(15, 23, 42, 0.18);
}

.real-qr {
    width: 216px;
    height: 216px;
    display: block;
}

.qr-render-error {
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

```
