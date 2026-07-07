# Knowledge Document: ProductionCalendarPage.tsx (Chunk 5/12)

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
  "chunk_index": 4,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
day?.totalTargetKg || 0;
                                    const actual = day?.totalActualKg || 0;
                                    const isSat = d.getDay() === 6 || d.getDay() === 0;
                                    return (
                                        <div key={i} style={{
                                            background: isSat ? 'rgba(0,0,0,0.03)' : 'var(--bg-input)',
                                            borderRadius: 8, padding: '8px 10px', minHeight: 60
                                        }}>
                                            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 11, color: 'var(--text-muted)', marginBottom: 4 }}>
                                                <span>Muc tieu</span>
                                            </div>
                                            <div style={{ fontSize: 14, fontWeight: 700, color: 'var(--text-primary)' }}>
                                                {target.toLocaleString('vi-VN')}
                                            </div>
                                            <div style={{ fontSize: 12, color: '#10b981', fontWeight: 600 }}>
                                                Thuc te: {actual.toLocaleString('vi-VN')}
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        </div>

                        {/* Row 2: Cong doan Rang */}
                        <div style={{ gridColumn: '1 / -1', marginTop: 8 }}>
                            <div style={{ fontSize: 11, color: '#d97706', fontWeight: 700, textTransform: 'uppercase', letterSpacing: 1, marginBottom: 6 }}>Cong doan Rang</div>
                            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(14, minmax(120px, 1fr))', gap: 8 }}>
                                {Array.from({ length: 14 }, (_, i) => {
                                    const d = new Date(new Date(weekStart).getTime() + i * 86400000);
                                    const day = calendar[i];
                                    const roast = day?.roast || {};
                                    const isSat = d.getDay() === 6 || d.getDay() === 0;
                                    return (

```
