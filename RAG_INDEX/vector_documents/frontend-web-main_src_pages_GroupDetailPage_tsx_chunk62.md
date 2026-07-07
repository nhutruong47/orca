# Knowledge Document: GroupDetailPage.tsx (Chunk 63/136)

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
  "chunk_index": 62,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                    <div style={{ fontSize: 12, color: 'var(--text-secondary, #65676b)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{team.members?.length || 0} thành viên</div>
                                    </div>
                                </>
                            )}
                            {/* Nhóm nút hành động bên phải — gọn, kiểu Messenger */}
                            <button onClick={() => alert('Tính năng gọi thoại đang được phát triển')} style={{ width: 36, height: 36, borderRadius: '50%', background: 'transparent', border: 'none', color: '#d4a574', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }} title="Gọi thoại" onMouseEnter={e => e.currentTarget.style.background = 'var(--bg-input, #f0f2f5)'} onMouseLeave={e => e.currentTarget.style.background = 'transparent'}>
                                <ion-icon name="call" style={{ fontSize: 20 }}></ion-icon>
                            </button>
                            <button onClick={() => setShowVideoCall(true)} style={{ width: 36, height: 36, borderRadius: '50%', background: 'transparent', border: 'none', color: '#d4a574', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }} title="Gọi video" onMouseEnter={e => e.currentTarget.style.background = 'var(--bg-input, #f0f2f5)'} onMouseLeave={e => e.currentTarget.style.background = 'transparent'}>
                                <ion-icon name="videocam" style={{ fontSize: 20 }}></ion-icon>
                            </button>

                            <button onClick={() => setChatExpanded(!chatExpanded)} style={{ width: 36, height: 36, borderRadius: '50%', background: 'transparent', border: 'none', color: 'var(--text-secondary, #65676b)', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }} title={chatExpanded ? "Ẩn danh sách" : "Xem danh sách thành viên"} onMouseEnter={e => e.currentTarget.style.background = 'var(--bg-input, #f0f2f5)'} onMouseLeave={e => e.currentTarget.style.background = 'transparent'}>
                                <ion-icon name={chatExpanded ? "chevron-forward-outline" : "people-outline"} style={{ fontSize: 22 }}></ion-icon>
                            </button>

```
