# Knowledge Document: GroupDetailPage.tsx (Chunk 87/136)

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
  "chunk_index": 86,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
               // Calculate total yield rate
                            let totalTarget = 0;
                            let totalActual = 0;
                            latestGoalTasks.forEach(t => {
                                totalTarget += Number(t.outputTarget ?? t.workload ?? 0);
                                totalActual += Number(t.actualOutput ?? 0);
                            });
                            const yieldRate = totalTarget > 0 ? Math.min(100, Math.round((totalActual / totalTarget) * 100)) : 0;

                            return (
                                <>
                                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 18 }}>
                                    {[
                                        { label: 'Tổng số công việc', value: total, unit: 'nhiệm vụ', icon: 'clipboard-outline', bg: 'rgba(212,165,116,0.1)', color: '#d4a574' },
                                        { label: 'Đã hoàn thành', value: completed, unit: 'nhiệm vụ', icon: 'checkmark-circle-outline', bg: 'rgba(16,185,129,0.1)', color: '#10b981' },
                                        { label: 'Đang thực hiện', value: inProgress, unit: 'nhiệm vụ', icon: 'sync-outline', bg: 'rgba(59,130,246,0.1)', color: '#3b82f6' },
                                        { label: 'Hiệu suất sản lượng', value: `${yieldRate}%`, unit: `${totalActual}/${totalTarget} mục tiêu`, icon: 'trending-up-outline', bg: 'rgba(245,158,11,0.1)', color: '#f59e0b' }
                                    ].map((m, idx) => (
                                        <div key={idx} style={{ background: 'var(--bg-secondary, #1e293b)', padding: '20px', borderRadius: 16, border: '1px solid var(--border, #334155)', display: 'flex', alignItems: 'center', gap: 16 }}>
                                            <div style={{ width: 48, height: 48, borderRadius: 12, background: m.bg, display: 'flex', alignItems: 'center', justifyContent: 'center', color: m.color, fontSize: 24 }}>
                                                <ion-icon name={m.icon}></ion-icon>
                                            </div>
                                            <div>
                                                <div style={{ fontSize: 26, fontWeight: 800, color: 'var(--text-primary)' }}>{m.value}</div>

```
