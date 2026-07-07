# Knowledge Document: GroupDetailPage.tsx (Chunk 44/136)

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
  "chunk_index": 43,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                                              return (
                                                    <div>
                                                        <div style={{ display: 'flex', alignItems: 'center', flexWrap: 'wrap', gap: 6, fontSize: 12 }}>
                                                            <span style={{ color: 'var(--text-secondary)' }}>Số lượng hiện tại:</span>
                                                            <input
                                                                type="number"
                                                                min={0}
                                                                max={target > 0 ? target : undefined}
                                                                value={actual}
                                                                onChange={(e) => {
                                                                    const val = clampActual(Number(e.target.value) || 0);
                                                                    setAllTasks(prev => prev.map(tk => tk.id === t.id ? { ...tk, actualOutput: val } : tk));
                                                                }}
                                                                onBlur={(e) => persistActual(Number(e.target.value) || 0)}
                                                                onKeyDown={(e) => { if (e.key === 'Enter') (e.currentTarget as HTMLInputElement).blur(); }}
                                                                style={{ width: 72, padding: '6px 8px', borderRadius: 7, border: '1px solid #cbd5e1', fontSize: 14, fontWeight: 800, color: '#0f172a', textAlign: 'right', background: '#fff' }}
                                                            />
                                                            <span style={{ color: 'var(--text-secondary)' }}>/</span>
                                                            {isAdmin ? (
                                                                <input
                                                                    type="number"
                                                                    min={0}
                                                                    defaultValue={target || ''}

```
