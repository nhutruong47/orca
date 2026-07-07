# Knowledge Document: GroupDetailPage.tsx (Chunk 109/136)

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
  "chunk_index": 108,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                           <div style={{ display: 'flex', gap: 16, fontSize: 12, fontWeight: 500, color: '#8e8e93', borderTop: '1px solid #232328', paddingTop: 16, flexWrap: 'wrap' }}>
                                             <span style={{ display: 'flex', alignItems: 'center', gap: 6 }}><span style={{ width: 8, height: 8, borderRadius: '50%', background: '#f59e0b' }}></span> Đang làm</span>
                                             <span style={{ display: 'flex', alignItems: 'center', gap: 6 }}><span style={{ width: 8, height: 8, borderRadius: '50%', background: '#ef4444' }}></span> Quá hạn</span>
                                             <span style={{ display: 'flex', alignItems: 'center', gap: 6 }}><span style={{ width: 8, height: 8, borderRadius: '50%', background: '#10b981' }}></span> Hoàn thành</span>
                                             <span style={{ display: 'flex', alignItems: 'center', gap: 6 }}><span style={{ width: 8, height: 8, borderRadius: '50%', background: '#8e8e93' }}></span> Chờ xử lý</span>
                                        </div>
                                    </div>

                                    {/* Right Side: Selected Day Details & Deadlines List */}
                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 20 }}>
                                        {/* Selected Day Details Card */}
                                        <div style={{ background: '#1c1c1e', padding: '20px', borderRadius: 16, border: '1px solid #2d2d34', display: 'flex', flexDirection: 'column', gap: 20 }}>
                                            <h3 style={{ margin: 0, fontSize: 16, fontWeight: 700, color: '#ffffff', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                                <span>Ngày {selectedCalendarDay}/{month + 1}</span>
                                                <span style={{ fontSize: 12, fontWeight: 500, color: '#8e8e93', background: '#2c2c2e', padding: '3px 10px', borderRadius: 12 }}>{selectedTasks.length} công việc</span>
                                            </h3>


```
