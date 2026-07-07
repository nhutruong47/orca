# Knowledge Document: GroupDetailPage.tsx (Chunk 86/136)

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
  "chunk_index": 85,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
yContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border, #334155)', paddingBottom: 20 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                                <span style={{ width: 44, height: 44, borderRadius: 12, background: 'rgba(212,165,116,0.15)', display: 'grid', placeItems: 'center', color: '#d4a574' }}>
                                    <ion-icon name="analytics-outline" style={{ fontSize: 24 }}></ion-icon>
                                </span>
                                <div>
                                    <h2 style={{ margin: 0, fontSize: 22, fontWeight: 800, color: 'var(--text-primary)' }}>
                                        Báo cáo & Phân tích Thống kê Sản xuất
                                    </h2>
                                    <p style={{ margin: '4px 0 0', fontSize: 13, color: 'var(--text-secondary, #94a3b8)' }}>Dữ liệu thời gian thực của nhóm: <b>{team.name}</b></p>
                                </div>
                            </div>
                            <button onClick={() => setShowStatsModal(false)} style={{ background: 'var(--bg-input, #f1f5f9)', border: 'none', width: 36, height: 36, borderRadius: '50%', display: 'grid', placeItems: 'center', cursor: 'pointer', color: 'var(--text-secondary)' }}><ion-icon name="close" style={{ fontSize: 22 }}></ion-icon></button>
                        </div>

                        {/* Top Metrics Grid */}
                        {(() => {
                            const total = latestGoalTasks.length;
                            const completed = latestGoalTasks.filter(t => t.status === 'COMPLETED').length;
                            const inProgress = latestGoalTasks.filter(t => t.status === 'IN_PROGRESS').length;
                            const pending = latestGoalTasks.filter(t => t.status === 'PENDING').length;

                            // Calculate total yield rate
                            let totalTarget = 0;
                            let totalActual = 0;
                            latestGoalTasks.forEach(t => {
                                totalTarget += Number(t.outputTarget ?? t.workload ?? 0);
                                totalActual += Number(t.actualOutput ?? 0);
                            });

```
