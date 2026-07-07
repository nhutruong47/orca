# Knowledge Document: GroupDetailPage.tsx (Chunk 33/136)

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
  "chunk_index": 32,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
n-icon>
                            CÔNG VIỆC
                        </h3>
                        {isAdmin && (
                            <div style={{ display: 'flex', gap: 8 }}>
                                {latestGoal && latestGoal.chatLog && (
                                    <button onClick={() => {
                                        setActiveGoalTitle(latestGoal.title || '');
                                        try {
                                            setActiveChatLog(JSON.parse(latestGoal.chatLog || '[]'));
                                            setShowChatHistory(true);
                                        } catch(e) {}
                                    }} style={{ background: '#f8fafc', color: '#64748b', border: '1px solid #e2e8f0', borderRadius: 8, padding: '6px 14px', fontSize: 12, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 4 }}>
                                        <ion-icon name="time-outline"></ion-icon> Lịch sử xác nhận
                                    </button>
                                )}
                                <button onClick={() => { if (!selectedGoalId && goals.length > 0) setSelectedGoalId(goals[0].id); setShowAddTask(!showAddTask); }} style={{ background: '#d4a574', color: '#fff', border: 'none', borderRadius: 8, padding: '6px 14px', fontSize: 12, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 4 }}>
                                    <ion-icon name="add"></ion-icon> Thêm mới
                                </button>
                            </div>
                        )}
                    </div>

                    <div style={{ display: 'flex', gap: 8 }}>
                        <button
                            onClick={() => setTaskFilter('my')}
                            style={{
                                padding: '8px 16px',
                                borderRadius: 10,
                                fontSize: 13,
                                fontWeight: 700,
                                cursor: 'pointer',
                                transition: 'all 0.2s',
                                border: 'none',
                                background: taskFilter === 'my' ? '#d4a574' : '#f1f5f9',
                                color: taskFilter === 'my' ? '#fff' : '#64748b',

```
