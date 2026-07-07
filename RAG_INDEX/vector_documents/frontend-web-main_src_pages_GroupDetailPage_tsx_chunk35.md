# Knowledge Document: GroupDetailPage.tsx (Chunk 36/136)

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
  "chunk_index": 35,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
14, fontWeight: 600, marginBottom: 8 }}>Loại công việc / Mục tiêu</label>
                                    <select value={selectedGoalId || ''} onChange={e => setSelectedGoalId(e.target.value)} style={{ width: '100%', padding: '12px 14px', borderRadius: 8, border: '1px solid var(--border, #cbd5e1)', fontSize: 14, background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)' }}>
                                        <option value="">Công việc thủ công</option>
                                        {goals.map(g => <option key={g.id} value={g.id}>{g.title}</option>)}
                                    </select>
                                </div>
                                <div>
                                    <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Tên task <span style={{ color: '#dc2626' }}>*</span></label>
                                    <input value={newTaskTitle} onChange={e => setNewTaskTitle(e.target.value)} placeholder="Tên task" style={{ width: '100%', padding: '12px 14px', borderRadius: 8, border: '1px solid var(--border, #cbd5e1)', fontSize: 14, background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }} autoFocus />
                                </div>
                                <div>
                                    <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Mô tả</label>
                                    <input value={newTaskDesc} onChange={e => setNewTaskDesc(e.target.value)} placeholder="Mô tả công việc..." style={{ width: '100%', padding: '12px 14px', borderRadius: 8, border: '1px solid var(--border, #cbd5e1)', fontSize: 14, background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }} />
                                </div>
                                <div style={{ display: 'flex', gap: 14 }}>
                                    <div style={{ flex: 1 }}>
                                        <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Giai đoạn</label>

```
