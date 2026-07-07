# Knowledge Document: Layout.tsx (Chunk 6/8)

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
  "chunk_index": 5,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: notification, payment, chat

## Source Code Chunk
```tsx
playNotifications.map(notif => (
                                            <div 
                                                key={notif.id} 
                                                className={`fb-notification-item ${notif.read ? 'read' : 'unread'}`}
                                                onClick={() => {
                                                    if (!notif.read) {
                                                        notificationService.markAsRead(notif.id).then(() => {
                                                            setNotifications(prev => prev.map(n => n.id === notif.id ? { ...n, read: true } : n));
                                                        }).catch(console.error);
                                                    }
                                                    if (notif.taskId) {
                                                        // Example navigation if there's a taskId
                                                        setShowNotifications(false);
                                                    }
                                                }}
                                                style={{cursor: 'pointer'}}
                                            >
                                                <div className="fb-notif-avatar-wrapper">
                                                    <div style={{ width: 48, height: 48, borderRadius: '50%', background: '#3b82f6', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: 18, fontWeight: 700 }}>
                                                        <Bell size={24} color="#fff" />
                                                    </div>
                                                </div>
                                                <div className="fb-notif-content">
                                                    <p>
                                                        <strong>Hệ thống</strong> {notif.message}
                                                    </p>
                                                    <span className="fb-notif-time">{new Date(notif.createdAt).toLocaleDateString('vi-VN')}</span>
                                                </div>

```
