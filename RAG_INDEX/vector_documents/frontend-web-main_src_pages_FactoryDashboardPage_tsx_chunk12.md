# Knowledge Document: FactoryDashboardPage.tsx (Chunk 13/14)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/FactoryDashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "dashboard",
    "production",
    "factory",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 12,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
 dashboard.stats.totalOrders, color: 'var(--text-secondary)' },
                        ].map(stat => (
                            <div key={stat.label} style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 12, padding: 16, textAlign: 'center' }}>
                                <div style={{ fontSize: 24, fontWeight: 800, color: stat.color }}>{stat.value}</div>
                                <div style={{ fontSize: 12, color: 'var(--text-muted)', marginTop: 4 }}>{stat.label}</div>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Upcoming Deadlines */}
            {dashboard.upcomingDeadlines?.length > 0 && (
                <div>
                    <h2 style={{ fontSize: 16, fontWeight: 700, marginBottom: 12, color: 'var(--text-primary)' }}>Deadline sap toi</h2>
                    <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14, padding: 16 }}>
                        {dashboard.upcomingDeadlines?.map((d: any, i: number) => (
                            <div key={i} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 0', borderBottom: i < dashboard.upcomingDeadlines.length - 1 ? '1px solid var(--border)' : 'none' }}>
                                <div style={{ fontWeight: 600, fontSize: 14 }}>{d.title}</div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                    <span style={{ fontSize: 12, color: 'var(--text-secondary)' }}>
                                        {new Date(d.internalDeadline).toLocaleDateString('vi-VN')}
                                    </span>
                                    <span style={{
                                        fontSize: 11, fontWeight: 700, padding: '2px 8px', borderRadius: 4,
                                        background: d.daysRemaining <= 1 ? '#ef4444' : d.daysRemaining <= 3 ? '#f59e0b' : 'rgba(16,185,129,0.1)',
                                        color: d.daysRemaining <= 1 ? '#fff' : d.daysRemaining <= 3 ? '#fff' : '#10b981'
                                    }}>
                                        {d.daysRemaining} ngay
                                    </span>

```
