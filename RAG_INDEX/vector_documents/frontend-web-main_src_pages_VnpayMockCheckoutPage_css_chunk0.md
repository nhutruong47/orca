# Knowledge Document: VnpayMockCheckoutPage.css (Chunk 1/4)

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
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```css
.vnpay-mock-page {
    min-height: calc(100vh - var(--topbar-height));
    color: #1f2937;
    background: #f6f7fb;
    border-radius: 8px;
    overflow: hidden;
}

.vnpay-mock-page.mb-bank {
    --pay-primary: #1459c8;
    --pay-primary-dark: #0b3d90;
    --pay-soft: #eef6ff;
    --pay-header: #fff;
    --pay-header-text: #1459c8;
}

.vnpay-mock-page.vnpay {
    --pay-primary: #1459c8;
    --pay-primary-dark: #0f4198;
    --pay-soft: #eef6ff;
    --pay-header: #ffea00;
    --pay-header-text: #1459c8;
}

.vnpay-mock-header {
    height: 74px;
    display: grid;
    grid-template-columns: 160px 1fr 64px;
    align-items: center;
    padding: 0 24px;
    background: var(--pay-header);
    border-bottom: 1px solid #d8dce3;
}

.vnpay-back,
.vnpay-close {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: var(--pay-header-text);
    border: 0;
    background: transparent;
    font: inherit;
    font-weight: 800;
    cursor: pointer;
}

.vnpay-close {
    width: 42px;
    height: 42px;
    justify-content: center;
    border-radius: 8px;
    justify-self: end;
}

.vnpay-brand {
    justify-self: center;
    color: var(--pay-header-text);
    font-size: 34px;
    line-height: 1;
    font-weight: 900;
    letter-spacing: 0;
}

.vnpay-brand strong {
    margin-left: 6px;
    color: var(--pay-primary);
}

.vnpay-mock-page.vnpay .vnpay-brand strong {
    color: #ed1c24;
}

.vnpay-mock-shell {
    width: min(1040px, calc(100% - 32px));
    margin: 28px auto;
    display: grid;
    gap: 18px;
}

.payment-order-card {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 18px;
}

.payment-order-info,
.payment-qr-panel {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    box-shadow: 0 14px 34px rgba(15, 23, 42, 0.08);
}

.payment-order-info {
    padding: 22px;
}

.payment-provider {
    display: inline-flex;
    min-height: 28px;
    align-items: center;
    padding: 0 10px;
    color: var(--pay-primary-dark);
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


```
