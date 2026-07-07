# Knowledge Document: GroupDetailPage.tsx (Chunk 38/136)

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
  "chunk_index": 37,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                   </select>
                                    </div>
                                </div>
                                <div style={{ display: 'flex', gap: 14 }}>
                                    <div style={{ flex: 2 }}>
                                        <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Hạn chót (Deadline)</label>
                                        <input value={newTaskDueTime} onChange={e => setNewTaskDueTime(e.target.value)} type="datetime-local" style={{ width: '100%', padding: '12px 14px', borderRadius: 8, border: '1px solid var(--border, #cbd5e1)', fontSize: 14, background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }} />
                                    </div>
                                    <div style={{ flex: 1 }}>
                                        <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Giờ công</label>
                                        <input value={newTaskWorkload} onChange={e => setNewTaskWorkload(e.target.value)} placeholder="0" type="number" min="0" style={{ width: '100%', padding: '12px 14px', borderRadius: 8, border: '1px solid var(--border, #cbd5e1)', fontSize: 14, background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }} />
                                    </div>
                                    <div style={{ flex: 1 }}>
                                        <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Đơn vị <span style={{ color: '#94a3b8', fontWeight: 400 }}>(tự đoán)</span></label>
                                        <input
                                            value={newTaskUnit || inferUnitFromText(`${newTaskTitle} ${newTaskDesc}`, newTaskStage)}
                                            onChange={e => setNewTaskUnit(e.target.value)}
                                            placeholder="kg, gói, hộp, chai, tem, mẫu, đơn..."
                                            style={{ width: '100%', padding: '12px 14px', borderRadius: 8, border: '1px solid var(--border, #cbd5e1)', fontSize: 14, background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }}

```
