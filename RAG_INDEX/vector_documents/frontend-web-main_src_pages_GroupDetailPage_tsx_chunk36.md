# Knowledge Document: GroupDetailPage.tsx (Chunk 37/136)

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
  "chunk_index": 36,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }} />
                                </div>
                                <div style={{ display: 'flex', gap: 14 }}>
                                    <div style={{ flex: 1 }}>
                                        <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Giai đoạn</label>
                                        <select value={newTaskStage} onChange={e => setNewTaskStage(e.target.value)} style={{ width: '100%', padding: '12px 14px', borderRadius: 8, border: '1px solid var(--border, #cbd5e1)', fontSize: 14, background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)' }}>
                                            {['Roasting', 'Cooling', 'Grinding', 'Packaging', 'Quality Check', 'Inventory'].map(stage => <option key={stage} value={stage}>{stage}</option>)}
                                        </select>
                                    </div>
                                    <div style={{ flex: 1 }}>
                                        <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Mức ưu tiên</label>
                                        <select value={newTaskPriority} onChange={e => setNewTaskPriority(Number(e.target.value))} style={{ width: '100%', padding: '12px 14px', borderRadius: 8, border: '1px solid var(--border, #cbd5e1)', fontSize: 14, background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)' }}>
                                            <option value={1}>Thấp</option>
                                            <option value={2}>Trung bình</option>
                                            <option value={3}>Cao</option>
                                        </select>
                                    </div>
                                </div>
                                <div style={{ display: 'flex', gap: 14 }}>
                                    <div style={{ flex: 2 }}>
                                        <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Hạn chót (Deadline)</label>

```
