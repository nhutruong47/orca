# Knowledge Document: GroupDetailPage.tsx (Chunk 94/136)

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
  "chunk_index": 93,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
20, background: 'var(--bg-input, #0f172a)', borderRadius: 10, overflow: 'hidden', position: 'relative', display: 'flex', alignItems: 'center' }}>
                                                                <div style={{ height: '100%', background: 'linear-gradient(90deg, #d4a574 0%, #f59e0b 100%)', width: `${pct}%`, borderRadius: 10, transition: 'width 0.6s cubic-bezier(0.4, 0, 0.2, 1)' }} />
                                                                <span style={{ position: 'absolute', right: 10, fontSize: 11, fontWeight: 800, color: pct > 80 ? '#fff' : 'var(--text-secondary)' }}>{pct}%</span>
                                                            </div>
                                                        </div>
                                                    );
                                                });
                                            })()}
                                        </div>
                                    </div>
                                </div>

                                {/* Bottom Grid: Employee Performance & Stage Breakdown */}
                                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(480px, 1fr))', gap: 24 }}>

                                    {/* Left: Employee Productivity Ranking */}
                                    <div style={{ background: 'var(--bg-secondary, #1e293b)', padding: '24px', borderRadius: 18, border: '1px solid var(--border, #334155)' }}>
                                        <h3 style={{ fontSize: 16, fontWeight: 700, margin: '0 0 18px 0', color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: 8 }}>
                                            <ion-icon name="people-outline" style={{ color: '#d4a574' }}></ion-icon>
                                            Xếp hạng hiệu suất nhân sự
                                        </h3>
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 14, maxHeight: 280, overflowY: 'auto', paddingRight: 4 }}>
                                            {(() => {
                                                const map: Record<string, { total: number; completed: number; name: string }> = {};
                                                latestGoalTasks.forEach(t => {

```
