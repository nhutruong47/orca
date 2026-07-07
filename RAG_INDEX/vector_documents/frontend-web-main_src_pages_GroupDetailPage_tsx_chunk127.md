# Knowledge Document: GroupDetailPage.tsx (Chunk 128/136)

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
  "chunk_index": 127,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                       <div style={{ padding: '20px 24px', display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 16 }}>
                            {[
                                { label: 'Tổng nhân viên', value: salaryData.length, icon: '👥', color: '#1e293b' },
                                { label: 'Tổng công việc', value: totalTasks.toLocaleString(), icon: '📋', color: '#1e293b' },
                                { label: 'Hoàn thành', value: `${avgCompletion}%`, icon: '✅', color: '#10b981' },
                                { label: 'Tổng quỹ lương', value: `${(totalSalary / 1000000).toFixed(1)}M`, icon: '💰', color: '#d4a574' }
                            ].map((stat, i) => (
                                <div key={i} style={{
                                    padding: 16, borderRadius: 12, background: '#f8fafc',
                                    border: '1px solid #e2e8f0'
                                }}>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 8 }}>
                                        <span style={{ fontSize: 18 }}>{stat.icon}</span>
                                        <span style={{ fontSize: 12, color: '#64748b', fontWeight: 600 }}>{stat.label}</span>
                                    </div>
                                    <div style={{ fontSize: 24, fontWeight: 800, color: stat.color }}>{stat.value}</div>
                                </div>
                            ))}
                        </div>

                        {loadingSalary ? (
                            <div style={{ padding: 60, textAlign: 'center', color: '#94a3b8' }}>
                                <div style={{ width: 40, height: 40, border: '3px solid #e2e8f0', borderTopColor: '#d4a574', borderRadius: '50%', margin: '0 auto 16px', animation: 'spin 1s linear infinite' }}></div>
                                <p>Đang tải dữ liệu...</p>
                            </div>
                        ) : salaryData.length === 0 ? (
                            <div style={{ padding: 60, textAlign: 'center', color: '#94a3b8' }}>
                                <div style={{ fontSize: 48, marginBottom: 12 }}>📭</div>
                                <p style={{ fontSize: 15, fontWeight: 600, marginBottom: 4 }}>Chưa có dữ liệu lương</p>

```
