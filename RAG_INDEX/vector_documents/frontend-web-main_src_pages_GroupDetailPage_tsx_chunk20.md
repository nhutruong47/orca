# Knowledge Document: GroupDetailPage.tsx (Chunk 21/136)

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
  "chunk_index": 20,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
  style={{ background: '#e0e7ff', border: '1px solid #c7d2fe', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 700, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: '#4338ca' }}
                        >
                            <ion-icon name="people-circle-outline"></ion-icon> Quản lý chấm công
                        </button>
                    )}

                    <button onClick={() => setShowScheduleModal(true)} style={{ background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: 'var(--text-secondary)' }} id="btn-schedule-modal"><ion-icon name="calendar-outline"></ion-icon> Lịch sản xuất</button>
                    <button onClick={() => setShowChat(!showChat)} style={{ position: 'relative', background: unreadTotal > 0 ? '#fff7ed' : 'var(--bg-input)', border: unreadTotal > 0 ? '1px solid #fed7aa' : '1px solid var(--border)', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: 'var(--accent-primary)' }}><ion-icon name={unreadTotal > 0 ? 'chatbubbles' : 'chatbubbles-outline'}></ion-icon> Nhắn tin {renderUnreadBadge(unreadTotal)}</button>
                    {isAdmin && <button onClick={() => setShowMemberRoles(!showMemberRoles)} style={{ background: showMemberRoles ? '#fff7ed' : 'var(--bg-input)', border: showMemberRoles ? '1px solid #fed7aa' : '1px solid var(--border)', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: showMemberRoles ? '#d97706' : 'var(--text-secondary)' }}><ion-icon name="id-card-outline"></ion-icon> Phân vai trò</button>}

                    {isAdmin && <button onClick={() => setShowAddMember(true)} style={{ background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: 'var(--text-secondary)' }}><ion-icon name="people-outline"></ion-icon> Mời</button>}

```
