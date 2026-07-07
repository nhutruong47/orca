# Knowledge Document: GroupDetailPage.tsx (Chunk 65/136)

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
  "chunk_index": 64,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
nt: 'center', margin: '0 auto 12px' }}>
                                                <ion-icon name="chatbubbles" style={{ fontSize: 48, color: '#d4a574' }}></ion-icon>
                                            </div>
                                            <div style={{ fontWeight: 700, fontSize: 17, color: 'var(--text-primary, #050505)', marginBottom: 4 }}>Bắt đầu cuộc trò chuyện</div>
                                            <div>Gửi tin nhắn cho {chatTab === 'dm' ? 'bạn bè' : 'nhóm'} của bạn</div>
                                        </div>
                                    )}
                                    {chatMessages.map((msg, idx) => {
                                        const isMe = msg.senderId === user?.id;
                                        const prev = idx > 0 ? chatMessages[idx - 1] : null;
                                        const isFirstOfGroup = !prev || prev.senderId !== msg.senderId;
                                        return (
                                            <div key={msg.id} style={{ display: 'flex', flexDirection: isMe ? 'row-reverse' : 'row', gap: 8, alignItems: 'flex-end', marginTop: isFirstOfGroup ? 12 : 2, marginBottom: 2 }}>
                                                {!isMe ? (
                                                    <div style={{ width: 28, height: 28, borderRadius: '50%', background: avatarColor(msg.senderName), display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontWeight: 700, fontSize: 11, flexShrink: 0, visibility: isFirstOfGroup ? 'visible' : 'hidden' }}>
                                                        {getInitials(msg.senderName)}
                                                    </div>
                                                ) : (
                                                    <div style={{ width: 28, flexShrink: 0 }} />
                                                )}
                                                <div style={{ maxWidth: '65%', display: 'flex', flexDirection: 'column', alignItems: isMe ? 'flex-end' : 'flex-start' }}>
                                                    {isFirstOfGroup && !isMe && chatTab === 'group' && (

```
