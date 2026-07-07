# Knowledge Document: GroupDetailPage.tsx (Chunk 9/136)

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
  "chunk_index": 8,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
      }
        if (showChat && chatTab === 'dm' && dmUserId) {
            setUnreadDmCounts(prev => ({ ...prev, [dmUserId]: 0 }));
        }
    }, [showChat, chatTab, dmUserId]);

    // WebSocket connection
    useEffect(() => {
        if (!id || !user) return;

        // Load initial messages if chat is open
        // if (showChat) loadChatMessages(); // handled by separate useEffect now

        const apiBase = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8080';
        const socketUrl = `${apiBase}/ws`;

        const client = new Client({
            webSocketFactory: () => new SockJS(socketUrl),
            connectHeaders: { userId: user.id },
            reconnectDelay: 5000,
            onConnect: () => {
                console.log('[STOMP] Connected');

                // Subscribe to group messages
                client.subscribe(`/topic/team/${id}`, (message) => {
                    const newMsg: ChatMsg = JSON.parse(message.body);
                    // ONLY append to current chat view if we are actively looking at the group chat
                    // If we are looking at a DM, DO NOT append group messages to the screen
                    if (chatTabRef.current === 'group') {
                        setChatMessages(prev => [...prev, newMsg]);
                    }
                    if (newMsg.senderId !== user.id && !(showChatRef.current && chatTabRef.current === 'group')) {
                        setUnreadGroupCount(prev => prev + 1);
                    }
                });

                // Subscribe to ALL incoming DMs for this user in this team
                team?.members?.filter(m => m.userId !== user.id).forEach(m => {
                    client.subscribe(`/topic/dm/${id}/${user.id}/${m.userId}`, (message) => {
                        const newMsg: ChatMsg = JSON.parse(message.body);

                        // Only append to current chat view if we are actively chatting with them
                        if (chatTabRef.current === 'dm' && dmUserIdRef.current === m.userId) {
                            setChatMessages(prev => [...prev, newMsg]);
                        }
                        if (newMsg.senderId !== user.id && !(showChatRef.current && chatTabRef.current === 'dm' && dmUserIdRef.current === m.userId)) {

```
