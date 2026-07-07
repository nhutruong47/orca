# Knowledge Document: ProductionCalendarPage.tsx (Chunk 6/12)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionCalendarPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 5,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
ay.from({ length: 14 }, (_, i) => {
                                    const d = new Date(new Date(weekStart).getTime() + i * 86400000);
                                    const day = calendar[i];
                                    const roast = day?.roast || {};
                                    const isSat = d.getDay() === 6 || d.getDay() === 0;
                                    return (
                                        <div key={i} style={{
                                            background: isSat ? 'rgba(0,0,0,0.03)' : 'rgba(217,119,6,0.05)',
                                            border: '1px solid rgba(217,119,6,0.15)',
                                            borderRadius: 8, padding: '8px 10px', minHeight: 60
                                        }}>
                                            <div style={{ fontSize: 14, fontWeight: 800, color: '#d97706' }}>
                                                {(roast.actualKg || 0).toLocaleString('vi-VN')}
                                            </div>
                                            <div style={{ fontSize: 11, color: 'var(--text-muted)' }}>
                                                / {(roast.targetKg || 0).toLocaleString('vi-VN')} kg
                                            </div>
                                            {roast.completionRate > 0 && (
                                                <ProgressBar value={roast.completionRate} max={100} />
                                            )}
                                        </div>
                                    );
                                })}
                            </div>
                        </div>

                        {/* Row 3: Cong doan QC */}
                        <div style={{ gridColumn: '1 / -1', marginTop: 8 }}>
                            <div style={{ fontSize: 11, color: '#3b82f6', fontWeight: 700, textTransform: 'uppercase', letterSpacing: 1, marginBottom: 6 }}>Cong doan QC</div>
                            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(14, minmax(120px, 1fr))', gap: 8 }}>
                                {Array.from({ length: 14 }, (_, i) => {
                                    const d = new Date(new Date(weekStart).getTime() + i * 86400000);
                                    const day = calendar[i];

```
