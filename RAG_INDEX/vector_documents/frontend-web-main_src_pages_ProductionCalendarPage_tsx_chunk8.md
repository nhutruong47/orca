# Knowledge Document: ProductionCalendarPage.tsx (Chunk 9/12)

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
  "chunk_index": 8,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
alue={pkg.completionRate} max={100} />
                                            )}
                                        </div>
                                    );
                                })}
                            </div>
                        </div>

                        {/* Row 5: Gio cong */}
                        <div style={{ gridColumn: '1 / -1', marginTop: 8 }}>
                            <div style={{ fontSize: 11, color: 'var(--text-muted)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: 1, marginBottom: 6 }}>Gio cong & Nhan su</div>
                            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(14, minmax(120px, 1fr))', gap: 8 }}>
                                {Array.from({ length: 14 }, (_, i) => {
                                    const d = new Date(new Date(weekStart).getTime() + i * 86400000);
                                    const day = calendar[i];
                                    const isSat = d.getDay() === 6 || d.getDay() === 0;
                                    return (
                                        <div key={i} style={{
                                            background: isSat ? 'rgba(0,0,0,0.03)' : 'var(--bg-card)',
                                            border: '1px solid var(--border)',
                                            borderRadius: 8, padding: '8px 10px', minHeight: 60
                                        }}>
                                            <div style={{ fontSize: 14, fontWeight: 800, color: '#8b5cf6' }}>
                                                {(day?.totalWorkerHours || 0).toFixed(1)}
                                            </div>
                                            <div style={{ fontSize: 11, color: 'var(--text-muted)' }}>gio</div>
                                            <div style={{ fontSize: 12, color: '#10b981', fontWeight: 600, marginTop: 4 }}>
                                                {day?.totalWorkers || 0} nguoi
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Don hang table */}

```
