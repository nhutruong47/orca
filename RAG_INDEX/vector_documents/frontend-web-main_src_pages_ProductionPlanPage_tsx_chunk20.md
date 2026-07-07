# Knowledge Document: ProductionPlanPage.tsx (Chunk 21/22)

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
  "chunk_index": 20,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
etween', padding: '10px 0', borderBottom: '1px solid var(--border)' }}>
                                                <span style={{ color: 'var(--text-muted)', fontSize: 13 }}>{label}</span>
                                                <span style={{ fontWeight: 600, fontSize: 13 }}>{value}</span>
                                            </div>
                                        ))}
                                    </div>

                                    {!myAttendance.checkOutTime ? (
                                        <button onClick={handleCheckOut} disabled={loadingAttendance}
                                            style={{
                                                width: '100%', marginTop: 16, padding: '14px', borderRadius: 12, border: 'none',
                                                background: 'linear-gradient(135deg, #ef4444, #dc2626)',
                                                color: '#fff', fontSize: 16, fontWeight: 800, cursor: loadingAttendance ? 'not-allowed' : 'pointer'
                                            }}>
                                            {loadingAttendance ? 'Dang xu ly...' : 'Check-out'}
                                        </button>
                                    ) : (
                                        <div style={{ marginTop: 16, background: 'rgba(16,185,129,0.08)', borderRadius: 12, padding: 16 }}>
                                            <div style={{ fontSize: 14, fontWeight: 700, color: '#10b981', marginBottom: 12 }}>Ca lam viec da hoan thanh</div>
                                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
                                                {[
                                                    ['Gio thuong', `${myAttendance.regularHours}h`],
                                                    ['Gio tang ca', `${myAttendance.overtimeHours}h`],
                                                    ['Tong gio', `${myAttendance.actualWorkHours}h`],
                                                    ['Check-out', new Date(myAttendance.checkOutTime).toLocaleTimeString('vi-VN')],
                                                ].map(([label, value]) => (

```
