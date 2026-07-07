# Knowledge Document: FactoryDashboardPage.tsx (Chunk 3/14)

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
  "chunk_index": 2,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
0,246,0.3)'}`,
                            borderRadius: 10, fontSize: 13, color: alert.level === 'warning' ? '#d97706' : '#2563eb'
                        }}>
                            <span style={{ fontSize: 16 }}>{alert.level === 'warning' ? '⚠️' : 'ℹ️'}</span>
                            <span style={{ flex: 1 }}>{alert.message}</span>
                        </div>
                    ))}
                </div>
            )}

            {/* Section A: Don dang chay */}
            <div style={{ marginBottom: 32 }}>
                <h2 style={{ fontSize: 16, fontWeight: 700, marginBottom: 12, color: 'var(--text-primary)' }}>
                    Don dang chay ({dashboard.activeOrdersCount})
                </h2>
                {dashboard.activeOrders?.length === 0 ? (
                    <div style={{ color: 'var(--text-muted)', fontSize: 13, padding: 20, textAlign: 'center', background: 'var(--bg-input)', borderRadius: 12 }}>
                        Chua co don nao dang chay
                    </div>
                ) : (
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: 12 }}>
                        {dashboard.activeOrders?.map((order: any) => (
                            <div key={order.id} style={{
                                padding: 16, background: 'var(--bg-card)', border: '1px solid var(--border)',
                                borderRadius: 14, borderLeft: order.isAtRisk ? '4px solid #ef4444' : '4px solid #10b981'
                            }}>
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 8 }}>
                                    <div>
                                        <div style={{ fontSize: 12, color: 'var(--text-muted)' }}>{order.orderCode}</div>
                                        <div style={{ fontWeight: 700, fontSize: 14, color: 'var(--text-primary)' }}>{order.title}</div>
                                        {order.customerName && <div style={{ fontSize: 12, color: 'var(--text-secondary)', marginTop: 2 }}>{order.customerName}</div>}
                                    </div>

```
