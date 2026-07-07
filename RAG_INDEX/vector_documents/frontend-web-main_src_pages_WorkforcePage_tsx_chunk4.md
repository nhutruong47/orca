# Knowledge Document: WorkforcePage.tsx (Chunk 5/8)

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
  "chunk_index": 4,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```tsx
N')} kg</div>
                                    </div>
                                    <div style={{ fontSize: 18, fontWeight: 900, color: '#10b981' }}>{o.progressPercent?.toFixed(0)}%</div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            </div>

            {/* Nguoi dang lam */}
            {wf.checkedIn?.length > 0 && (
                <div style={{ marginBottom: 20 }}>
                    <h2 style={{ fontSize: 15, fontWeight: 700, color: 'var(--text-primary)', marginBottom: 12 }}>
                        Dang lam viec ({wf.checkedIn.length})
                    </h2>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(240px, 1fr))', gap: 12 }}>
                        {wf.checkedIn.map((w: any) => (
                            <div key={w.userId} style={{
                                background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14,
                                padding: 16, borderTop: `3px solid ${STAGE_COLOR[w.stage] || '#8b5cf6'}`
                            }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                                    <Avatar name={w.userName} />
                                    <div style={{ flex: 1, minWidth: 0 }}>
                                        <div style={{ fontSize: 14, fontWeight: 700, color: 'var(--text-primary)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{w.userName}</div>
                                        <div style={{ fontSize: 12, color: 'var(--text-secondary)', textTransform: 'capitalize' }}>{w.shiftType?.toLowerCase()}</div>
                                    </div>
                                    <StatusBadge status={w.attendanceStatus} />
                                </div>
                                <div style={{ marginTop: 10, fontSize: 12, color: 'var(--text-muted)', display: 'flex', justifyContent: 'space-between' }}>
                                    <span style={{ textTransform: 'capitalize', color: STAGE_COLOR[w.stage] || 'var(--text-secondary)', fontWeight: 600 }}>{w.stage?.replace('_', ' ').toLowerCase()}</span>

```
