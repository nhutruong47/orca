# Knowledge Document: GroupDetailPage.tsx (Chunk 48/136)

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
  "chunk_index": 47,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
e={{ padding: '12px 16px' }}>
                                            {isAdmin ? (
                                                <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                                                    <select value={t.memberId || ''} onChange={async e => {
                                                        const nextMemberId = e.target.value;
                                                        if (!nextMemberId) return;
                                                        let updatedTask;
                                                        if (t.memberId && t.memberId !== nextMemberId) {
                                                            const reason = window.prompt('Lý do chuyển giao công việc?', 'Điều phối lại nhân sự') || 'Điều phối lại nhân sự';
                                                            updatedTask = await taskService.transfer(t.id, nextMemberId, reason);
                                                        } else {
                                                            updatedTask = await taskService.assign(t.id, nextMemberId);
                                                        }
                                                        if (updatedTask && updatedTask.id) {
                                                            setAllTasks(prev => prev.map(tk => tk.id === updatedTask.id ? updatedTask : tk));
                                                        }
                                                        if (id) { const g = await goalService.getByTeam(id); setGoals(g); }
                                                    }} style={{ background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: 8, padding: '4px 8px', fontSize: 12, cursor: 'pointer', minWidth: 100 }}>
                                                        <option value="">— Giao —</option>
                                                        {team?.members?.map(m => <option key={m.userId} value={m.userId}>{m.fullName || m.username}</option>)}
                                                    </select>
                                                    <select value={t.backupMemberId || ''} onChange={async e => {
                                                        const updatedTask = await taskService.setBackup(t.id, e.target.value);

```
