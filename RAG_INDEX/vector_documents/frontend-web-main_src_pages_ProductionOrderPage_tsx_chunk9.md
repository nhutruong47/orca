# Knowledge Document: ProductionOrderPage.tsx (Chunk 10/19)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionOrderPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 9,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
iv>

                                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: 12, marginTop: 16, paddingTop: 16, borderTop: '1px solid var(--border)' }}>
                                    {[
                                        ['Ngay dat', order.orderDate],
                                        ['Bat dau', order.productionStartDate],
                                        ['Han noi bo', order.internalDeadline],
                                        ['Giao hang', order.customerDeliveryDate],
                                    ].map(([label, val]) => val && (
                                        <div key={label as string}>
                                            <div style={{ fontSize: 11, color: 'var(--text-muted)', marginBottom: 2 }}>{label}</div>
                                            <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-primary)' }}>
                                                {new Date(val).toLocaleDateString('vi-VN')}
                                            </div>
                                        </div>
                                    ))}
                                    {order.inputRequired && (
                                        <div>
                                            <div style={{ fontSize: 11, color: 'var(--text-muted)', marginBottom: 2 }}>Nguyen lieu can</div>
                                            <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-primary)' }}>{order.inputRequired.toLocaleString('vi-VN')} kg</div>
                                        </div>
                                    )}
                                    {order.expectedYield && (
                                        <div>
                                            <div style={{ fontSize: 11, color: 'var(--text-muted)', marginBottom: 2 }}>Ty le thu hoi</div>
                                            <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-primary)' }}>{((order.expectedYield as number) * 100).toFixed(0)}%</div>
                                        </div>
                                    )}
                                </div>

                                {(order.recipientName || order.recipientPhone) && (

```
