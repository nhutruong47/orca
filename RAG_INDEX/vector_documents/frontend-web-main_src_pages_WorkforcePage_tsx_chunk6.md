# Knowledge Document: WorkforcePage.tsx (Chunk 7/8)

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
  "chunk_index": 6,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```tsx

                                <span style={{ fontSize: 11, background: '#fee2e2', color: '#dc2626', padding: '3px 10px', borderRadius: 20, fontWeight: 700 }}>TRE</span>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Da check-out */}
            {wf.checkedOut?.length > 0 && (
                <div>
                    <h2 style={{ fontSize: 15, fontWeight: 700, color: 'var(--text-primary)', marginBottom: 12 }}>Da check-out ({wf.checkedOut.length})</h2>
                    <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14, overflow: 'hidden' }}>
                        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
                            <thead>
                                <tr style={{ borderBottom: '1px solid var(--border)', background: 'var(--bg-input)' }}>
                                    {['Nhan vien', 'Cong doan', 'Ca', 'Gio thuong', 'Gio tang ca', 'Tong gio'].map(h => (
                                        <th key={h} style={{ textAlign: 'left', padding: '10px 16px', color: 'var(--text-muted)', fontWeight: 600, fontSize: 12 }}>{h}</th>
                                    ))}
                                </tr>
                            </thead>
                            <tbody>
                                {wf.checkedOut.map((w: any, i: number) => (
                                    <tr key={w.userId} style={{ borderBottom: i < wf.checkedOut.length - 1 ? '1px solid var(--border)' : 'none' }}>
                                        <td style={{ padding: '10px 16px', display: 'flex', alignItems: 'center', gap: 10 }}>
                                            <Avatar name={w.userName} size={28} />
                                            <span style={{ fontWeight: 600 }}>{w.userName}</span>
                                        </td>
                                        <td style={{ padding: '10px 16px', color: STAGE_COLOR[w.stage] || 'var(--text-secondary)', fontWeight: 600, textTransform: 'capitalize' }}>
                                            {w.stage?.replace('_', ' ').toLowerCase()}
                                        </td>

```
