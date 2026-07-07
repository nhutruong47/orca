# Knowledge Document: GroupDetailPage.tsx (Chunk 46/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 45,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                  onKeyDown={(e) => { if (e.key === 'Enter') e.currentTarget.blur(); }}
                                                                    style={{ width: 72, padding: '6px 8px', borderRadius: 7, border: '1px solid #cbd5e1', fontSize: 14, fontWeight: 800, color: '#0f172a', textAlign: 'right', background: '#fff' }}
                                                                />
                                                            ) : (
                                                                <span style={{ fontSize: 12, fontWeight: 700, color: '#1e293b' }}>{target}</span>
                                                            )}
                                                            <span style={{ color: 'var(--text-muted)', fontWeight: 600 }}>{unit}</span>
                                                            <span style={{ marginLeft: 'auto', fontSize: 12, fontWeight: 700, color: PROGRESS_COLOR }}>{pct}%</span>
                                                        </div>
                                                        <div style={{ position: 'relative', marginTop: 8, height: 18 }}>
                                                            <div style={{ position: 'absolute', left: 0, right: 0, top: 7, height: 4, background: 'var(--border)', borderRadius: 2 }} />
                                                            <div style={{ position: 'absolute', left: 0, top: 7, height: 4, width: `${pct}%`, background: PROGRESS_COLOR, borderRadius: 2, transition: 'width 0.15s ease' }} />
                                                            <input
                                                                type="range"
                                                                min={0}
                                                                max={Math.max(target, 1)}
                                                                value={Math.min(actual, target > 0 ? target : actual)}
                                                                onChange={(e) => {
                                                                    const val = clampActual(Number(e.target.value));
                                                                    setAllTasks(prev => prev.map(tk => tk.id === t.id ? { ...tk, actualOutput: val } : tk));

```
