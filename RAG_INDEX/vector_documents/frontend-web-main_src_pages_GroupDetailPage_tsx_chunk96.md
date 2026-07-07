# Knowledge Document: GroupDetailPage.tsx (Chunk 97/136)

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
  "chunk_index": 96,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                                                      <span style={{ color: pct === 100 ? '#10b981' : '#d4a574' }}>{m.completed}/{m.total} task ({pct}%)</span>
                                                                </div>
                                                                <div style={{ height: 6, background: 'var(--bg-input, #0f172a)', borderRadius: 3, overflow: 'hidden' }}>
                                                                    <div style={{ height: '100%', background: pct === 100 ? '#10b981' : 'linear-gradient(90deg, #d4a574 0%, #f59e0b 100%)', width: `${pct}%`, borderRadius: 3, transition: 'width 0.5s ease' }} />
                                                                </div>
                                                            </div>
                                                        </div>
                                                    );
                                                });
                                            })()}
                                        </div>
                                    </div>

                                    {/* Right: Production Stage Distribution Chart */}
                                    <div style={{ background: 'var(--bg-secondary, #1e293b)', padding: '24px', borderRadius: 18, border: '1px solid var(--border, #334155)', display: 'flex', flexDirection: 'column' }}>
                                        <h3 style={{ fontSize: 16, fontWeight: 700, margin: '0 0 18px 0', color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: 8 }}>
                                            <ion-icon name="git-network-outline" style={{ color: '#d4a574' }}></ion-icon>
                                            Phân bổ theo giai đoạn sản xuất
                                        </h3>
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 12, maxHeight: 280, overflowY: 'auto', paddingRight: 4 }}>
                                            {(() => {
                                                const map: Record<string, number> = {};
                                                let maxCount = 0;
                                                latestGoalTasks.forEach(t => {
                                                    const stage = t.productionStage || 'Chưa phân loại';

```
