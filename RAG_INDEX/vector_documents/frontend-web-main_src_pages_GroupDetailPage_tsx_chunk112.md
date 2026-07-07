# Knowledge Document: GroupDetailPage.tsx (Chunk 113/136)

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
  "chunk_index": 112,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
rgin: 0, fontSize: 15, fontWeight: 700, color: '#ffffff', display: 'flex', alignItems: 'center', gap: 8 }}>
                                                <span style={{ width: 8, height: 8, borderRadius: '50%', background: '#f59e0b', display: 'inline-block' }}></span>
                                                Công việc Đang làm & Hạn chót
                                            </h3>

                                            <div style={{ display: 'flex', flexDirection: 'column', gap: 12, minHeight: 140, justifyContent: 'center', alignItems: 'center' }}>
                                                {latestGoalTasks.filter(t => t.status === 'IN_PROGRESS').length === 0 ? (
                                                    <>
                                                        <div style={{ width: 56, height: 56, borderRadius: 12, border: '1.5px solid #3a3a3c', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#8e8e93', marginBottom: 4 }}>
                                                            <ion-icon name="checkmark-outline" style={{ fontSize: 28 }}></ion-icon>
                                                        </div>
                                                        <div style={{ fontSize: 13, color: '#8e8e93', fontWeight: 500, textAlign: 'center', marginBottom: 12 }}>Không có công việc nào đang thực hiện.</div>
                                                        {isAdmin && (
                                                            <button
                                                                onClick={() => {
                                                                    setShowScheduleModal(false);
                                                                    if (!selectedGoalId && goals.length > 0) setSelectedGoalId(goals[0].id);
                                                                    setShowAddTask(true);
                                                                }}
                                                                style={{
                                                                    width: '85%',
                                                                    background: '#cbd5e1',
                                                                    color: '#0f172a',

```
