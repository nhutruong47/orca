# Knowledge Document: ProductionCalendarPage.tsx (Chunk 4/12)

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
  "chunk_index": 3,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
     <div key={i} style={{
                                    background: isToday(d) ? 'rgba(139,92,246,0.1)' : isWeekend(d) ? 'rgba(0,0,0,0.03)' : 'var(--bg-card)',
                                    border: `1px solid ${isToday(d) ? '#8b5cf6' : 'var(--border)'}`,
                                    borderRadius: 10, padding: '12px 10px', textAlign: 'center'
                                }}>
                                    <div style={{ fontSize: 11, color: 'var(--text-muted)', fontWeight: 600 }}>{dayName(d)}</div>
                                    <div style={{ fontSize: 16, fontWeight: 800, color: isToday(d) ? '#8b5cf6' : 'var(--text-primary)' }}>
                                        {d.getDate()}
                                    </div>
                                    {day && (
                                        <div style={{ fontSize: 11, fontWeight: 700, color: '#10b981', marginTop: 4 }}>
                                            {(day.totalActualKg || 0).toLocaleString('vi-VN')} kg
                                        </div>
                                    )}
                                </div>
                            );
                        })}

                        {/* Row 1: Tong target */}
                        <div style={{ gridColumn: '1 / -1', marginTop: 8 }}>
                            <div style={{ fontSize: 11, color: 'var(--text-muted)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: 1, marginBottom: 6 }}>Tong san luong (kg)</div>
                            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(14, minmax(120px, 1fr))', gap: 8 }}>
                                {Array.from({ length: 14 }, (_, i) => {
                                    const d = new Date(new Date(weekStart).getTime() + i * 86400000);
                                    const day = calendar[i];
                                    const target = day?.totalTargetKg || 0;
                                    const actual = day?.totalActualKg || 0;
                                    const isSat = d.getDay() === 6 || d.getDay() === 0;
                                    return (
                                        <div key={i} style={{
                                            background: isSat ? 'rgba(0,0,0,0.03)' : 'var(--bg-input)',

```
