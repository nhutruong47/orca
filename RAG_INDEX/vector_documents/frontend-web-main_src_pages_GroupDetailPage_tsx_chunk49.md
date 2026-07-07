# Knowledge Document: GroupDetailPage.tsx (Chunk 50/136)

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
  "chunk_index": 49,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
12, color: '#475569' }}>{t.memberName || 'Chưa giao'}</span>
                                                    {t.backupMemberName && <span style={{ marginLeft: 8, fontSize: 11, color: '#9a8a6f' }}>Sao lưu: {t.backupMemberName}</span>}
                                                    {t.memberId && t.memberId !== user?.id && (
                                                        <ion-icon
                                                            name="chatbubble-ellipses"
                                                            onClick={() => { setChatTab('dm'); setDmUserId(t.memberId!); setShowChat(true); }}
                                                            style={{ cursor: 'pointer', color: '#d4a574', marginLeft: 4, fontSize: 16 }}
                                                            title={`Nhắn tin với ${t.memberName}`}
                                                        ></ion-icon>
                                                    )}
                                                </div>
                                            )}
                                        </td>
                                        <td style={{ padding: '12px 16px' }}>
                                            {isAdmin && (
                                                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                                    {editingTaskId === t.id ? (
                                                        <>
                                                            <button onClick={() => handleUpdateTask(t.id)} disabled={loading || !editTaskTitle.trim()} title="Lưu" style={{ background: '#16a34a', border: 'none', borderRadius: 7, color: '#fff', cursor: 'pointer', fontSize: 13, width: 28, height: 28, display: 'grid', placeItems: 'center', opacity: loading || !editTaskTitle.trim() ? 0.55 : 1 }}><ion-icon name="checkmark-outline"></ion-icon></button>
                                                            <button onClick={cancelEditTask} title="Hủy" style={{ background: '#fff', border: '1px solid #e2e8f0', borderRadius: 7, color: '#64748b', cursor: 'pointer', fontSize: 13, width: 28, height: 28, display: 'grid', placeItems: 'center' }}><ion-icon name="close-outline"></ion-icon></button>
                                                        </>

```
