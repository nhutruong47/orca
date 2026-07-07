# Knowledge Document: GroupDetailPage.tsx (Chunk 131/136)

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
  "chunk_index": 130,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
8)}...</div>
                                                </div>
                                            </div>

                                            <div style={{ textAlign: 'center' }}>
                                                <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--text-primary)' }}>{s.totalTasks}</div>
                                            </div>

                                            <div style={{ textAlign: 'center' }}>
                                                <div style={{
                                                    display: 'inline-flex', alignItems: 'center', gap: 4,
                                                    padding: '4px 10px', borderRadius: 20,
                                                    background: completionRate >= 80 ? 'rgba(16, 185, 129, 0.1)' : completionRate >= 50 ? 'rgba(245, 158, 11, 0.1)' : 'rgba(239, 68, 68, 0.1)',
                                                    color: completionRate >= 80 ? '#10b981' : completionRate >= 50 ? '#f59e0b' : '#ef4444'
                                                }}>
                                                    <span style={{ fontSize: 13, fontWeight: 700 }}>{s.completedTasks}</span>
                                                </div>
                                                <div style={{ fontSize: 10, color: '#94a3b8', marginTop: 2 }}>{completionRate}%</div>
                                            </div>

                                            {/* Workload */}
                                            <div style={{ textAlign: 'center' }}>
                                                <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-primary)' }}>
                                                    {(s.regularHours && s.regularHours > 0) ? s.regularHours.toFixed(1) : s.totalWorkload.toFixed(1)}h
                                                </div>
                                                {(s.overtimeHours && s.overtimeHours > 0) ? (
                                                    <div style={{ fontSize: 11, color: '#f59e0b', fontWeight: 700 }}>+ {s.overtimeHours.toFixed(1)}h TC</div>
                                                ) : <div style={{ fontSize: 10, color: '#94a3b8' }}>giờ thường</div>}
                                            </div>


```
