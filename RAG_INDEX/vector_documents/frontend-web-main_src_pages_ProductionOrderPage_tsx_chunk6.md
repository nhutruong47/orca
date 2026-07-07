# Knowledge Document: ProductionOrderPage.tsx (Chunk 7/19)

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
  "chunk_index": 6,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
 activeTab === tab ? '0 1px 3px rgba(0,0,0,0.1)' : 'none'
                    }}>{tab === 'create' && editingOrderId ? 'Sua don hang' : label}</button>
                ))}
            </div>

            {/* List */}
            {activeTab === 'list' && (
                loading ? (
                    <div style={{ textAlign: 'center', padding: 40, color: 'var(--text-muted)' }}>Dang tai...</div>
                ) : orders.length === 0 ? (
                    <div style={{ textAlign: 'center', padding: 60, background: 'var(--bg-card)', borderRadius: 14, border: '1px solid var(--border)' }}>
                        <div style={{ fontSize: 40, marginBottom: 12 }}>📦</div>
                        <div style={{ fontWeight: 700, marginBottom: 8, color: 'var(--text-primary)' }}>Chua co don hang nao</div>
                        <div style={{ fontSize: 13, color: 'var(--text-muted)', marginBottom: 20 }}>Tao don hang dau tien de bat dau san xuat</div>
                        <button onClick={startCreate} style={{
                            background: 'linear-gradient(135deg, #10b981, #059669)', color: '#fff', border: 'none',
                            borderRadius: 10, padding: '10px 24px', fontSize: 14, fontWeight: 700, cursor: 'pointer'
                        }}>Tao don hang</button>
                    </div>
                ) : (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                        {orders.map(order => (
                            <div key={order.id} style={{
                                background: 'var(--bg-card)', border: '1px solid var(--border)',
                                borderRadius: 14, padding: 20, borderLeft: `5px solid ${getStatusColor(order.status)}`
                            }}>
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                                    <div style={{ flex: 1 }}>
                                        <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
                                            <span style={{ fontSize: 13, fontWeight: 700, color: 'var(--accent-primary)' }}>{order.orderCode}</span>

```
