# Knowledge Document: FactoryDashboardPage.tsx (Chunk 2/14)

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
  "chunk_index": 1,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
ding: 40, textAlign: 'center', color: 'var(--text-muted)' }}>
            Dang tai dashboard...
        </div>
    );

    if (!dashboard) return (
        <div style={{ padding: 40, textAlign: 'center', color: 'var(--text-muted)' }}>
            Khong co du lieu
        </div>
    );

    const todayTarget = dashboard.todayTarget || {};
    const completionRate = todayTarget.completionRate || 0;
    const progressColor = completionRate >= 100 ? '#10b981' : completionRate >= 80 ? '#f59e0b' : '#ef4444';

    return (
        <div style={{ padding: 24, margin: '0 auto' }}>
            {/* Header */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 24 }}>
                <button onClick={() => navigate(`/groups/${teamId}`)} style={{
                    background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                    width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                    color: 'var(--text-secondary)', fontSize: 18,
                }}>
                    <ion-icon name="chevron-back-outline" />
                </button>
                <h1 style={{ fontSize: 22, fontWeight: 800, color: 'var(--text-primary)', margin: 0 }}>
                    Dashboard Xuong
                </h1>
            </div>

            {/* Alerts */}
            {dashboard.alerts?.length > 0 && (
                <div style={{ marginBottom: 24 }}>
                    {dashboard.alerts.map((alert: any, i: number) => (
                        <div key={i} style={{
                            display: 'flex', alignItems: 'center', gap: 10,
                            padding: '10px 14px', marginBottom: 8,
                            background: alert.level === 'warning' ? 'rgba(245,158,11,0.1)' : 'rgba(59,130,246,0.1)',
                            border: `1px solid ${alert.level === 'warning' ? 'rgba(245,158,11,0.3)' : 'rgba(59,130,246,0.3)'}`,
                            borderRadius: 10, fontSize: 13, color: alert.level === 'warning' ? '#d97706' : '#2563eb'
                        }}>
                            <span style={{ fontSize: 16 }}>{alert.level === 'warning' ? '⚠️' : 'ℹ️'}</span>
                            <span style={{ flex: 1 }}>{alert.message}</span>
                        </div>
                    ))}

```
