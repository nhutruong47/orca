# Knowledge Document: GroupDetailPage.tsx (Chunk 49/136)

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
  "chunk_index": 48,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
.members?.map(m => <option key={m.userId} value={m.userId}>{m.fullName || m.username}</option>)}
                                                    </select>
                                                    <select value={t.backupMemberId || ''} onChange={async e => {
                                                        const updatedTask = await taskService.setBackup(t.id, e.target.value);
                                                        if (updatedTask && updatedTask.id) {
                                                            setAllTasks(prev => prev.map(tk => tk.id === updatedTask.id ? updatedTask : tk));
                                                        }
                                                        if (id) { const g = await goalService.getByTeam(id); setGoals(g); }
                                                    }} style={{ background: '#fff7ed', border: '1px solid #fde3c7', borderRadius: 8, padding: '4px 8px', fontSize: 12, cursor: 'pointer', minWidth: 120 }}>
                                                        <option value="">— Sao lưu —</option>
                                                        {team?.members?.map(m => <option key={m.userId} value={m.userId}>{m.fullName || m.username}</option>)}
                                                    </select>
                                                </div>
                                            ) : (
                                                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                                    {t.memberName && <div style={{ width: 24, height: 24, borderRadius: '50%', background: avatarColor(t.memberName), display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 10, fontWeight: 700, color: '#fff' }}>{getInitials(t.memberName)}</div>}
                                                    <span style={{ fontSize: 12, color: '#475569' }}>{t.memberName || 'Chưa giao'}</span>
                                                    {t.backupMemberName && <span style={{ marginLeft: 8, fontSize: 11, color: '#9a8a6f' }}>Sao lưu: {t.backupMemberName}</span>}
                                                    {t.memberId && t.memberId !== user?.id && (
                                                        <ion-icon

```
