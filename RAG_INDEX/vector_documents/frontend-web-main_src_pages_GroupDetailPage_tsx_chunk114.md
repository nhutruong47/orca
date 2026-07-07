# Knowledge Document: GroupDetailPage.tsx (Chunk 115/136)

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
  "chunk_index": 114,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                                  </button>
                                                        )}
                                                    </>
                                                ) : (
                                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 10, width: '100%', maxHeight: 200, overflowY: 'auto', paddingRight: 4 }}>
                                                        {latestGoalTasks.filter(t => t.status === 'IN_PROGRESS').map(t => {
                                                            const dueTime = t.dueTime || t.deadline;
                                                            const formatted = dueTime ? new Date(dueTime).toLocaleDateString('vi-VN', { month: 'numeric', day: 'numeric', hour: '2-digit', minute: '2-digit' }) : 'Không có hạn';
                                                            return (
                                                                <div key={t.id} style={{ background: '#262629', padding: '10px 12px', borderRadius: 10, border: '1px solid #f59e0b', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: 10 }}>
                                                                    <div style={{ minWidth: 0, flex: 1 }}>
                                                                        <div style={{ fontSize: 12, fontWeight: 700, color: '#ffffff', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>{t.title}</div>
                                                                        <div style={{ fontSize: 10, color: '#8e8e93', marginTop: 2 }}>Giai đoạn: {t.productionStage || '—'}</div>
                                                                    </div>
                                                                    <div style={{ textAlign: 'right', flexShrink: 0 }}>
                                                                        <div style={{ fontSize: 11, fontWeight: 700, color: '#f59e0b' }}>{formatted}</div>
                                                                        <div style={{ fontSize: 9, color: '#8e8e93', textTransform: 'uppercase', marginTop: 1 }}>Hạn chót</div>
                                                                    </div>
                                                                </div>

```
