# Knowledge Document: ProductionPlanPage.tsx (Chunk 19/22)

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
  "chunk_index": 18,
  "total_chunks": 22
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production, chat

## Source Code Chunk
```tsx
t.entries(STAGE_LABELS) as [ProductionStage, string][]).map(([key, label]) => (
                                                <button key={key} onClick={() => setStage(key)}
                                                    style={{
                                                        padding: '8px 16px', borderRadius: 10, border: `2px solid ${stage === key ? '#3b82f6' : 'var(--border)'}`,
                                                        background: stage === key ? 'rgba(59,130,246,0.1)' : 'var(--bg-input)',
                                                        color: stage === key ? '#3b82f6' : 'var(--text-secondary)', fontSize: 13, fontWeight: 600, cursor: 'pointer'
                                                    }}>
                                                    {label}
                                                </button>
                                            ))}
                                        </div>
                                    </div>

                                    <div style={{ marginBottom: 20 }}>
                                        <label style={{ display: 'block', fontSize: 13, fontWeight: 600, color: 'var(--text-secondary)', marginBottom: 8 }}>
                                            Thoi gian nghi giua ca (phut)
                                        </label>
                                        <input type="number" value={breakMinutes} onChange={e => setBreakMinutes(parseInt(e.target.value) || 30)}
                                            min="0" max="120"
                                            style={{ padding: '8px 14px', borderRadius: 10, border: '1px solid var(--border)', background: 'var(--bg-input)', fontSize: 14, width: 120 }} />
                                    </div>

                                    <button onClick={handleCheckIn} disabled={loadingAttendance}
                                        style={{
                                            width: '100%', padding: '14px', borderRadius: 12, border: 'none',
                                            background: 'linear-gradient(135deg, #10b981, #059669)',
                                            color: '#fff', fontSize: 16, fontWeight: 800, cursor: loadingAttendance ? 'not-allowed' : 'pointer',

```
