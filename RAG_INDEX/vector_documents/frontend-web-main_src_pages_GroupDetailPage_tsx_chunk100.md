# Knowledge Document: GroupDetailPage.tsx (Chunk 101/136)

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
  "chunk_index": 100,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                     const month = calendarDate.getMonth();

                            // Days calculations
                            const numDays = new Date(year, month + 1, 0).getDate();
                            const startDay = new Date(year, month, 1).getDay(); // Sunday=0, Monday=1
                            const offset = startDay === 0 ? 6 : startDay - 1; // Align to Monday start

                            const days = [];

                            // Prev month padding
                            const prevMonthNumDays = new Date(year, month, 0).getDate();
                            for (let i = offset - 1; i >= 0; i--) {
                                days.push({ day: prevMonthNumDays - i, isCurrentMonth: false, monthOffset: -1 });
                            }

                            // Current month days
                            for (let d = 1; d <= numDays; d++) {
                                days.push({ day: d, isCurrentMonth: true, monthOffset: 0 });
                            }

                            // Next month padding to fill grid to 35 or 42 cells
                            const totalCells = days.length <= 35 ? 35 : 42;
                            const nextPadding = totalCells - days.length;
                            for (let d = 1; d <= nextPadding; d++) {
                                days.push({ day: d, isCurrentMonth: false, monthOffset: 1 });
                            }

                            // Filter tasks for current calendar view
                            const getTasksForDay = (cellDay: number, cellMonthOffset: number) => {
                                const targetMonth = month + cellMonthOffset;
                                const targetDate = new Date(year, targetMonth, cellDay);
                                targetDate.setHours(0,0,0,0);

                                return latestGoalTasks.filter(t => {
                                    const start = t.createdAt ? new Date(t.createdAt) : null;
                                    if (start) start.setHours(0,0,0,0);
                                    const end = (t.dueTime || t.deadline) ? new Date(t.dueTime || t.deadline) : null;
                                    if (end) end.setHours(0,0,0,0);

                                    const isStart = start && start.getTime() === targetDate.getTime();

```
