# Knowledge Document: ProductionPlanPage.tsx (Chunk 15/22)

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
  "chunk_index": 14,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
          min={0}
                                                            max={targetQty}
                                                            value={actualQty}
                                                            onChange={e => updateField('actual', Math.max(0, Number(e.target.value) || 0))}
                                                            disabled={target.isHoliday}
                                                            style={{ width: 80, padding: '6px 8px', borderRadius: 6, border: '1px solid var(--border)', background: '#fff', fontSize: 13, textAlign: 'right' }}
                                                        />
                                                        <span style={{ color: 'var(--text-secondary)' }}>/</span>
                                                        <input
                                                            type="number"
                                                            min={0}
                                                            value={targetQty}
                                                            onChange={e => updateField('target', Math.max(0, Number(e.target.value) || 0))}
                                                            disabled={target.isHoliday}
                                                            style={{ width: 80, padding: '6px 8px', borderRadius: 6, border: '1px solid var(--border)', background: '#fff', fontSize: 13, textAlign: 'right' }}
                                                        />
                                                        <span style={{ color: 'var(--text-muted)', fontWeight: 600 }}>{unit}</span>
                                                    </div>

                                                    <div style={{ position: 'relative', height: 18, marginTop: 10 }}>
                                                        <div style={{ position: 'absolute', left: 0, right: 0, top: 7, height: 4, background: 'var(--border)', borderRadius: 2 }} />
                                                        <div style={{ position: 'absolute', left: 0, top: 7, height: 4, width: `${livePct}%`, background: PROGRESS_COLOR, borderRadius: 2, transition: 'width 0.15s ease' }} />
                                                        <input

```
