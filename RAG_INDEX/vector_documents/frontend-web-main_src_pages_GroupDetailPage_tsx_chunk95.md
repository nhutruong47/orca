# Knowledge Document: GroupDetailPage.tsx (Chunk 96/136)

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
  "chunk_index": 95,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
 rankGold = i === 0 && pct > 0;
                                                    return (
                                                        <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 14, background: 'var(--bg-card, #1e293b)', padding: '12px 16px', borderRadius: 14, border: rankGold ? '1px solid #f59e0b' : '1px solid var(--border, #334155)', position: 'relative' }}>
                                                            {rankGold && (
                                                                <span style={{ position: 'absolute', top: -8, right: 12, background: 'linear-gradient(135deg, #f59e0b, #d4a574)', color: '#fff', fontSize: 9, fontWeight: 800, padding: '2px 8px', borderRadius: 10, textTransform: 'uppercase' }}>Top 1</span>
                                                            )}
                                                            <div style={{ width: 36, height: 36, borderRadius: '50%', background: avatarColor(m.name), color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 13, fontWeight: 700, flexShrink: 0 }}>
                                                                {getInitials(m.name)}
                                                            </div>
                                                            <div style={{ flex: 1, minWidth: 0 }}>
                                                                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 13, fontWeight: 700, color: 'var(--text-primary)', marginBottom: 6 }}>
                                                                    <span style={{ textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>{m.name}</span>
                                                                    <span style={{ color: pct === 100 ? '#10b981' : '#d4a574' }}>{m.completed}/{m.total} task ({pct}%)</span>
                                                                </div>
                                                                <div style={{ height: 6, background: 'var(--bg-input, #0f172a)', borderRadius: 3, overflow: 'hidden' }}>

```
