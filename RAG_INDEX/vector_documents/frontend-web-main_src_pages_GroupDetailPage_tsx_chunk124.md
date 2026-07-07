# Knowledge Document: GroupDetailPage.tsx (Chunk 125/136)

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
  "chunk_index": 124,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
ound((billableHours * rate) + (overtimeHours * overtimeRate));
    };

    const totalSalary = salaryData.reduce((sum, s) => sum + calculateSalary(s), 0);
    const totalTasks = salaryData.reduce((sum, s) => sum + s.totalTasks, 0);
    const totalCompleted = salaryData.reduce((sum, s) => sum + s.completedTasks, 0);
    const totalWorkload = salaryData.reduce((sum, s) => sum + s.totalWorkload, 0);
    const avgCompletion = totalTasks > 0 ? Math.round((totalCompleted / totalTasks) * 100) : 0;


    return (
        <div style={{ background: '#fff', borderRadius: 14, border: '1px solid #e2e8f0', overflow: 'hidden', marginBottom: 18 }}>
            {/* Header */}
            <div style={{ padding: '16px 24px', borderBottom: '1px solid #e2e8f0', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                    <h3 style={{ margin: 0, fontSize: 15, fontWeight: 700, color: '#1e293b' }}>
                        <ion-icon name="card-outline" style={{ fontSize: 18, verticalAlign: 'middle', marginRight: 6, color: '#d4a574' }}></ion-icon> BẢNG LƯƠNG NHÂN VIÊN
                    </h3>
                    <p style={{ margin: 0, fontSize: 13, color: '#64748b' }}>Theo dõi & quản lý chi phí nhân sự</p>
                </div>
                <button onClick={() => { setShowSalary(p => !p); if (!showSalary) loadSalary(); }} style={{
                    background: 'transparent',
                    color: '#64748b',
                    border: 'none',
                    padding: '6px 12px', fontSize: 13, fontWeight: 600, cursor: 'pointer',
                    display: 'flex', alignItems: 'center', gap: 4,
                }}>
                    {showSalary ? 'Ẩn bảng' : 'Xem chi tiết'}
                    <ion-icon name={showSalary ? "chevron-up-outline" : "chevron-down-outline"}></ion-icon>
                </button>
            </div>

            {/* Month Selector & Content */}
            {showSalary && (
                <div style={{ borderTop: '1px solid #e2e8f0' }}>
                    <div style={{ padding: '16px 24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: '#f8fafc' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                            <button

```
