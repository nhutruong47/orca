# Knowledge Document: PaymentResultPage.tsx (Chunk 2/2)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/PaymentResultPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "dashboard",
  "tags": [
    "dashboard",
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, payment

## Source Code Chunk
```tsx
pexels.com/photos/30427274/pexels-photo-30427274.jpeg?auto=compress&cs=tinysrgb&w=900"
                    alt="Cà phê espresso mới pha"
                />

                <div className="payment-result-details">
                    <div>
                        <span>Mã giao dịch</span>
                        <strong>{txnRef || '-'}</strong>
                    </div>
                    <div>
                        <span>Gói AI</span>
                        <strong>{planId || '-'}</strong>
                    </div>
                    <div>
                        <span>Trạng thái</span>
                        <strong>{status || '-'}</strong>
                    </div>
                </div>

                <div className="payment-result-actions">
                    <Link to="/upgrade" className="payment-result-primary">
                        <ReceiptText size={16} />
                        Quay lại gói AI
                    </Link>
                    <Link to="/dashboard" className="payment-result-secondary">
                        Về dashboard
                    </Link>
                </div>
            </section>
        </div>
    );
}

```
