# Knowledge Document: GroupDetailPage.tsx (Chunk 129/136)

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
  "chunk_index": 128,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
/p>
                            </div>
                        ) : salaryData.length === 0 ? (
                            <div style={{ padding: 60, textAlign: 'center', color: '#94a3b8' }}>
                                <div style={{ fontSize: 48, marginBottom: 12 }}>📭</div>
                                <p style={{ fontSize: 15, fontWeight: 600, marginBottom: 4 }}>Chưa có dữ liệu lương</p>
                                <p style={{ fontSize: 13 }}>Nhân viên chưa có task hoàn thành trong tháng này</p>
                            </div>
                        ) : (
                            <div style={{ padding: '0 28px 24px' }}>
                                <div style={{
                                    display: 'grid',
                                    gridTemplateColumns: '2fr 1fr 1fr 1fr 1.2fr 1.3fr',
                                    gap: 12, padding: '12px 16px',
                                    background: 'var(--bg-input, rgba(255, 255, 255, 0.03))', borderRadius: '12px 12px 0 0',
                                    borderBottom: '1px solid var(--border)'
                                }}>
                                    {['Nhân viên', 'Tổng task', 'Hoàn thành', 'Giờ công (Thường + Tăng ca)', 'Đơn giá/giờ', 'Lương thực nhận'].map((h, i) => (
                                        <div key={i} style={{
                                            fontSize: 11, fontWeight: 700, color: '#64748b',
                                            textTransform: 'uppercase', letterSpacing: '0.05em',
                                            textAlign: i >= 1 ? 'center' : 'left'
                                        }}>{h}</div>
                                    ))}
                                </div>

                                {salaryData.map((s, idx) => {
                                    const salary = calculateSalary(s);
                                    const completionRate = s.totalTasks > 0 ? Math.round((s.completedTasks / s.totalTasks) * 100) : 0;
                                    const isEditing = editingRate === s.memberId;

                                    return (
                                        <div key={s.memberId} style={{
                                            display: 'grid',
                                            gridTemplateColumns: '2fr 1fr 1fr 1fr 1.2fr 1.3fr',

```
