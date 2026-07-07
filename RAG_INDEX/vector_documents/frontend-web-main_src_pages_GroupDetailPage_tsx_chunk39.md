# Knowledge Document: GroupDetailPage.tsx (Chunk 40/136)

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
  "chunk_index": 39,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
rm: 'uppercase', letterSpacing: '0.05em', borderBottom: '1px solid var(--border)' }}>{h}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {(() => {
                            const filtered = (taskFilter === 'my' || !isAdmin) ? latestGoalTasks.filter(t => t.memberId === user?.id) : latestGoalTasks;
                            if (filtered.length === 0) {
                                return <tr><td colSpan={5} style={{ textAlign: 'center', padding: 40, color: 'var(--text-muted)', fontSize: 13 }}>Chưa có công việc nào trong danh sách này</td></tr>;
                            }
                            return filtered.map(t => {
                                return (
                                    <tr key={t.id} style={{ borderBottom: '1px solid var(--border)' }}>
                                        <td style={{ padding: '12px 16px' }}>
                                            {editingTaskId === t.id ? (
                                                <div style={{ display: 'grid', gap: 6, minWidth: 220 }}>
                                                    <input value={editTaskTitle} onChange={e => setEditTaskTitle(e.target.value)} placeholder="Tên công việc" style={{ padding: '7px 10px', borderRadius: 8, border: '1px solid var(--accent-primary)', fontSize: 13, fontWeight: 700, color: 'var(--text-primary)', background: 'var(--bg-input)' }} />
                                                    <input value={editTaskDesc} onChange={e => setEditTaskDesc(e.target.value)} placeholder="Mô tả" style={{ padding: '7px 10px', borderRadius: 8, border: '1px solid var(--border)', fontSize: 12, color: 'var(--text-secondary)', background: 'var(--bg-input)' }} />
                                                    <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                                                        <select value={editTaskStage} onChange={e => setEditTaskStage(e.target.value)} style={{ padding: '6px 8px', borderRadius: 8, border: '1px solid var(--border)', fontSize: 12, background: 'var(--bg-input)', color: 'var(--text-secondary)' }}>

```
