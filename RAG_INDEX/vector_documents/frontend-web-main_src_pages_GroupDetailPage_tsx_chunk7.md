# Knowledge Document: GroupDetailPage.tsx (Chunk 8/136)

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
  "chunk_index": 7,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
          });
            setMyAttendance(result);
            alert('Vào ca thành công!');
        } catch (e: any) {
            alert(e.response?.data?.error || e.message || 'Lỗi vào ca');
        } finally {
            setLoadingAttendance(false);
        }
    };

    const handleCheckOut = async () => {
        if (!id || !user?.id) return;
        setLoadingAttendance(true);
        try {
            const result = await attendanceService.checkOut(id);
            setMyAttendance(result);
            alert('Tan ca thành công!');
        } catch (e: any) {
            alert(e.response?.data?.error || e.message || 'Lỗi tan ca');
        } finally {
            setLoadingAttendance(false);
        }
    };

    useEffect(() => {
        chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [chatMessages]);

    const loadChatMessages = useCallback(async () => {
        if (!id) return;
        try {
            if (chatTab === 'group') {
                const msgs = await chatService.getGroupMessages(id);
                setChatMessages(msgs);
            } else if (dmUserId) {
                const msgs = await chatService.getDirectMessages(id, dmUserId);
                setChatMessages(msgs);
            }
        } catch (err) {
            console.error('Failed to load messages', err);
        }
    }, [id, chatTab, dmUserId]);

    // Load online users + DM previews
    useEffect(() => {
        if (!id || !user) return;
        chatService.getOnlineUsers().then(setOnlineUsers).catch(() => {});
        chatService.getDmPreviews(id).then(setDmPreviews).catch(() => {});
    }, [id, user]);

    // Automatically load messages when chat is opened or tab/user changes
    useEffect(() => {
        if (showChat) {
            loadChatMessages();
        }
    }, [showChat, chatTab, dmUserId, loadChatMessages]);

    useEffect(() => {
        if (showChat && chatTab === 'group') {
            setUnreadGroupCount(0);
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


```
