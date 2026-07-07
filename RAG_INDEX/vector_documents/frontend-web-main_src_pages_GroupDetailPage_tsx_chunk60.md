# Knowledge Document: GroupDetailPage.tsx (Chunk 61/136)

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
  "chunk_index": 60,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
: 6 }}>
                                                    <span style={{ fontSize: 11, color: isUnread ? '#d4a574' : 'var(--text-secondary, #65676b)', fontWeight: isUnread ? 700 : 500 }}>{timeLabel}</span>
                                                    {renderUnreadBadge(unreadCount)}
                                                </span>
                                            </div>
                                            <div style={{ fontSize: 13, color: isUnread ? 'var(--text-primary, #050505)' : 'var(--text-secondary, #65676b)', fontWeight: isUnread ? 600 : 400, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                                                {previewText}
                                            </div>
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>

                    {/* ===== RIGHT: chat conversation ===== */}
                    <div style={{ flex: 1, display: 'flex', flexDirection: 'column', minWidth: 0, background: 'var(--bg-card, #fff)' }}>
                        {/* Conversation header (Messenger style) — có nút đóng tắt (X) + mở rộng/thu nhỏ */}
                        <div style={{ flexShrink: 0, padding: '10px 12px', borderBottom: '1px solid var(--border, #e4e6eb)', display: 'flex', alignItems: 'center', gap: 10, background: 'var(--bg-card, #fff)' }}>
                            {chatTab === 'dm' && dmUserId ? (() => {
                                const m = team.members?.find(mem => mem.userId === dmUserId);
                                const isOnline = m ? onlineUsers.includes(m.userId) : false;
                                return (
                                    <>
                                        <div style={{ position: 'relative', flexShrink: 0 }}>
                                            <div style={{ width: 40, height: 40, borderRadius: '50%', background: avatarColor(m?.fullName || m?.username || '?'), display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontWeight: 700, fontSize: 15 }}>{getInitials(m?.fullName || m?.username || '?')}</div>

```
