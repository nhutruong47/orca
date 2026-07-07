# Knowledge Document: GroupDetailPage.tsx (Chunk 10/136)

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
  "chunk_index": 9,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
urrent chat view if we are actively chatting with them
                        if (chatTabRef.current === 'dm' && dmUserIdRef.current === m.userId) {
                            setChatMessages(prev => [...prev, newMsg]);
                        }
                        if (newMsg.senderId !== user.id && !(showChatRef.current && chatTabRef.current === 'dm' && dmUserIdRef.current === m.userId)) {
                            setUnreadDmCounts(prev => ({ ...prev, [m.userId]: (prev[m.userId] || 0) + 1 }));
                        }
                        // Update DM previews
                        setDmPreviews(prev => {
                            const filtered = prev.filter(p => {
                                const contactId = p.senderId === user.id ? p.recipientId : p.senderId;
                                return contactId !== m.userId;
                            });
                            return [newMsg, ...filtered];
                        });
                    });
                });

                // Subscribe to online presence
                client.subscribe('/topic/presence', (message) => {
                    const userIds: string[] = JSON.parse(message.body);
                    setOnlineUsers(userIds);
                });
            },
            onStompError: (frame) => {
                console.error('[STOMP] Error:', frame);
            }
        });

        client.activate();
        stompClientRef.current = client;

        return () => {
            client.deactivate();
            stompClientRef.current = null;
        };
    }, [id, user, team]);

    const handleSendChat = async () => {
        if (!id || (!chatInput.trim() && !chatAttachment)) return;

        let messageContent = chatInput.trim();
        if (chatAttachment) {
            messageContent = messageContent ? `${messageContent} [Đính kèm: ${chatAttachment.name}]` : `[Đính kèm: ${chatAttachment.name}]`;
        }

        await chatService.sendMessage(id, messageContent, chatTab === 'dm' && dmUserId ? dmUserId : undefined);
        setChatInput('');
        setChatAttachment(null);
        loadChatMessages();
    };

    const renderUnreadBadge = (count: number) => count > 0 ? (
        <span style={{
            minWidth: 20,
            height: 20,
            padding: '0 6px',
            borderRadius: 999,
            background: '#ef4444',

```
