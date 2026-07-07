# Knowledge Document: GroupDetailPage.tsx (Chunk 95/136)

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
  "chunk_index": 94,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
               <div style={{ display: 'flex', flexDirection: 'column', gap: 14, maxHeight: 280, overflowY: 'auto', paddingRight: 4 }}>
                                            {(() => {
                                                const map: Record<string, { total: number; completed: number; name: string }> = {};
                                                latestGoalTasks.forEach(t => {
                                                    const mId = t.memberId || 'unassigned';
                                                    const mName = t.memberName || 'Chưa giao';
                                                    if (!map[mId]) map[mId] = { total: 0, completed: 0, name: mName };
                                                    map[mId].total += 1;
                                                    if (t.status === 'COMPLETED') map[mId].completed += 1;
                                                });

                                                const items = Object.values(map).sort((a, b) => {
                                                    const pctA = a.total > 0 ? (a.completed / a.total) : 0;
                                                    const pctB = b.total > 0 ? (b.completed / b.total) : 0;
                                                    return pctB - pctA;
                                                });

                                                if (items.length === 0) {
                                                    return <div style={{ fontSize: 13, color: 'var(--text-muted)', textAlign: 'center', padding: '40px 0' }}>Chưa có nhân sự phụ trách.</div>;
                                                }
                                                return items.map((m, i) => {
                                                    const pct = m.total > 0 ? Math.round((m.completed / m.total) * 100) : 0;
                                                    const rankGold = i === 0 && pct > 0;
                                                    return (
                                                        <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 14, background: 'var(--bg-card, #1e293b)', padding: '12px 16px', borderRadius: 14, border: rankGold ? '1px solid #f59e0b' : '1px solid var(--border, #334155)', position: 'relative' }}>

```
