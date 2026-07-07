# Knowledge Document: Layout.tsx (Chunk 2/8)

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
  "chunk_index": 1,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: notification, payment, chat

## Source Code Chunk
```tsx
MessageGroups(mapped);
            }).catch(console.error);

            notificationService.getAll().then(setNotifications).catch(console.error);
        }
    }, [user]);

    useEffect(() => {
        function handleClickOutside(event: MouseEvent) {
            if (notifRef.current && !notifRef.current.contains(event.target as Node)) {
                setShowNotifications(false);
            }
            if (msgRef.current && !msgRef.current.contains(event.target as Node)) {
                setShowMessages(false);
            }
        }
        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, []);

    const unreadCount = notifications.filter(n => !n.read).length;
    const displayNotifications = activeTab === 'all' ? notifications : notifications.filter(n => !n.read);
    
    const unreadMsgCount = messageGroups.reduce((acc, curr) => acc + curr.unreadCount, 0);

    return (
        <div className="layout">
            <Sidebar />
            <div className="layout-main">
                {/* Top bar */}
                <header className="topbar">
                    <div className="topbar-left">
                        <h2 className="topbar-greeting">
                            Xin chào, <span className="topbar-username">{user?.fullName || user?.username || 'Người dùng'}</span>
                        </h2>
                    </div>
                    <div className="topbar-right">
                        
                        {/* MESSENGER DROPDOWN */}
                        <div className="topbar-messenger" ref={msgRef}>
                            <button 
                                className="notification-btn" 
                                title="Tin nhắn"
                                onClick={() => {
                                    setShowMessages(!showMessages);
                                    if (!showMessages) setShowNotifications(false);
                                }}
                            >
                                <MessageCircle size={20} />
                                {unreadMsgCount > 0 && <span className="notification-badge">{unreadMsgCount}</span>}
                            </button>

                            {showMessages && (

```
