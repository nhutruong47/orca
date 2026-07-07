# Knowledge Document: GroupDetailPage.tsx (Chunk 41/136)

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
  "chunk_index": 40,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                                            <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                                                        <select value={editTaskStage} onChange={e => setEditTaskStage(e.target.value)} style={{ padding: '6px 8px', borderRadius: 8, border: '1px solid var(--border)', fontSize: 12, background: 'var(--bg-input)', color: 'var(--text-secondary)' }}>
                                                            {['Roasting', 'Cooling', 'Grinding', 'Packaging', 'Quality Check', 'Inventory'].map(stage => <option key={stage} value={stage}>{stage}</option>)}
                                                        </select>
                                                        <select value={editTaskPriority} onChange={e => setEditTaskPriority(Number(e.target.value))} style={{ padding: '6px 8px', borderRadius: 8, border: '1px solid var(--border)', fontSize: 12, background: 'var(--bg-input)', color: 'var(--text-secondary)' }}>
                                                            <option value={1}>Thấp</option>
                                                            <option value={2}>TB</option>
                                                            <option value={3}>Cao</option>
                                                        </select>
                                                        <input value={editTaskDueTime} onChange={e => setEditTaskDueTime(e.target.value)} type="datetime-local" style={{ padding: '6px 8px', borderRadius: 8, border: '1px solid var(--border)', fontSize: 12, color: 'var(--text-secondary)', background: 'var(--bg-input)' }} />
                                                        <input value={editTaskUnit || inferUnitFromText(`${editTaskTitle} ${editTaskDesc}`, editTaskStage)} onChange={e => setEditTaskUnit(e.target.value)} placeholder="Đơn vị" style={{ padding: '6px 8px', borderRadius: 8, border: '1px solid var(--border)', fontSize: 12, color: 'var(--text-secondary)', background: 'var(--bg-input)', width: 90 }} title="Đơn vị (kg, gói, hộp, chai, tem, mẫu, đơn...)" />
                                                    </div>
                                                </div>
                                            ) : (
                                                <>

```
