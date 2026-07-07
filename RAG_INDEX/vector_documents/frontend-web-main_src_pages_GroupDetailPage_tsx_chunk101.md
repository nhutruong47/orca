# Knowledge Document: GroupDetailPage.tsx (Chunk 102/136)

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
  "chunk_index": 101,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
tedAt ? new Date(t.createdAt) : null;
                                    if (start) start.setHours(0,0,0,0);
                                    const end = (t.dueTime || t.deadline) ? new Date(t.dueTime || t.deadline) : null;
                                    if (end) end.setHours(0,0,0,0);

                                    const isStart = start && start.getTime() === targetDate.getTime();
                                    const isEnd = end && end.getTime() === targetDate.getTime();
                                    const isBetween = start && end && targetDate.getTime() > start.getTime() && targetDate.getTime() < end.getTime() && t.status === 'IN_PROGRESS';

                                    return isStart || isEnd || isBetween;
                                });
                            };

                            const handlePrevMonth = () => {
                                setCalendarDate(new Date(year, month - 1, 1));
                            };

                            const handleNextMonth = () => {
                                setCalendarDate(new Date(year, month + 1, 1));
                            };

                            const selectedTasks = getTasksForDay(selectedCalendarDay, 0);

                            return (
                                <div style={{ display: 'grid', gridTemplateColumns: '1.6fr 1fr', gap: 24, alignItems: 'start', width: '100%' }}>

                                    {/* Left Side: Calendar Grid */}
                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
                                        {/* Month Header Controller */}
                                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                            <h3 style={{ margin: 0, fontSize: 18, fontWeight: 700, color: '#ffffff' }}>
                                                Tháng {month + 1}, {year}
                                            </h3>
                                            <div style={{ display: 'flex', gap: 8 }}>

```
