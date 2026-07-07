# Knowledge Document: ProductionOrderPage.tsx (Chunk 8/19)

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
  "chunk_index": 7,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
ex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                                    <div style={{ flex: 1 }}>
                                        <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
                                            <span style={{ fontSize: 13, fontWeight: 700, color: 'var(--accent-primary)' }}>{order.orderCode}</span>
                                            <span style={{ fontSize: 11, fontWeight: 700, padding: '2px 8px', borderRadius: 4, background: `${getStatusColor(order.status)}20`, color: getStatusColor(order.status) }}>
                                                {getStatusLabel(order.status)}
                                            </span>
                                            {order.productType && (
                                                <span style={{ fontSize: 11, color: 'var(--text-muted)', padding: '2px 8px', background: 'var(--bg-input)', borderRadius: 4 }}>
                                                    {order.productType}
                                                </span>
                                            )}
                                        </div>
                                        <div style={{ fontWeight: 700, fontSize: 15, color: 'var(--text-primary)', marginBottom: 4 }}>{order.title}</div>
                                        {order.customerName && <div style={{ fontSize: 13, color: 'var(--text-secondary)' }}>Khach hang: {order.customerName}</div>}
                                    </div>
                                    <div style={{ textAlign: 'right' }}>
                                        <div style={{ fontSize: 20, fontWeight: 800, color: 'var(--text-primary)' }}>
                                            {(order.outputTarget || 0).toLocaleString('vi-VN')} kg
                                        </div>
                                        {order.completedQuantity != null && (
                                            <div style={{ fontSize: 12, color: '#10b981', marginTop: 4 }}>
                                                Da xong: {(order.completedQuantity).toLocaleString('vi-VN')} kg ({order.progressPercent?.toFixed(0)}%)
                                            </div>
                                        )}

```
