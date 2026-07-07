# Knowledge Document: GroupDetailPage.tsx (Chunk 59/136)

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
  "chunk_index": 58,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                              <div style={{ fontSize: 13, color: 'var(--text-secondary, #65676b)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                                            {team.members?.length || 0} thành viên • Trò chuyện nhóm
                                        </div>
                                    </div>
                                </div>
                            )}

                            {/* DM rows */}
                            {(chatTab === 'dm' || chatTab === 'group') && (team.members?.filter(m => m.userId !== user?.id) || []).map(m => {
                                const isOnline = onlineUsers.includes(m.userId);
                                const preview = dmPreviews.find(p => p.senderId === m.userId || p.recipientId === m.userId);
                                const unreadCount = unreadDmCounts[m.userId] || 0;
                                const previewText = preview ? (preview.content.length > 35 ? preview.content.substring(0, 35) + '…' : preview.content) : 'Bắt đầu trò chuyện';
                                const previewTime = preview ? new Date(preview.createdAt) : null;
                                const timeLabel = previewTime ? (() => {
                                    const diff = Date.now() - previewTime.getTime();
                                    if (diff < 60000) return 'Vừa xong';
                                    if (diff < 3600000) return `${Math.floor(diff / 60000)} ph`;
                                    if (diff < 86400000) return `${Math.floor(diff / 3600000)} giờ`;
                                    return previewTime.toLocaleDateString('vi-VN');
                                })() : '';
                                const isActive = chatTab === 'dm' && dmUserId === m.userId;
                                const isUnread = unreadCount > 0;
                                return (
                                    <div key={m.userId} onClick={() => { setChatTab('dm'); setDmUserId(m.userId); }} style={{ padding: '10px 12px', display: 'flex', alignItems: 'center', gap: 12, cursor: 'pointer', borderRadius: 8, margin: '2px 8px', background: isActive ? 'rgba(212, 165, 116, 0.15)' : (isUnread ? 'rgba(212, 165, 116, 0.08)' : 'transparent') }}

```
