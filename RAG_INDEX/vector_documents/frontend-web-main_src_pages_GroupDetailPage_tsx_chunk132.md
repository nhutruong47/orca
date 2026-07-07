# Knowledge Document: GroupDetailPage.tsx (Chunk 133/136)

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
  "chunk_index": 132,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                                             ) : (
                                                    <div
                                                        onClick={() => handleRateEdit(s.memberId, s.hourlyRate)}
                                                        style={{
                                                            display: 'inline-flex', alignItems: 'center', gap: 4,
                                                            padding: '4px 10px', borderRadius: 8,
                                                            background: hourlyRateOverride[s.memberId] ? 'rgba(212,165,116,0.1)' : 'var(--bg-input, rgba(255,255,255,0.05))',
                                                            color: hourlyRateOverride[s.memberId] ? '#d4a574' : '#64748b', cursor: 'pointer', fontSize: 13, fontWeight: 600,
                                                            border: hourlyRateOverride[s.memberId] ? '1px dashed #d4a574' : '1px dashed var(--border)'
                                                        }}
                                                        title="Nhấp để chỉnh sửa đơn giá"
                                                    >
                                                        {getEffectiveRate(s.memberId, s.hourlyRate).toLocaleString('vi-VN')}
                                                        <span style={{ fontSize: 10 }}>đ</span>
                                                        <svg width="12" height="12" fill="none" stroke="currentColor" strokeWidth="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                                                    </div>
                                                )}
                                            </div>

                                            {/* Salary */}
                                            <div style={{ textAlign: 'left' }}>
                                                <div style={{ color: '#d4a574', fontWeight: 800, fontSize: 15 }}>
                                                    {salary.toLocaleString('vi-VN')} đ
                                                </div>
                                            </div>
                                        </div>
                                    );

```
