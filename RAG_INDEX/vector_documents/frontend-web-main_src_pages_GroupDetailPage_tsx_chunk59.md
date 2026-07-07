# Knowledge Document: GroupDetailPage.tsx (Chunk 60/136)

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
  "chunk_index": 59,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                           return (
                                    <div key={m.userId} onClick={() => { setChatTab('dm'); setDmUserId(m.userId); }} style={{ padding: '10px 12px', display: 'flex', alignItems: 'center', gap: 12, cursor: 'pointer', borderRadius: 8, margin: '2px 8px', background: isActive ? 'rgba(212, 165, 116, 0.15)' : (isUnread ? 'rgba(212, 165, 116, 0.08)' : 'transparent') }}
                                        onMouseEnter={e => { if (!isActive) e.currentTarget.style.background = 'var(--bg-card-hover, #f0f2f5)'; }} onMouseLeave={e => { if (!isActive) e.currentTarget.style.background = isUnread ? 'rgba(212, 165, 116, 0.08)' : 'transparent'; }}>
                                        <div style={{ position: 'relative', flexShrink: 0 }}>
                                            <div style={{ width: 48, height: 48, borderRadius: '50%', background: avatarColor(m.fullName || m.username), display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontWeight: 700, fontSize: 16 }}>{getInitials(m.fullName || m.username)}</div>
                                            {isOnline && <div style={{ position: 'absolute', bottom: 0, right: 0, width: 14, height: 14, borderRadius: '50%', background: '#31a24c', border: '2.5px solid #fff' }} />}
                                        </div>
                                        <div style={{ flex: 1, minWidth: 0 }}>
                                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                                <span style={{ fontWeight: isUnread ? 800 : 600, fontSize: 15, color: 'var(--text-primary, #050505)' }}>{m.fullName || m.username}</span>
                                                <span style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                                    <span style={{ fontSize: 11, color: isUnread ? '#d4a574' : 'var(--text-secondary, #65676b)', fontWeight: isUnread ? 700 : 500 }}>{timeLabel}</span>
                                                    {renderUnreadBadge(unreadCount)}
                                                </span>
                                            </div>

```
