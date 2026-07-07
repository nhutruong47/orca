# Knowledge Document: WorkforcePage.tsx (Chunk 6/8)

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
  "chunk_index": 5,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```tsx
                                </div>
                                <div style={{ marginTop: 10, fontSize: 12, color: 'var(--text-muted)', display: 'flex', justifyContent: 'space-between' }}>
                                    <span style={{ textTransform: 'capitalize', color: STAGE_COLOR[w.stage] || 'var(--text-secondary)', fontWeight: 600 }}>{w.stage?.replace('_', ' ').toLowerCase()}</span>
                                    {w.checkInTime && <span>{new Date(w.checkInTime).toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' })}</span>}
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Nguoi di tre */}
            {wf.lateWorkers?.length > 0 && (
                <div style={{ marginBottom: 20 }}>
                    <h2 style={{ fontSize: 15, fontWeight: 700, color: '#ef4444', marginBottom: 12 }}>Nguoi di tre ({wf.lateWorkers.length})</h2>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                        {wf.lateWorkers.map((w: any) => (
                            <div key={w.userId} style={{
                                background: 'rgba(239,68,68,0.06)', border: '1px solid rgba(239,68,68,0.15)',
                                borderRadius: 12, padding: '12px 16px', display: 'flex', alignItems: 'center', gap: 12
                            }}>
                                <Avatar name={w.userName} size={32} />
                                <div style={{ flex: 1 }}>
                                    <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--text-primary)' }}>{w.userName}</div>
                                    {w.checkInTime && <div style={{ fontSize: 12, color: '#ef4444' }}>Check-in luc: {new Date(w.checkInTime).toLocaleTimeString('vi-VN')}</div>}
                                </div>
                                <span style={{ fontSize: 11, background: '#fee2e2', color: '#dc2626', padding: '3px 10px', borderRadius: 20, fontWeight: 700 }}>TRE</span>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Da check-out */}
            {wf.checkedOut?.length > 0 && (
                <div>

```
