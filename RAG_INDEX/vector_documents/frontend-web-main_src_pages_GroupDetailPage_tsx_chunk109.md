# Knowledge Document: GroupDetailPage.tsx (Chunk 110/136)

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
  "chunk_index": 109,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
tween', alignItems: 'center' }}>
                                                <span>Ngày {selectedCalendarDay}/{month + 1}</span>
                                                <span style={{ fontSize: 12, fontWeight: 500, color: '#8e8e93', background: '#2c2c2e', padding: '3px 10px', borderRadius: 12 }}>{selectedTasks.length} công việc</span>
                                            </h3>

                                            <div style={{ display: 'flex', flexDirection: 'column', gap: 12, minHeight: 120, justifyContent: selectedTasks.length === 0 ? 'center' : 'flex-start', alignItems: selectedTasks.length === 0 ? 'center' : 'stretch' }}>
                                                {selectedTasks.length === 0 ? (
                                                    <>
                                                        <div style={{ width: 64, height: 64, borderRadius: '50%', border: '1.5px dashed #3a3a3c', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#8e8e93', marginBottom: 4 }}>
                                                            <ion-icon name="calendar-outline" style={{ fontSize: 28 }}></ion-icon>
                                                        </div>
                                                        <div style={{ textAlign: 'center', color: '#8e8e93', fontSize: 13, fontWeight: 500 }}>Không có lịch trình nào vào ngày này.</div>
                                                    </>
                                                ) : (
                                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 10, maxHeight: 220, overflowY: 'auto', paddingRight: 4 }}>
                                                        {selectedTasks.map(t => {
                                                            const isTaskOverdue = (t.dueTime || t.deadline) && new Date(t.dueTime || t.deadline!).getTime() < Date.now() && t.status !== 'COMPLETED';
                                                            const inProgress = t.status === 'IN_PROGRESS';

                                                            let pillBg = '#262629';
                                                            let pillBorder = '1px solid #3a3a3c';
                                                            let pillColor = '#ffffff';


```
