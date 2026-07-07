# Knowledge Document: GroupDetailPage.tsx (Chunk 98/136)

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
  "chunk_index": 97,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
: 4 }}>
                                            {(() => {
                                                const map: Record<string, number> = {};
                                                let maxCount = 0;
                                                latestGoalTasks.forEach(t => {
                                                    const stage = t.productionStage || 'Chưa phân loại';
                                                    map[stage] = (map[stage] || 0) + 1;
                                                    if (map[stage] > maxCount) maxCount = map[stage];
                                                });
                                                const items = Object.entries(map);
                                                if (items.length === 0) {
                                                    return <div style={{ fontSize: 13, color: 'var(--text-muted)', textAlign: 'center', padding: '40px 0' }}>Không có giai đoạn nào.</div>;
                                                }
                                                return items.map(([stage, count], i) => {
                                                    return (
                                                        <div key={i} style={{ background: 'var(--bg-card, #1e293b)', padding: '12px 14px', borderRadius: 12, border: '1px solid var(--border, #334155)', display: 'flex', alignItems: 'center', gap: 16 }}>
                                                            <div style={{ width: 100, fontSize: 12, fontWeight: 700, color: 'var(--text-secondary)', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>
                                                                {stage}
                                                            </div>
                                                            <div style={{ flex: 1, height: 16, background: 'var(--bg-input, #0f172a)', borderRadius: 8, overflow: 'hidden', position: 'relative', display: 'flex', alignItems: 'center' }}>
                                                                <span style={{ position: 'absolute', right: 8, fontSize: 10, fontWeight: 800, color: '#fff' }}>{count} task</span>
                                                            </div>
                                                        </div>
                                                    );

```
