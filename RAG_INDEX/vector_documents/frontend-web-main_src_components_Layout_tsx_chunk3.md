# Knowledge Document: Layout.tsx (Chunk 4/8)

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
  "chunk_index": 3,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: notification, payment, chat

## Source Code Chunk
```tsx
-notif-avatar" />
                                                    {group.isActive && <div className="online-indicator"></div>}
                                                </div>
                                                <div className="fb-notif-content">
                                                    <p className={`msg-group-name ${group.unreadCount > 0 ? 'unread-text' : ''}`}>
                                                        {group.name}
                                                    </p>
                                                    <div className="msg-preview">
                                                        <span className={`msg-preview-text ${group.unreadCount > 0 ? 'unread-text' : ''}`}>
                                                            {group.lastMessage}
                                                        </span>
                                                        <span className="msg-preview-time"> · {group.time}</span>
                                                    </div>
                                                </div>
                                                {group.unreadCount > 0 && (
                                                    <div className="msg-unread-badge-icon">
                                                        {group.unreadCount}
                                                    </div>
                                                )}
                                            </div>
                                        ))}
                                    </div>
                                    <div className="fb-notification-footer">
                                        <button onClick={() => { setShowMessages(false); navigate('/groups'); }}>Xem tất cả trong Messenger</button>
                                    </div>
                                </div>
                            )}
                        </div>

                        {/* NOTIFICATION DROPDOWN */}
                        <div className="topbar-notification" ref={notifRef}>
                            <button 
                                className="notification-btn"
                                onClick={() => {
                                    setShowNotifications(!showNotifications);

```
