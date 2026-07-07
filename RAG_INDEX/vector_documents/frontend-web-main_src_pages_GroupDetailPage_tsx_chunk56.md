# Knowledge Document: GroupDetailPage.tsx (Chunk 57/136)

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
  "chunk_index": 56,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
f2f5)', borderRadius: 20, padding: '8px 12px' }}>
                                <ion-icon name="search-outline" style={{ color: 'var(--text-secondary, #65676b)', fontSize: 16 }}></ion-icon>
                                <input placeholder="Tìm kiếm nhân viên" style={{ flex: 1, background: 'transparent', border: 'none', outline: 'none', fontSize: 14, color: 'var(--text-primary, #050505)' }} />
                            </div>
                        </div>

                        {/* Tab pills: Nhóm / Cá nhân */}
                        <div style={{ display: 'flex', padding: '4px 12px 8px', gap: 6, flexShrink: 0 }}>
                            <button onClick={() => { setChatTab('group'); setDmUserId(null); }} style={{ flex: 1, padding: '8px 12px', borderRadius: 18, border: 'none', cursor: 'pointer', background: chatTab === 'group' ? '#d4a574' : 'var(--bg-input, #e4e6eb)', color: chatTab === 'group' ? '#fff' : 'var(--text-primary, #050505)', fontSize: 13, fontWeight: 700, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6 }}>
                                <ion-icon name="people" style={{ fontSize: 14 }}></ion-icon> Nhóm {chatTab === 'group' && renderUnreadBadge(unreadGroupCount)}
                            </button>
                            <button onClick={() => setChatTab('dm')} style={{ flex: 1, padding: '8px 12px', borderRadius: 18, border: 'none', cursor: 'pointer', background: chatTab === 'dm' ? '#d4a574' : 'var(--bg-input, #e4e6eb)', color: chatTab === 'dm' ? '#fff' : 'var(--text-primary, #050505)', fontSize: 13, fontWeight: 700, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6 }}>
                                <ion-icon name="person" style={{ fontSize: 14 }}></ion-icon> Cá nhân {chatTab === 'dm' && renderUnreadBadge(unreadDmTotal)}
                            </button>
                        </div>

                        {/* Conversation list */}
                        <div style={{ flex: 1, overflowY: 'auto' }}>
                            {/* Group chat row (always first when on group tab) */}
                            {chatTab === 'group' && (

```
