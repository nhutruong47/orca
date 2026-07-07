# Knowledge Document: ProductionPlanPage.tsx (Chunk 14/22)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionPlanPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 13,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
fyContent: 'space-between', marginBottom: 10 }}>
                                                    <div>
                                                        <span style={{ fontSize: 14, fontWeight: 700 }}>
                                                            {new Date(target.targetDate!).toLocaleDateString('vi-VN', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}
                                                        </span>
                                                        {isToday && <span style={{ marginLeft: 8, fontSize: 11, fontWeight: 700, background: '#8b5cf6', color: '#fff', padding: '2px 8px', borderRadius: 4 }}>Hom nay</span>}
                                                        {target.isHoliday && <span style={{ marginLeft: 8, fontSize: 11, fontWeight: 600, background: 'var(--bg-input)', color: 'var(--text-muted)', padding: '2px 8px', borderRadius: 4 }}>Ngay nghi</span>}
                                                    </div>
                                                    <span style={{ fontSize: 13, fontWeight: 700, color: PROGRESS_COLOR }}>{livePct}%</span>
                                                </div>

                                                <div style={{ background: 'var(--bg-input)', borderRadius: 8, padding: '10px 12px' }}>
                                                    <div style={{ display: 'flex', alignItems: 'center', flexWrap: 'wrap', gap: 8, fontSize: 13 }}>
                                                        <span style={{ color: 'var(--text-secondary)' }}>So luong hien tai:</span>
                                                        <input
                                                            type="number"
                                                            min={0}
                                                            max={targetQty}
                                                            value={actualQty}
                                                            onChange={e => updateField('actual', Math.max(0, Number(e.target.value) || 0))}
                                                            disabled={target.isHoliday}

```
