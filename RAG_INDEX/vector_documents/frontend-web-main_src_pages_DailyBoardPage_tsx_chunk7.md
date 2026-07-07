# Knowledge Document: DailyBoardPage.tsx (Chunk 8/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DailyBoardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 7,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
0, color: '#10b981' }}>
                                            {row.completedQuantity?.toLocaleString('vi-VN')}
                                        </div>
                                        <div style={{ fontSize: 12, color: 'var(--text-muted)' }}>/ {row.outputTarget?.toLocaleString('vi-VN')} kg</div>
                                    </div>
                                </div>

                                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 8, marginBottom: 10 }}>
                                    {[
                                        { label: 'Rang', actual: row.roastActual, target: row.roastTarget },
                                        { label: 'QC', actual: row.qcActual, target: row.qcTarget },
                                        { label: 'Dong goi', actual: row.packagingActual, target: row.packagingTarget },
                                    ].map(c => (
                                        <div key={c.label} style={{ background: 'var(--bg-input)', borderRadius: 8, padding: '8px 10px' }}>
                                            <div style={{ fontSize: 11, color: 'var(--text-muted)', marginBottom: 2 }}>{c.label}</div>
                                            <div style={{ fontSize: 13, fontWeight: 700, color: '#10b981' }}>
                                                {c.actual?.toLocaleString('vi-VN')}
                                                <span style={{ fontSize: 11, color: 'var(--text-muted)', fontWeight: 400 }}> / {c.target?.toLocaleString('vi-VN')}</span>
                                            </div>
                                        </div>
                                    ))}
                                </div>

                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                    <div style={{ flex: 1, marginRight: 16 }}>
                                        <input
                                            type="range"
                                            min={0}
                                            max={100}
                                            value={row.progressPercent || 0}
                                            onChange={(e) => {

```
