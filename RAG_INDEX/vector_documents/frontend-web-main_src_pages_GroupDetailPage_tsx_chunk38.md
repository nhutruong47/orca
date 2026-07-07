# Knowledge Document: GroupDetailPage.tsx (Chunk 39/136)

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
  "chunk_index": 38,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
> setNewTaskUnit(e.target.value)}
                                            placeholder="kg, gói, hộp, chai, tem, mẫu, đơn..."
                                            style={{ width: '100%', padding: '12px 14px', borderRadius: 8, border: '1px solid var(--border, #cbd5e1)', fontSize: 14, background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)', boxSizing: 'border-box' }}
                                        />
                                    </div>
                                </div>
                            </div>
                            <div style={{ display: 'flex', gap: 10, justifyContent: 'flex-end', marginTop: 28 }}>
                                <button onClick={() => setShowAddTask(false)} style={{ padding: '10px 20px', borderRadius: 10, border: '1px solid var(--border, #e2e8f0)', background: 'transparent', color: 'var(--text-primary, #64748b)', fontSize: 14, fontWeight: 600, cursor: 'pointer' }}>Hủy</button>
                                <button onClick={handleAddTask} disabled={loading || !newTaskTitle.trim()} style={{ padding: '10px 20px', borderRadius: 10, border: 'none', background: '#d4a574', color: '#fff', fontSize: 14, fontWeight: 600, cursor: 'pointer', opacity: (loading || !newTaskTitle.trim()) ? 0.6 : 1 }}>
                                    {loading ? 'Đang tạo...' : 'Tạo công việc'}
                                </button>
                            </div>
                        </div>
                    </div>
                )}

        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                    <thead>
                        <tr style={{ background: 'var(--bg-secondary)' }}>
                            {['Tên công việc', 'Tiến độ', 'Ưu tiên', 'Thành viên', ''].map((h, i) => (
                                <th key={i} style={{ padding: '10px 16px', textAlign: 'left', fontSize: 11, fontWeight: 700, color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.05em', borderBottom: '1px solid var(--border)' }}>{h}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {(() => {
                            const filtered = (taskFilter === 'my' || !isAdmin) ? latestGoalTasks.filter(t => t.memberId === user?.id) : latestGoalTasks;

```
