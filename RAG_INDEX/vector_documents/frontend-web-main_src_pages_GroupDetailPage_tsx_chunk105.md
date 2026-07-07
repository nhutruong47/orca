# Knowledge Document: GroupDetailPage.tsx (Chunk 106/136)

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
  "chunk_index": 105,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
         if (isSelected) {
                                                    borderStyle = '1.5px solid #e2b053';
                                                    bgStyle = '#1e1e1e';
                                                    shadowStyle = '0 0 12px rgba(226, 176, 83, 0.15)';
                                                }

                                                return (
                                                     <div
                                                         key={idx}
                                                         onClick={(e) => {
                                                             e.stopPropagation();
                                                             if (item.monthOffset !== 0) {
                                                                 setCalendarDate(new Date(year, month + item.monthOffset, 1));
                                                             }
                                                             setSelectedCalendarDay(item.day);
                                                         }}
                                                         style={{
                                                             aspectRatio: '1/1',
                                                             minHeight: 80,
                                                             borderRadius: 10,
                                                             border: borderStyle,
                                                             background: bgStyle,
                                                             boxShadow: shadowStyle,
                                                             padding: '10px',
                                                             display: 'flex',
                                                             flexDirection: 'column',
                                                             justifyContent: 'space-between',
                                                             cursor: 'pointer',
                                                             position: 'relative',
                                                             transition: 'all 0.2s ease',
                                                             opacity: item.isCurrentMonth ? 1 : 0.45

```
