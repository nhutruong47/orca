# Knowledge Document: ProductionCalendarPage.tsx (Chunk 3/12)

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
  "chunk_index": 2,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
ttom: 4 }}>Lich San Xuat</h1>
                        <p style={{ color: 'var(--text-secondary)', fontSize: 13 }}>{formatWeekRange()}</p>
                    </div>
                </div>
                <div style={{ display: 'flex', gap: 8 }}>
                    <button onClick={prevWeek} style={{
                        padding: '8px 16px', borderRadius: 10, border: '1px solid var(--border)',
                        background: 'var(--bg-input)', color: 'var(--text-primary)', fontSize: 13, cursor: 'pointer'
                    }}>← Truoc</button>
                    <button onClick={thisWeek} style={{
                        padding: '8px 16px', borderRadius: 10, border: '1px solid var(--border)',
                        background: 'var(--bg-card)', color: 'var(--text-primary)', fontSize: 13, cursor: 'pointer', fontWeight: 600
                    }}>Tuan nay</button>
                    <button onClick={nextWeek} style={{
                        padding: '8px 16px', borderRadius: 10, border: '1px solid var(--border)',
                        background: 'var(--bg-input)', color: 'var(--text-primary)', fontSize: 13, cursor: 'pointer'
                    }}>Sau →</button>
                </div>
            </div>

            {loading ? (
                <div style={{ textAlign: 'center', padding: 40, color: 'var(--text-muted)' }}>Dang tai...</div>
            ) : (
                <div style={{ overflowX: 'auto' }}>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(14, minmax(120px, 1fr))', gap: 8, minWidth: 800 }}>
                        {/* Header row */}
                        {Array.from({ length: 14 }, (_, i) => {
                            const d = new Date(new Date(weekStart).getTime() + i * 86400000);
                            const day = calendar[i];
                            return (
                                <div key={i} style={{
                                    background: isToday(d) ? 'rgba(139,92,246,0.1)' : isWeekend(d) ? 'rgba(0,0,0,0.03)' : 'var(--bg-card)',
                                    border: `1px solid ${isToday(d) ? '#8b5cf6' : 'var(--border)'}`,
                                    borderRadius: 10, padding: '12px 10px', textAlign: 'center'
                                }}>

```
