# Knowledge Document: ProductionOrderPage.tsx (Chunk 11/19)

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
  "chunk_index": 10,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
oi</div>
                                            <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-primary)' }}>{((order.expectedYield as number) * 100).toFixed(0)}%</div>
                                        </div>
                                    )}
                                </div>

                                {(order.recipientName || order.recipientPhone) && (
                                    <div style={{ marginTop: 14, paddingTop: 14, borderTop: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                                        <div>
                                            <div style={{ fontSize: 11, color: 'var(--text-muted)', marginBottom: 4 }}>Nguoi nhan hang</div>
                                            <div style={{ fontWeight: 700, fontSize: 14, color: 'var(--text-primary)' }}>{order.recipientName}</div>
                                            <div style={{ color: 'var(--accent-primary)', fontSize: 13 }}>{order.recipientPhone}</div>
                                            {order.shippingNote && <div style={{ fontSize: 12, color: 'var(--text-muted)', marginTop: 4, fontStyle: 'italic' }}>{order.shippingNote}</div>}
                                        </div>
                                        {order.recipientPhone && (
                                            <a href={`tel:${order.recipientPhone}`}
                                                style={{ padding: '6px 14px', background: '#10b981', color: '#fff', borderRadius: 8, fontSize: 12, fontWeight: 700, textDecoration: 'none', display: 'flex', alignItems: 'center', gap: 4, flexShrink: 0 }}>
                                                Gọi ngay
                                            </a>
                                        )}
                                    </div>
                                )}

                                {order.progressPercent !== undefined && order.progressPercent > 0 && (
                                    <div style={{ marginTop: 14 }}>
                                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12, marginBottom: 4 }}>
                                            <span style={{ color: 'var(--text-secondary)' }}>Tien do san xuat</span>

```
