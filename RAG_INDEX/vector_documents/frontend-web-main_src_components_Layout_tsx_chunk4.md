# Knowledge Document: Layout.tsx (Chunk 5/8)

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
  "chunk_index": 4,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: notification, payment, chat

## Source Code Chunk
```tsx
         )}
                        </div>

                        {/* NOTIFICATION DROPDOWN */}
                        <div className="topbar-notification" ref={notifRef}>
                            <button 
                                className="notification-btn"
                                onClick={() => {
                                    setShowNotifications(!showNotifications);
                                    if (!showNotifications) setShowMessages(false);
                                }}
                            >
                                <Bell size={20} />
                                {unreadCount > 0 && <span className="notification-badge">{unreadCount}</span>}
                            </button>
                            
                            {showNotifications && (
                                <div className="fb-notification-dropdown">
                                    <div className="fb-notification-header">
                                        <h3>Thông báo</h3>
                                        <button className="fb-notification-options"><MoreHorizontal size={20}/></button>
                                    </div>
                                    <div className="fb-notification-tabs">
                                        <button className={activeTab === 'all' ? 'active' : ''} onClick={() => setActiveTab('all')}>Tất cả</button>
                                        <button className={activeTab === 'unread' ? 'active' : ''} onClick={() => setActiveTab('unread')}>Chưa đọc</button>
                                    </div>
                                    <div className="fb-notification-section">
                                        <span>Gần đây</span>
                                        <button>Xem tất cả</button>
                                    </div>
                                    <div className="fb-notification-list">
                                        {displayNotifications.map(notif => (
                                            <div 
                                                key={notif.id} 
                                                className={`fb-notification-item ${notif.read ? 'read' : 'unread'}`}
                                                onClick={() => {
                                                    if (!notif.read) {

```
