# Knowledge Document: GroupDetailPage.tsx (Chunk 91/136)

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
  "chunk_index": 90,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12, fontWeight: 700, color: 'var(--text-secondary)' }}>
                                                <span>Trạng thái công việc chi tiết</span>
                                                <span>{completed} / {total} hoàn thành</span>
                                            </div>
                                            <div style={{ height: 16, background: 'var(--border, #334155)', borderRadius: 8, overflow: 'hidden', display: 'flex' }}>
                                                <div style={{ width: `${total > 0 ? (completed / total) * 100 : 0}%`, background: '#10b981', transition: 'width 0.4s' }} title={`Hoàn thành: ${completed}`} />
                                                <div style={{ width: `${total > 0 ? (inProgress / total) * 100 : 0}%`, background: '#3b82f6', transition: 'width 0.4s' }} title={`Đang làm: ${inProgress}`} />
                                                <div style={{ width: `${total > 0 ? (pending / total) * 100 : 0}%`, background: '#94a3b8', transition: 'width 0.4s' }} title={`Chờ xử lý: ${pending}`} />
                                            </div>
                                            <div style={{ display: 'flex', gap: 16, fontSize: 11, fontWeight: 600, color: 'var(--text-secondary)', marginTop: 4 }}>
                                                <span style={{ display: 'flex', alignItems: 'center', gap: 5 }}><span style={{ width: 8, height: 8, borderRadius: '50%', background: '#10b981' }}></span> Hoàn thành ({completed})</span>
                                                <span style={{ display: 'flex', alignItems: 'center', gap: 5 }}><span style={{ width: 8, height: 8, borderRadius: '50%', background: '#3b82f6' }}></span> Đang làm ({inProgress})</span>
                                                <span style={{ display: 'flex', alignItems: 'center', gap: 5 }}><span style={{ width: 8, height: 8, borderRadius: '50%', background: '#94a3b8' }}></span> Chờ xử lý ({pending})</span>
                                            </div>
                                        </div>
                                    </div>

                                    {/* Right Column: Yield Target vs. Actual (Real CSS/SVG Bar Charts) */}

```
