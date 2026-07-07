# Knowledge Document: FactoryDashboardPage.tsx (Chunk 6/14)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/FactoryDashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "dashboard",
    "production",
    "factory",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 5,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
een', fontSize: 12, marginTop: 4 }}>
                                        <span style={{ color: 'var(--text-muted)' }}>Han noi bo</span>
                                        <span style={{ fontWeight: 600, color: 'var(--text-primary)' }}>
                                            {new Date(order.internalDeadline).toLocaleDateString('vi-VN')}
                                        </span>
                                    </div>
                                )}
                                {order.customerDeliveryDate && (
                                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12, marginTop: 4 }}>
                                        <span style={{ color: 'var(--text-muted)' }}>Giao hang</span>
                                        <span style={{ fontWeight: 600, color: 'var(--text-primary)' }}>
                                            {new Date(order.customerDeliveryDate).toLocaleDateString('vi-VN')}
                                        </span>
                                    </div>
                                )}
                                {(order.recipientName || order.recipientPhone) && (
                                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12, marginTop: 8, paddingTop: 8, borderTop: '1px solid var(--border)' }}>
                                        <div>
                                            <div style={{ color: 'var(--text-muted)' }}>Nguoi nhan</div>
                                            {order.recipientName && <div style={{ fontWeight: 600, color: 'var(--text-primary)' }}>{order.recipientName}</div>}
                                            {order.recipientPhone && <div style={{ color: 'var(--accent-primary)', fontSize: 11 }}>{order.recipientPhone}</div>}
                                        </div>
                                        {order.recipientPhone && (
                                            <a href={`tel:${order.recipientPhone}`} style={{ display: 'flex', alignItems: 'center', gap: 4, fontSize: 11, color: '#10b981', fontWeight: 600, textDecoration: 'none' }}>
                                                Gọi ngay
                                            </a>
                                        )}
                                    </div>

```
