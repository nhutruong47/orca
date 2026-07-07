# Knowledge Document: GroupDetailPage.tsx (Chunk 104/136)

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
  "chunk_index": 103,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
fontSize: 13, color: '#8e8e93' }}>
                                            {['Th 2', 'Th 3', 'Th 4', 'Th 5', 'Th 6', 'Th 7', 'CN'].map(d => (
                                                <div key={d} style={{ padding: '6px 0' }}>{d}</div>
                                            ))}
                                        </div>

                                        {/* Days Grid */}
                                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)', gap: 8 }}>
                                            {days.map((item, idx) => {
                                                const cellDate = new Date(year, month + item.monthOffset, item.day);
                                                cellDate.setHours(0,0,0,0);

                                                // Find events for this cell
                                                const dayEvents: any[] = [];
                                                latestGoalTasks.forEach(t => {
                                                    const start = t.createdAt ? new Date(t.createdAt) : null;
                                                    if (start) start.setHours(0,0,0,0);
                                                    const end = (t.dueTime || t.deadline) ? new Date(t.dueTime || t.deadline) : null;
                                                    if (end) end.setHours(0,0,0,0);

                                                    const isStart = start && start.getTime() === cellDate.getTime();
                                                    const isEnd = end && end.getTime() === cellDate.getTime();
                                                    const isBetween = start && end && cellDate.getTime() > start.getTime() && cellDate.getTime() < end.getTime() && t.status === 'IN_PROGRESS';

                                                    if (isStart) dayEvents.push({ type: 'START', task: t });
                                                    if (isEnd) dayEvents.push({ type: 'END', task: t });
                                                    if (isBetween) dayEvents.push({ type: 'BETWEEN', task: t });
                                                });

                                                const isSelected = item.isCurrentMonth && item.day === selectedCalendarDay;

```
