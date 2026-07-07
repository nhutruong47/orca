# Knowledge Document: GroupDetailPage.tsx (Chunk 54/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 53,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
ns: '1fr 30px', gap: 6, alignItems: 'baseline', width: '100%', maxWidth: 120, margin: '0 auto' }}>
                                            <div style={{ textAlign: 'right', fontWeight: 700, fontSize: 15, color: '#3b82f6', letterSpacing: '0.5px' }}>
                                                {Number(item.quantity).toLocaleString('vi-VN')}
                                            </div>
                                            <div style={{ textAlign: 'left', fontSize: 13, fontWeight: 500, color: '#94a3b8' }}>
                                                {item.unit}
                                            </div>
                                        </div>
                                    </td>
                                    <td style={{ padding: '12px 16px' }}>
                                        {isUpdating ? (
                                            <div style={{ display: 'flex', gap: 6 }}>
                                                <input type="text" value={updateInvQty} onChange={e => { const val = e.target.value.replace(/\./g, ''); if (!isNaN(Number(val))) setUpdateInvQty(val === '' ? '' : Number(val).toLocaleString('de-DE')); }} style={{ padding: '4px 8px', borderRadius: 6, border: '1px solid #d4a574', width: 70, fontSize: 12 }} autoFocus />
                                                <button onClick={() => handleUpdateInvQty(item.id)} style={{ background: '#10b981', color: '#fff', border: 'none', borderRadius: 6, padding: '0 8px', fontSize: 11, cursor: 'pointer' }}>OK</button>
                                                <button onClick={() => setUpdatingInvId(null)} style={{ background: '#f1f5f9', color: '#64748b', border: 'none', borderRadius: 6, padding: '0 8px', fontSize: 11, cursor: 'pointer' }}>Hủy</button>
                                            </div>
                                        ) : (
                                            <button onClick={() => { setUpdatingInvId(item.id); setUpdateInvQty(Number(item.quantity).toLocaleString('de-DE')); }} style={{ background: '#f8fafc', color: '#d4a574', border: '1px solid #e2e8f0', borderRadius: 6, padding: '4px 10px', fontSize: 11, fontWeight: 600, cursor: 'pointer' }}>Chỉnh sửa</button>
                                        )}
                                    </td>

```
