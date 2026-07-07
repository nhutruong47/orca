# Knowledge Document: GroupDetailPage.tsx (Chunk 47/136)

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
  "chunk_index": 46,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
min(actual, target > 0 ? target : actual)}
                                                                onChange={(e) => {
                                                                    const val = clampActual(Number(e.target.value));
                                                                    setAllTasks(prev => prev.map(tk => tk.id === t.id ? { ...tk, actualOutput: val } : tk));
                                                                }}
                                                                onMouseUp={(e) => persistActual(Number((e.currentTarget as HTMLInputElement).value))}
                                                                onTouchEnd={(e) => persistActual(Number((e.currentTarget as HTMLInputElement).value))}
                                                                style={{ position: 'absolute', left: 0, right: 0, top: 0, width: '100%', height: 18, margin: 0, accentColor: PROGRESS_COLOR, cursor: 'pointer', background: 'transparent' }}
                                                            />
                                                        </div>
                                                    </div>
                                                );
                                            })()}
                                        </td>
                                        <td style={{ padding: '12px 16px' }}>
                                            <span style={{ background: t.priority >= 3 ? '#f5e6d3' : t.priority >= 2 ? '#f9f1e3' : '#f0fdf4', color: t.priority >= 3 ? '#a0673c' : t.priority >= 2 ? '#c9884a' : '#16a34a', padding: '3px 8px', borderRadius: 6, fontSize: 11, fontWeight: 700 }}>
                                                {t.priority >= 3 ? 'Cao' : t.priority >= 2 ? 'TB' : 'Thấp'}
                                            </span>
                                        </td>
                                        <td style={{ padding: '12px 16px' }}>
                                            {isAdmin ? (
                                                <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                                                    <select value={t.memberId || ''} onChange={async e => {
                                                        const nextMemberId = e.target.value;

```
