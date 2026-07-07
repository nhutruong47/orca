# Knowledge Document: MarketplacePage.tsx (Chunk 31/70)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/MarketplacePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "notification",
    "factory",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 30,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
x', alignItems: 'center', gap: '24px', padding: '24px', background: 'rgba(255,255,255,0.03)', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.05)'}}>
                                        <div style={{textAlign: 'center'}}>
                                            <div style={{fontSize: '36px', fontWeight: 700, color: '#f59e0b'}}>{avgRating > 0 ? avgRating.toFixed(1) : '—'}</div>
                                            <div style={{color: '#f59e0b', margin: '4px 0', letterSpacing: '2px'}}>{avgRating > 0 ? '★'.repeat(Math.round(avgRating)) + '☆'.repeat(5 - Math.round(avgRating)) : '—'}</div>
                                            <div style={{fontSize: '13px', color: '#a79d94'}}>{reviewCount} đánh giá</div>
                                        </div>
                                        <div style={{flex: 1}}>
                                            {[['Đúng hẹn', onTimeRate, '#10b981'], ['Trễ hẹn', 100 - onTimeRate, '#f59e0b']].map(([label, pct, color]) => (
                                                <div key={label as string} style={{display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '10px'}}>
                                                    <span style={{fontSize: '12px', color: '#a79d94', width: '70px'}}>{label}</span>
                                                    <div style={{flex: 1, height: '8px', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', overflow: 'hidden'}}>
                                                        <div style={{height: '100%', background: color as string, width: `${pct}%`, transition: 'width 0.3s'}}></div>
                                                    </div>
                                                    <span style={{fontSize: '12px', color: '#a79d94', width: '35px', textAlign: 'right'}}>{pct}%</span>
                                                </div>
                                            ))}
                                            <div style={{display: 'flex', gap: 16, marginTop: 8}}>
                                                <span style={{fontSize: 12, color: '#a79d94'}}>✓ {completed} đơn đúng hẹn</span>
                                                <span style={{fontSize: 12, color: '#a79d94'}}>⚠ {late} đơn trễ</span>
                                            </div>
                                        </div>

```
