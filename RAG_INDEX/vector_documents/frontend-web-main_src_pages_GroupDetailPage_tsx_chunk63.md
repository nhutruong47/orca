# Knowledge Document: GroupDetailPage.tsx (Chunk 64/136)

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
  "chunk_index": 63,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
le={chatExpanded ? "Ẩn danh sách" : "Xem danh sách thành viên"} onMouseEnter={e => e.currentTarget.style.background = 'var(--bg-input, #f0f2f5)'} onMouseLeave={e => e.currentTarget.style.background = 'transparent'}>
                                <ion-icon name={chatExpanded ? "chevron-forward-outline" : "people-outline"} style={{ fontSize: 22 }}></ion-icon>
                            </button>
                            <button onClick={() => setShowChat(false)} aria-label="Đóng" style={{ width: 36, height: 36, borderRadius: '50%', background: 'var(--bg-input, #e4e6eb)', border: 'none', color: 'var(--text-primary, #050505)', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }} title="Đóng chat"
                                onMouseEnter={e => { e.currentTarget.style.background = 'var(--danger, #f02849)'; e.currentTarget.style.color = '#fff'; }} onMouseLeave={e => { e.currentTarget.style.background = 'var(--bg-input, #e4e6eb)'; e.currentTarget.style.color = 'var(--text-primary, #050505)'; }}>
                                <ion-icon name="close" style={{ fontSize: 22 }}></ion-icon>
                            </button>
                        </div>

                        {/* Messages area */}
                        {(chatTab === 'group' || (chatTab === 'dm' && dmUserId)) ? (
                            <>
                                <div style={{ flex: 1, overflowY: 'auto', padding: '16px 12px', display: 'flex', flexDirection: 'column', gap: 4, background: 'var(--bg-card, #fff)' }}>
                                    {chatMessages.length === 0 && (
                                        <div style={{ textAlign: 'center', color: 'var(--text-secondary, #65676b)', fontSize: 14, padding: '60px 20px', margin: 'auto' }}>
                                            <div style={{ width: 96, height: 96, borderRadius: '50%', background: 'var(--bg-input, #f0f2f5)', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 12px' }}>
                                                <ion-icon name="chatbubbles" style={{ fontSize: 48, color: '#d4a574' }}></ion-icon>
                                            </div>
                                            <div style={{ fontWeight: 700, fontSize: 17, color: 'var(--text-primary, #050505)', marginBottom: 4 }}>Bắt đầu cuộc trò chuyện</div>

```
