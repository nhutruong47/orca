# Knowledge Document: ProductionPlanPage.tsx (Chunk 5/22)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionPlanPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 4,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
                background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                    width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                    color: 'var(--text-secondary)', fontSize: 18,
                }}>
                    <ion-icon name="chevron-back-outline" />
                </button>
                <h1 style={{ fontSize: 22, fontWeight: 800, color: 'var(--text-primary)', margin: 0 }}>Ke hoach San xuat</h1>
            </div>

            {/* Order Selector */}
            <div style={{ marginBottom: 24 }}>
                <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--text-secondary)', marginBottom: 8 }}>
                    Chon don hang
                </label>
                <select
                    value={selectedOrder?.id || ''}
                    onChange={e => {
                        const order = orders.find(o => o.id === e.target.value);
                        if (order) handleSelectOrder(order);
                    }}
                    style={{ width: '100%', maxWidth: 500, padding: '10px 14px', borderRadius: 10, border: '1px solid var(--border)', background: 'var(--bg-input)', color: 'var(--text-primary)', fontSize: 14 }}
                >
                    <option value="">-- Chon don hang --</option>
                    {orders.map(o => (
                        <option key={o.id} value={o.id}>
                            {o.orderCode} - {o.title} ({((o.outputTarget || 0)).toLocaleString()} kg) [{STATUS_LABELS[o.status] || o.status}]
                        </option>
                    ))}
                </select>
            </div>

            {selectedOrder && (
                <>
                    {/* Order Info */}
                    <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14, padding: 20, marginBottom: 24 }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                            <div>
                                <div style={{ fontSize: 12, color: 'var(--text-muted)', marginBottom: 4 }}>{selectedOrder.orderCode} · {selectedOrder.productType}</div>

```
