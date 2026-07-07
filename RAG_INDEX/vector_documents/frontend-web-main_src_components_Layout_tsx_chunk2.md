# Knowledge Document: Layout.tsx (Chunk 3/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/Layout.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "notification",
  "tags": [
    "notification",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 2,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: notification, payment, chat

## Source Code Chunk
```tsx
                        if (!showMessages) setShowNotifications(false);
                                }}
                            >
                                <MessageCircle size={20} />
                                {unreadMsgCount > 0 && <span className="notification-badge">{unreadMsgCount}</span>}
                            </button>

                            {showMessages && (
                                <div className="fb-notification-dropdown msg-dropdown">
                                    <div className="fb-notification-header">
                                        <h3>Đoạn chat</h3>
                                        <div style={{display: 'flex', gap: '8px'}}>
                                            <button className="fb-notification-options"><MoreHorizontal size={20}/></button>
                                            <button className="fb-notification-options"><Edit size={18}/></button>
                                        </div>
                                    </div>
                                    <div className="fb-notification-list">
                                        {messageGroups.map(group => (
                                            <div 
                                                key={group.id} 
                                                className="fb-notification-item msg-item"
                                                onClick={() => {
                                                    setShowMessages(false);
                                                    navigate(`/groups/${group.id}?openChat=1`);
                                                }}
                                                style={{cursor: 'pointer'}}
                                            >
                                                <div className="fb-notif-avatar-wrapper">
                                                    <img src={group.avatar} alt="avatar" className="fb-notif-avatar" />
                                                    {group.isActive && <div className="online-indicator"></div>}
                                                </div>
                                                <div className="fb-notif-content">
                                                    <p className={`msg-group-name ${group.unreadCount > 0 ? 'unread-text' : ''}`}>

```
