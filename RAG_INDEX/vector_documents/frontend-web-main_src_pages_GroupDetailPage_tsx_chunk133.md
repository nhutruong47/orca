# Knowledge Document: GroupDetailPage.tsx (Chunk 134/136)

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
  "chunk_index": 133,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
t' }}>
                                                <div style={{ color: '#d4a574', fontWeight: 800, fontSize: 15 }}>
                                                    {salary.toLocaleString('vi-VN')} đ
                                                </div>
                                            </div>
                                        </div>
                                    );
                                })}

                                {/* Total Row */}
                                <div style={{
                                    display: 'grid',
                                    gridTemplateColumns: '2fr 1fr 1fr 1fr 1.2fr 1.3fr',
                                    gap: 12, padding: '18px 16px',
                                    background: 'var(--bg-input, rgba(255, 255, 255, 0.03))',
                                    borderTop: '1px solid var(--border)',
                                    borderRadius: '0 0 16px 16px',
                                    alignItems: 'center'
                                }}>
                                    <div style={{ fontSize: 15, fontWeight: 800, color: 'var(--text-primary)' }}>Tổng cộng</div>
                                    <div style={{ textAlign: 'center', color: 'var(--text-primary)' }}><span style={{ fontSize: 16, fontWeight: 800 }}>{totalTasks}</span></div>
                                    <div style={{ textAlign: 'center', color: '#10b981' }}><span style={{ fontSize: 16, fontWeight: 800 }}>{totalCompleted}</span></div>
                                    <div style={{ textAlign: 'center', color: 'var(--text-primary)' }}><span style={{ fontSize: 16, fontWeight: 800 }}>{totalWorkload.toFixed(1)}h</span></div>
                                    <div style={{ textAlign: 'center', color: '#94a3b8', fontSize: 12 }}>—</div>
                                    <div style={{ textAlign: 'left' }}>
                                        <div style={{
                                            color: '#d4a574', fontWeight: 900, fontSize: 17
                                        }}>
                                            {totalSalary.toLocaleString('vi-VN')} đ
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}


```
