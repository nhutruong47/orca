# Knowledge Document: VnpayMockCheckoutPage.tsx (Chunk 5/5)

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
  "chunk_index": 4,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: payment

## Source Code Chunk
```tsx
 className="qr-placeholder">Đang tạo QR...</div>}
                        {!loading && qrPayment && (
                            <>
                                <div className="payment-qr-frame">
                                    <RealQr payload={qrPayment.qrPayload} label={config.shortLabel} />
                                </div>
                                <p className="scan-copy">
                                    <Smartphone size={16} />
                                    {config.instruction}
                                </p>
                                <div className="payment-expiry">
                                    <Clock3 size={15} />
                                    Hết hạn sau 15 phút
                                </div>
                                {openPaymentUrl && (
                                    <a className="open-wallet-link" href={openPaymentUrl}>
                                        <ExternalLink size={15} />
                                        Mở {config.shortLabel}
                                    </a>
                                )}
                            </>
                        )}

                        {error && <div className="vnpay-error">{error}</div>}

                        <button type="button" className="vnpay-confirm" onClick={handleConfirm} disabled={!qrPayment || confirming}>
                            {confirming ? 'Đang cập nhật database...' : `Tôi đã thanh toán qua ${config.shortLabel}`}
                        </button>
                        <button type="button" className="vnpay-cancel" onClick={() => navigate('/upgrade')}>
                            Hủy thanh toán
                        </button>
                    </section>
                </section>

                <section className="payment-mobile-steps" aria-label="Các bước thanh toán">
                    {['Mở ứng dụng trên điện thoại', 'Quét QR trên màn hình', 'Xác nhận để ORCA cập nhật gói'].map((step, index) => (
                        <div key={step}>
                            <CheckCircle2 size={16} />
                            <span>{index + 1}</span>
                            <strong>{step}</strong>
                        </div>
                    ))}
                </section>
            </main>
        </div>
    );
}

```
