# Knowledge Document: VnpayMockCheckoutPage.tsx (Chunk 4/5)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/VnpayMockCheckoutPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "payment",
  "tags": [
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```tsx
ong>
                </div>
                <button type="button" className="vnpay-close" onClick={() => navigate('/upgrade')} title="Hủy thanh toán">
                    <X size={20} />
                </button>
            </header>

            <main className="vnpay-mock-shell">
                <section className="payment-order-card">
                    <aside className="payment-order-info">
                        <span className="payment-provider">{config.label}</span>
                        <h1>Thông tin đơn hàng</h1>
                        <dl>
                            <div>
                                <dt>Nhà cung cấp</dt>
                                <dd>ORCA AI</dd>
                            </div>
                            <div>
                                <dt>Gói nâng cấp</dt>
                                <dd>{plan.name}</dd>
                            </div>
                            <div>
                                <dt>Mã đơn hàng</dt>
                                <dd>{qrPayment?.txnRef || 'Đang tạo...'}</dd>
                            </div>
                            <div>
                                <dt>Số tiền</dt>
                                <dd className="payment-amount">{formatCurrency(qrPayment?.amount ?? plan.amount)}</dd>
                            </div>
                        </dl>
                        <button type="button" className="copy-txn" onClick={handleCopy} disabled={!qrPayment}>
                            <Copy size={15} />
                            {copied ? 'Đã sao chép' : 'Sao chép mã đơn'}
                        </button>
                    </aside>

                    <section className="payment-qr-panel">
                        <div className="payment-qr-head">
                            <QrCode size={22} />
                            <h2>Quét mã QR để thanh toán</h2>
                        </div>

                        {loading && <div className="qr-placeholder">Đang tạo QR...</div>}
                        {!loading && qrPayment && (
                            <>
                                <div className="payment-qr-frame">
                                    <RealQr payload={qrPayment.qrPayload} label={config.shortLabel} />
                                </div>
                                <p className="scan-copy">

```
