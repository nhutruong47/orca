# Knowledge Document: GroupDetailPage.tsx (Chunk 58/136)

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
  "chunk_index": 57,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
ion-icon> Cá nhân {chatTab === 'dm' && renderUnreadBadge(unreadDmTotal)}
                            </button>
                        </div>

                        {/* Conversation list */}
                        <div style={{ flex: 1, overflowY: 'auto' }}>
                            {/* Group chat row (always first when on group tab) */}
                            {chatTab === 'group' && (
                                <div onClick={() => { setChatTab('group'); setDmUserId(null); }} style={{ padding: '10px 12px', display: 'flex', alignItems: 'center', gap: 12, cursor: 'pointer', borderRadius: 8, margin: '2px 8px', background: chatTab === 'group' && !dmUserId ? 'rgba(212, 165, 116, 0.15)' : 'transparent' }}
                                    onMouseEnter={e => { if (!(chatTab === 'group' && !dmUserId)) e.currentTarget.style.background = 'var(--bg-card-hover, #f0f2f5)'; }} onMouseLeave={e => { if (!(chatTab === 'group' && !dmUserId)) e.currentTarget.style.background = 'transparent'; }}>
                                    <div style={{ position: 'relative', flexShrink: 0 }}>
                                        <div style={{ width: 48, height: 48, borderRadius: '50%', background: '#d4a574', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff' }}>
                                            <ion-icon name="people" style={{ fontSize: 24 }}></ion-icon>
                                        </div>
                                    </div>
                                    <div style={{ flex: 1, minWidth: 0 }}>
                                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                            <span style={{ fontWeight: 700, fontSize: 15, color: 'var(--text-primary, #050505)' }}>Nhóm chung</span>
                                            {renderUnreadBadge(unreadGroupCount)}
                                        </div>
                                        <div style={{ fontSize: 13, color: 'var(--text-secondary, #65676b)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                                            {team.members?.length || 0} thành viên • Trò chuyện nhóm
                                        </div>
                                    </div>
                                </div>

```
