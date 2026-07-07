# Knowledge Document: GroupDetailPage.tsx (Chunk 130/136)

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
  "chunk_index": 129,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
.completedTasks / s.totalTasks) * 100) : 0;
                                    const isEditing = editingRate === s.memberId;

                                    return (
                                        <div key={s.memberId} style={{
                                            display: 'grid',
                                            gridTemplateColumns: '2fr 1fr 1fr 1fr 1.2fr 1.3fr',
                                            gap: 12, padding: '14px 16px',
                                            borderBottom: '1px solid var(--border)',
                                            alignItems: 'center',
                                            background: idx % 2 === 0 ? 'transparent' : 'var(--bg-input, rgba(255,255,255,0.02))'
                                        }}>
                                            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                                                <div style={{
                                                    width: 40, height: 40, borderRadius: 12,
                                                    background: ['#d4a574', '#8b5cf6', '#ec4899', '#f43f5e', '#f59e0b', '#10b981'][idx % 6],
                                                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                                                    color: '#fff', fontWeight: 700, fontSize: 14
                                                }}>
                                                    {(s.memberName || '?').split(' ').slice(-2).map(w => w[0]).join('').toUpperCase()}
                                                </div>
                                                <div>
                                                    <div style={{ fontSize: 14, fontWeight: 700, color: 'var(--text-primary)' }}>{s.memberName}</div>
                                                    <div style={{ fontSize: 11, color: '#94a3b8' }}>ID: {s.memberId?.slice(0, 8)}...</div>
                                                </div>
                                            </div>

                                            <div style={{ textAlign: 'center' }}>
                                                <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--text-primary)' }}>{s.totalTasks}</div>
                                            </div>


```
