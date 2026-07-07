# Knowledge Document: FactoryDashboardPage.tsx (Chunk 4/14)

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
  "chunk_index": 3,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
olor: 'var(--text-muted)' }}>{order.orderCode}</div>
                                        <div style={{ fontWeight: 700, fontSize: 14, color: 'var(--text-primary)' }}>{order.title}</div>
                                        {order.customerName && <div style={{ fontSize: 12, color: 'var(--text-secondary)', marginTop: 2 }}>{order.customerName}</div>}
                                    </div>
                                    {order.isAtRisk && <span style={{ fontSize: 10, background: '#ef4444', color: '#fff', padding: '2px 6px', borderRadius: 4, fontWeight: 700 }}>Rủi ro</span>}
                                </div>
                                <div style={{ marginBottom: 10 }}>
                                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12, marginBottom: 4 }}>
                                        <span style={{ color: 'var(--text-secondary)' }}>Tien do</span>
                                        <span style={{ fontWeight: 600, color: 'var(--text-primary)' }}>{order.progressPercent?.toFixed(0)}%</span>
                                    </div>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                        <input
                                            type="range"
                                            min={0}
                                            max={100}
                                            value={order.progressPercent || 0}
                                            onChange={(e) => {
                                                const val = Number(e.target.value);
                                                setDashboard((prev: any) => ({
                                                    ...prev,
                                                    activeOrders: prev.activeOrders?.map((o: any) =>
                                                        o.id === order.id ? { ...o, progressPercent: val } : o
                                                    ),
                                                }));
                                            }}
                                            onMouseUp={(e) => updateOrderProgress(order.id, Number((e.target as HTMLInputElement).value))}

```
