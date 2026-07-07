# Knowledge Document: WorkforcePage.tsx (Chunk 4/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/WorkforcePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```tsx
}}>
                            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 13, marginBottom: 6 }}>
                                <span style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>{row.label}</span>
                                <span style={{ fontWeight: 800, color: row.color }}>{row.hours.toFixed(1)} gio</span>
                            </div>
                            <div style={{ background: 'var(--bg-input)', borderRadius: 6, height: 8 }}>
                                <div style={{ width: `${Math.min(100, row.hours * 5)}%`, height: '100%', background: row.color, borderRadius: 6 }} />
                            </div>
                        </div>
                    ))}
                </div>

                {/* Don hang dang chay */}
                <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 16, padding: 20 }}>
                    <h2 style={{ fontSize: 14, fontWeight: 700, color: 'var(--text-primary)', marginBottom: 16 }}>Don hang dang chay</h2>
                    {(!wf.activeOrders || wf.activeOrders.length === 0) ? (
                        <div style={{ color: 'var(--text-muted)', fontSize: 13, textAlign: 'center', padding: 20 }}>Khong co don nao</div>
                    ) : (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                            {wf.activeOrders.map((o: any) => (
                                <div key={o.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 0', borderBottom: '1px solid var(--border)' }}>
                                    <div>
                                        <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-primary)' }}>{o.title}</div>
                                        <div style={{ fontSize: 11, color: 'var(--text-muted)' }}>Con lai: {o.remainingQuantity?.toLocaleString('vi-VN')} kg</div>
                                    </div>
                                    <div style={{ fontSize: 18, fontWeight: 900, color: '#10b981' }}>{o.progressPercent?.toFixed(0)}%</div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            </div>

            {/* Nguoi dang lam */}

```
