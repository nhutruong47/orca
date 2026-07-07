# Knowledge Document: ProductionOrderPage.tsx (Chunk 12/19)

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
  "chunk_index": 11,
  "total_chunks": 19
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
      {order.progressPercent !== undefined && order.progressPercent > 0 && (
                                    <div style={{ marginTop: 14 }}>
                                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12, marginBottom: 4 }}>
                                            <span style={{ color: 'var(--text-secondary)' }}>Tien do san xuat</span>
                                            <span style={{ fontWeight: 700, color: getStatusColor(order.status) }}>{order.progressPercent.toFixed(0)}%</span>
                                        </div>
                                        <div style={{ background: 'var(--bg-input)', borderRadius: 6, height: 8, overflow: 'hidden' }}>
                                            <div style={{ width: `${order.progressPercent}%`, height: '100%', background: getStatusColor(order.status), borderRadius: 6, transition: 'width 0.3s' }} />
                                        </div>
                                    </div>
                                )}
                            </div>
                        ))}
                    </div>
                )
            )}

            {/* Create Form */}
            {activeTab === 'create' && (
                <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 16, padding: 28 }}>
                    <h2 style={{ fontSize: 18, fontWeight: 700, marginBottom: 24, color: 'var(--text-primary)' }}>
                        {editingOrderId ? 'Sua don hang san xuat' : 'Tao don hang san xuat moi'}
                    </h2>
                    <form onSubmit={handleSubmit}>
                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20 }}>
                            {/* Thong tin co ban */}
                            <div style={{ gridColumn: '1 / -1' }}>
                                <h3 style={{ fontSize: 13, fontWeight: 700, color: 'var(--text-muted)', marginBottom: 12, textTransform: 'uppercase', letterSpacing: 1 }}>Thong tin don hang</h3>
                            </div>

                            
                            <Field label="Tieu de don hang" required>
                                <input value={form.title} onChange={e => handleChange('title', e.target.value)} required

```
