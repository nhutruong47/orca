# Knowledge Document: GroupDetailPage.tsx (Chunk 62/136)

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
  "chunk_index": 61,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                <div style={{ position: 'relative', flexShrink: 0 }}>
                                            <div style={{ width: 40, height: 40, borderRadius: '50%', background: avatarColor(m?.fullName || m?.username || '?'), display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontWeight: 700, fontSize: 15 }}>{getInitials(m?.fullName || m?.username || '?')}</div>
                                            {isOnline && <div style={{ position: 'absolute', bottom: 0, right: 0, width: 12, height: 12, borderRadius: '50%', background: '#31a24c', border: '2.5px solid #fff' }} />}
                                        </div>
                                        <div style={{ flex: 1, minWidth: 0 }}>
                                            <div style={{ fontWeight: 700, fontSize: 15, color: 'var(--text-primary, #050505)' }}>{m?.fullName || m?.username}</div>
                                            <div style={{ fontSize: 12, color: isOnline ? '#31a24c' : 'var(--text-secondary, #65676b)' }}>{isOnline ? 'Đang hoạt động' : 'Ngoại tuyến'}</div>
                                        </div>
                                    </>
                                );
                            })() : (
                                <>
                                    <div style={{ width: 40, height: 40, borderRadius: '50%', background: '#d4a574', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', flexShrink: 0 }}>
                                        <ion-icon name="people" style={{ fontSize: 22 }}></ion-icon>
                                    </div>
                                    <div style={{ flex: 1, minWidth: 0 }}>
                                        <div style={{ fontWeight: 700, fontSize: 15, color: 'var(--text-primary, #050505)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>Nhóm chung</div>
                                        <div style={{ fontSize: 12, color: 'var(--text-secondary, #65676b)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{team.members?.length || 0} thành viên</div>
                                    </div>
                                </>
                            )}
                            {/* Nhóm nút hành động bên phải — gọn, kiểu Messenger */}

```
