# Knowledge Document: GroupDetailPage.tsx (Chunk 90/136)

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
  "chunk_index": 89,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                                             </svg>
                                                        <div style={{ position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', color: 'var(--text-primary)' }}>
                                                            <span style={{ fontSize: 32, fontWeight: 900 }}>{rate}%</span>
                                                            <span style={{ fontSize: 9, color: 'var(--text-muted)', fontWeight: 700, textTransform: 'uppercase', marginTop: 2 }}>Tỷ lệ đạt</span>
                                                        </div>
                                                    </div>
                                                    <div style={{ flex: 1 }}>
                                                        <h4 style={{ margin: '0 0 6px', fontSize: 16, fontWeight: 700, color: 'var(--text-primary)' }}>Tổng quan công việc</h4>
                                                        <p style={{ margin: 0, fontSize: 13, color: 'var(--text-secondary)', lineHeight: 1.6 }}>
                                                            Tiến độ chung của toàn đội đạt <b>{rate}%</b>. Có <b>{completed}</b> nhiệm vụ đã được xác nhận hoàn thành, <b>{inProgress}</b> nhiệm vụ đang tiến hành, và <b>{pending}</b> nhiệm vụ đang chờ xử lý.
                                                        </p>
                                                    </div>
                                                </div>
                                            );
                                        })()}

                                        {/* Horizontal Task Breakdown Chart */}
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 8, marginTop: 8 }}>
                                            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12, fontWeight: 700, color: 'var(--text-secondary)' }}>
                                                <span>Trạng thái công việc chi tiết</span>
                                                <span>{completed} / {total} hoàn thành</span>
                                            </div>

```
