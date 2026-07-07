# Knowledge Document: GroupDetailPage.tsx (Chunk 92/136)

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
  "chunk_index": 91,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
lignItems: 'center', gap: 5 }}><span style={{ width: 8, height: 8, borderRadius: '50%', background: '#94a3b8' }}></span> Chờ xử lý ({pending})</span>
                                            </div>
                                        </div>
                                    </div>

                                    {/* Right Column: Yield Target vs. Actual (Real CSS/SVG Bar Charts) */}
                                    <div style={{ background: 'var(--bg-secondary, #1e293b)', padding: '24px', borderRadius: 18, border: '1px solid var(--border, #334155)', display: 'flex', flexDirection: 'column', gap: 20 }}>
                                        <h3 style={{ fontSize: 16, fontWeight: 700, margin: 0, color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: 8 }}>
                                            <ion-icon name="cube-outline" style={{ color: '#d4a574' }}></ion-icon>
                                            Tổng hợp sản lượng theo đơn vị mục tiêu
                                        </h3>

                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 16, maxHeight: 300, overflowY: 'auto', paddingRight: 4 }}>
                                            {(() => {
                                                const map: Record<string, { target: number; actual: number }> = {};
                                                latestGoalTasks.forEach(t => {
                                                    const unit = (t.unit && t.unit.trim()) ? t.unit : 'kg';
                                                    const target = Number(t.outputTarget ?? t.workload ?? 0);
                                                    const actual = Number(t.actualOutput ?? 0);
                                                    if (!map[unit]) map[unit] = { target: 0, actual: 0 };
                                                    map[unit].target += target;
                                                    map[unit].actual += actual;
                                                });
                                                const items = Object.entries(map);
                                                if (items.length === 0) {

```
