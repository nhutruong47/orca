# Knowledge Document: GroupDetailPage.tsx (Chunk 34/136)

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
  "chunk_index": 33,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
            fontSize: 13,
                                fontWeight: 700,
                                cursor: 'pointer',
                                transition: 'all 0.2s',
                                border: 'none',
                                background: taskFilter === 'my' ? '#d4a574' : '#f1f5f9',
                                color: taskFilter === 'my' ? '#fff' : '#64748b',
                                display: 'flex',
                                alignItems: 'center',
                                gap: 6
                            }}
                        >
                            <ion-icon name="person-outline"></ion-icon>
                            Việc của tôi
                            <span style={{
                                background: taskFilter === 'my' ? 'rgba(255,255,255,0.2)' : 'rgba(0,0,0,0.05)',
                                padding: '1px 6px',
                                borderRadius: 6,
                                fontSize: 11,
                                marginLeft: 6
                            }}>
                                {latestGoalTasks.filter(t => t.memberId === user?.id).length}
                            </span>
                        </button>
                        {isAdmin && (
                            <button
                                onClick={() => setTaskFilter('all')}
                                style={{
                                    padding: '8px 16px',
                                    borderRadius: 10,
                                    fontSize: 13,
                                    fontWeight: 700,
                                    cursor: 'pointer',
                                    transition: 'all 0.2s',
                                    border: 'none',
                                    background: taskFilter === 'all' ? '#d4a574' : '#f1f5f9',
                                    color: taskFilter === 'all' ? '#fff' : '#64748b',
                                    display: 'flex',
                                    alignItems: 'center',
                                    gap: 6
                                }}
                            >
                                <ion-icon name="people-outline"></ion-icon>
                                Tất cả công việc
                                <span style={{

```
