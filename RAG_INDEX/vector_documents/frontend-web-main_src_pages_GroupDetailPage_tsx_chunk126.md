# Knowledge Document: GroupDetailPage.tsx (Chunk 127/136)

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
  "chunk_index": 126,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`;
                                    return <option key={val} value={val} style={{ color: '#000' }}>{d.toLocaleDateString('vi-VN', { month: 'long', year: 'numeric' })}</option>;
                                })}
                            </select>
                            <button
                                onClick={() => {
                                    const [y, m] = selectedMonth.split('-').map(Number);
                                    const next = new Date(y, m);
                                    const now = new Date();
                                    if (next <= now) {
                                        setSelectedMonth(`${next.getFullYear()}-${String(next.getMonth() + 1).padStart(2, '0')}`);
                                    }
                                }}
                                style={{ width: 32, height: 32, borderRadius: 8, border: '1px solid #e2e8f0', background: '#fff', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
                            >
                                <svg width="16" height="16" fill="none" stroke="#64748b" strokeWidth="2"><path d="M9 18l6-6-6-6"/></svg>
                            </button>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                            <span style={{ fontSize: 12, color: '#64748b' }}>
                                <svg width="12" height="12" fill="none" stroke="currentColor" strokeWidth="2" style={{ verticalAlign: 'middle', marginRight: 4 }}><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
                                Tự động cập nhật theo giờ công
                            </span>
                        </div>
                    </div>

                    <div style={{ background: '#fff' }}>
                        {/* Summary Stats */}
                        <div style={{ padding: '20px 24px', display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 16 }}>
                            {[
                                { label: 'Tổng nhân viên', value: salaryData.length, icon: '👥', color: '#1e293b' },
                                { label: 'Tổng công việc', value: totalTasks.toLocaleString(), icon: '📋', color: '#1e293b' },

```
