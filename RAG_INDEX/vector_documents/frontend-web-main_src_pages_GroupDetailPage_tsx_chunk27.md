# Knowledge Document: GroupDetailPage.tsx (Chunk 28/136)

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
  "chunk_index": 27,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
ing: 20 }}>
                    <div style={{ fontSize: 11, fontWeight: 800, color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: 10 }}>Roadmap tu task database</div>
                    <table style={{ width: '100%', borderCollapse: 'collapse', border: '1px solid var(--border)', borderRadius: 10, overflow: 'hidden' }}>
                        <thead>
                            <tr style={{ background: 'var(--bg-secondary)' }}>
                                {['STT', 'Cong viec', 'Nguoi chinh', 'Du phong', 'Trang thai', 'Tien do'].map((h, i) => (
                                    <th key={i} style={{ padding: '10px 12px', textAlign: 'left', fontSize: 11, fontWeight: 800, color: 'var(--text-secondary)', borderBottom: '1px solid var(--border)' }}>{h}</th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {latestGoalTasks.length === 0 ? (
                                <tr><td colSpan={6} style={{ textAlign: 'center', padding: 28, color: 'var(--text-muted)', fontSize: 13 }}>Chua co task trong database</td></tr>
                            ) : latestGoalTasks.map((task, index) => {
                                const actual = Number(task.actualOutput ?? 0);
                                const target = Number(task.outputTarget ?? 0);
                                const progressPct = target > 0 ? Math.min(100, Math.round((actual / target) * 100)) : (task.completionPercentage || 0);

                                let displayStatusKey = task.status;
                                if (target > 0) {
                                    if (progressPct >= 100) {
                                        displayStatusKey = 'COMPLETED';
                                    } else if (progressPct > 0) {
                                        displayStatusKey = 'IN_PROGRESS';
                                    } else {
                                        displayStatusKey = 'PENDING';
                                    }
                                }
                                const status = STATUS_COLORS[displayStatusKey] || STATUS_COLORS.PENDING;
                                return (

```
