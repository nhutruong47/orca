# Knowledge Document: GroupDetailPage.tsx (Chunk 112/136)

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
  "chunk_index": 111,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
etween', alignItems: 'flex-start', gap: 8 }}>
                                                                        <span style={{ fontSize: 13, fontWeight: 700, color: '#ffffff' }}>{t.title}</span>
                                                                        <span style={{ fontSize: 10, fontWeight: 800, padding: '2px 6px', borderRadius: 6, background: '#1c1c1e', color: pillColor }}>
                                                                            {STATUS_COLORS[t.status]?.label || t.status}
                                                                        </span>
                                                                    </div>
                                                                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 11, color: '#8e8e93' }}>
                                                                        <span>Giai đoạn: {t.productionStage || '—'}</span>
                                                                        <span>Phụ trách: {t.memberName || 'Chưa giao'}</span>
                                                                    </div>
                                                                </div>
                                                            );
                                                        })}
                                                    </div>
                                                )}
                                            </div>
                                        </div>

                                        {/* Highlight Panel: In progress & Deadlines list */}
                                        <div style={{ background: '#1c1c1e', padding: '20px', borderRadius: 16, border: '1px solid #2d2d34', display: 'flex', flexDirection: 'column', gap: 20 }}>
                                            <h3 style={{ margin: 0, fontSize: 15, fontWeight: 700, color: '#ffffff', display: 'flex', alignItems: 'center', gap: 8 }}>
                                                <span style={{ width: 8, height: 8, borderRadius: '50%', background: '#f59e0b', display: 'inline-block' }}></span>
                                                Công việc Đang làm & Hạn chót
                                            </h3>


```
