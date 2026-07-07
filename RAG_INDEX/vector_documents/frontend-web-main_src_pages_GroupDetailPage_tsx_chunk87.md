# Knowledge Document: GroupDetailPage.tsx (Chunk 88/136)

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
  "chunk_index": 87,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
ems: 'center', justifyContent: 'center', color: m.color, fontSize: 24 }}>
                                                <ion-icon name={m.icon}></ion-icon>
                                            </div>
                                            <div>
                                                <div style={{ fontSize: 26, fontWeight: 800, color: 'var(--text-primary)' }}>{m.value}</div>
                                                <div style={{ fontSize: 11, color: 'var(--text-muted, #94a3b8)', fontWeight: 600, textTransform: 'uppercase', marginTop: 2 }}>{m.label}</div>
                                                <div style={{ fontSize: 11, color: 'var(--text-secondary)', marginTop: 2 }}>{m.unit}</div>
                                            </div>
                                        </div>
                                    ))}
                                </div>

                                {/* Main Dashboard Grid */}
                                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(480px, 1fr))', gap: 24 }}>

                                    {/* Left Column: Radial Chart & Completion Rate Details */}
                                    <div style={{ background: 'var(--bg-secondary, #1e293b)', padding: '24px', borderRadius: 18, border: '1px solid var(--border, #334155)', display: 'flex', flexDirection: 'column', gap: 20 }}>
                                        <h3 style={{ fontSize: 16, fontWeight: 700, margin: 0, color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: 8 }}>
                                            <ion-icon name="pie-chart-outline" style={{ color: '#d4a574' }}></ion-icon>
                                            Phân tích tỷ lệ hoàn thành
                                        </h3>

                                        {(() => {
                                            const rate = total > 0 ? Math.round((completed / total) * 100) : 0;
                                            const rad = 60;
                                            const circ = 2 * Math.PI * rad;
                                            const offset = circ - (rate / 100) * circ;
                                            return (

```
