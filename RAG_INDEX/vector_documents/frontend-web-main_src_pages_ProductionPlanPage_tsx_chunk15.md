# Knowledge Document: ProductionPlanPage.tsx (Chunk 16/22)

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
  "chunk_index": 15,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
{ position: 'absolute', left: 0, right: 0, top: 7, height: 4, background: 'var(--border)', borderRadius: 2 }} />
                                                        <div style={{ position: 'absolute', left: 0, top: 7, height: 4, width: `${livePct}%`, background: PROGRESS_COLOR, borderRadius: 2, transition: 'width 0.15s ease' }} />
                                                        <input
                                                            type="range"
                                                            min={0}
                                                            max={Math.max(targetQty, 1)}
                                                            value={cappedActual}
                                                            onChange={e => updateField('actual', Math.max(0, Number(e.target.value) || 0))}
                                                            disabled={target.isHoliday}
                                                            style={{ position: 'absolute', left: 0, right: 0, top: 0, width: '100%', height: 18, margin: 0, accentColor: PROGRESS_COLOR, cursor: target.isHoliday ? 'not-allowed' : 'pointer', background: 'transparent' }}
                                                        />
                                                    </div>

                                                    {edit && !target.isHoliday && (
                                                        <div style={{ marginTop: 10, textAlign: 'right' }}>
                                                            <button onClick={() => handleSaveTarget(target)} disabled={savingTargetId === target.id} style={{
                                                                padding: '6px 14px', borderRadius: 8, border: 'none',
                                                                background: PROGRESS_COLOR, color: '#fff', fontSize: 12, fontWeight: 700,
                                                                cursor: savingTargetId === target.id ? 'not-allowed' : 'pointer',
                                                                opacity: savingTargetId === target.id ? 0.6 : 1
                                                            }}>
                                                                {savingTargetId === target.id ? 'Dang luu...' : 'Luu tien do'}

```
