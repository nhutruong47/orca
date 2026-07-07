# Knowledge Document: GroupDetailPage.tsx (Chunk 105/136)

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
  "chunk_index": 104,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
 });
                                                    if (isEnd) dayEvents.push({ type: 'END', task: t });
                                                    if (isBetween) dayEvents.push({ type: 'BETWEEN', task: t });
                                                });

                                                const isSelected = item.isCurrentMonth && item.day === selectedCalendarDay;
                                                const hasStart = dayEvents.some(e => e.type === 'START');
                                                const hasEnd = dayEvents.some(e => e.type === 'END');
                                                const hasBetween = dayEvents.some(e => e.type === 'BETWEEN');
                                                const hasTasks = dayEvents.length > 0;

                                                let borderStyle = '1px solid #232328';
                                                let bgStyle = '#16161a';
                                                let colorStyle = item.isCurrentMonth ? '#ffffff' : '#4e4e54';
                                                let shadowStyle = 'none';

                                                if (hasEnd) {
                                                    borderStyle = '1px solid #ef4444';
                                                    bgStyle = 'rgba(239,68,68,0.06)';
                                                } else if (hasBetween) {
                                                    borderStyle = '1px solid #f59e0b';
                                                    bgStyle = 'rgba(245,158,11,0.06)';
                                                } else if (hasStart) {
                                                    borderStyle = '1px solid #3b82f6';
                                                    bgStyle = 'rgba(59,130,246,0.06)';
                                                }

                                                if (isSelected) {
                                                    borderStyle = '1.5px solid #e2b053';
                                                    bgStyle = '#1e1e1e';
                                                    shadowStyle = '0 0 12px rgba(226, 176, 83, 0.15)';
                                                }

                                                return (

```
