# Knowledge Document: GroupDetailPage.tsx (Chunk 93/136)

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
  "chunk_index": 92,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
t] = { target: 0, actual: 0 };
                                                    map[unit].target += target;
                                                    map[unit].actual += actual;
                                                });
                                                const items = Object.entries(map);
                                                if (items.length === 0) {
                                                    return <div style={{ fontSize: 13, color: 'var(--text-muted)', textAlign: 'center', padding: '40px 0' }}>Chưa có dữ liệu sản lượng.</div>;
                                                }
                                                return items.map(([unit, val]) => {
                                                    const pct = val.target > 0 ? Math.min(100, Math.round((val.actual / val.target) * 100)) : 0;
                                                    return (
                                                        <div key={unit} style={{ background: 'var(--bg-card, #1e293b)', padding: '16px', borderRadius: 14, border: '1px solid var(--border, #334155)' }}>
                                                            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 13, fontWeight: 700, color: 'var(--text-primary)', marginBottom: 8 }}>
                                                                <span style={{ display: 'flex', alignItems: 'center', gap: 6 }}><ion-icon name="pricetag-outline" style={{ color: '#d4a574', fontSize: 14 }}></ion-icon> Đơn vị: {unit}</span>
                                                                <span style={{ color: '#d4a574' }}>{val.actual} / {val.target} {unit} ({pct}%)</span>
                                                            </div>
                                                            <div style={{ height: 20, background: 'var(--bg-input, #0f172a)', borderRadius: 10, overflow: 'hidden', position: 'relative', display: 'flex', alignItems: 'center' }}>
                                                                <div style={{ height: '100%', background: 'linear-gradient(90deg, #d4a574 0%, #f59e0b 100%)', width: `${pct}%`, borderRadius: 10, transition: 'width 0.6s cubic-bezier(0.4, 0, 0.2, 1)' }} />

```
