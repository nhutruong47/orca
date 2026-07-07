# Knowledge Document: GroupDetailPage.tsx (Chunk 107/136)

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
  "chunk_index": 106,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
             justifyContent: 'space-between',
                                                             cursor: 'pointer',
                                                             position: 'relative',
                                                             transition: 'all 0.2s ease',
                                                             opacity: item.isCurrentMonth ? 1 : 0.45
                                                         }}
                                                     >
                                                         {/* Day number */}
                                                         <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                                             <span style={{ fontSize: 14, fontWeight: 700, color: colorStyle }}>{item.day}</span>
                                                             {hasEnd && (
                                                                 <span style={{ width: 6, height: 6, borderRadius: '50%', background: '#ef4444' }} title="Hạn chót nhiệm vụ!" />
                                                             )}
                                                         </div>

                                                         {/* Task List Pills (Only if present) */}
                                                          {hasTasks && (
                                                              <div style={{ display: 'flex', gap: 3, marginTop: 4, flexWrap: 'wrap' }}>
                                                                  {dayEvents.slice(0, 3).map((ev, evIdx) => {
                                                                      let dotColor = '#94a3b8';
                                                                      if (ev.type === 'START') dotColor = '#3b82f6';
                                                                      else if (ev.type === 'END') dotColor = '#ef4444';
                                                                      else if (ev.type === 'BETWEEN') dotColor = '#f59e0b';
                                                                      if (ev.task.status === 'COMPLETED') dotColor = '#10b981';

                                                                      return (

```
