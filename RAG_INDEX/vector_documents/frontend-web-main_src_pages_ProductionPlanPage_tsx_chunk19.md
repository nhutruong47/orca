# Knowledge Document: ProductionPlanPage.tsx (Chunk 20/22)

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
  "chunk_index": 19,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
                                   style={{
                                            width: '100%', padding: '14px', borderRadius: 12, border: 'none',
                                            background: 'linear-gradient(135deg, #10b981, #059669)',
                                            color: '#fff', fontSize: 16, fontWeight: 800, cursor: loadingAttendance ? 'not-allowed' : 'pointer',
                                            display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8
                                        }}>
                                        {loadingAttendance ? 'Dang xu ly...' : 'Check-in'}
                                    </button>
                                </div>
                            ) : (
                                <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14, padding: 24 }}>
                                    <h3 style={{ fontSize: 16, fontWeight: 700, marginBottom: 16 }}>Trang thai hom nay</h3>
                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                        {[
                                            ['Ca lam', SHIFT_LABELS[myAttendance.shiftType] || myAttendance.shiftType],
                                            ['Cong doan', STAGE_LABELS[myAttendance.productionStage] || myAttendance.productionStage],
                                            ['Check-in', myAttendance.checkInTime ? new Date(myAttendance.checkInTime).toLocaleTimeString('vi-VN') : '-'],
                                            ['Don hang', myAttendance.orderTitle || 'Khong lien ket'],
                                            ['Gio nghi', `${myAttendance.breakMinutes} phut`],
                                        ].map(([label, value]) => (
                                            <div key={label as string} style={{ display: 'flex', justifyContent: 'space-between', padding: '10px 0', borderBottom: '1px solid var(--border)' }}>
                                                <span style={{ color: 'var(--text-muted)', fontSize: 13 }}>{label}</span>
                                                <span style={{ fontWeight: 600, fontSize: 13 }}>{value}</span>
                                            </div>
                                        ))}

```
