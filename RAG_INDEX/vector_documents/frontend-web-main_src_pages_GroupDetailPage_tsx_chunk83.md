# Knowledge Document: GroupDetailPage.tsx (Chunk 84/136)

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
  "chunk_index": 83,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
'Đang lưu...' : 'Lưu vào kho'}
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* Chat History Modal */}
            {showChatHistory && (
                <div className="modal-overlay" onClick={() => setShowChatHistory(false)} style={{ background: 'rgba(0,0,0,0.6)', backdropFilter: 'blur(8px)' }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 640, padding: 0, borderRadius: 20, overflow: 'hidden', height: '80vh', display: 'flex', flexDirection: 'column', background: '#fff' }}>
                        <div style={{ padding: '20px 24px', borderBottom: '1px solid #e2e8f0', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                            <div><h3 style={{ margin: 0, fontSize: 18, fontWeight: 700, color: '#1e293b' }}>Lịch sử Chat AI</h3><p style={{ margin: '2px 0 0', fontSize: 13, color: '#64748b' }}>Mục tiêu: {activeGoalTitle}</p></div>
                            <button onClick={() => setShowChatHistory(false)} style={{ background: '#f1f5f9', border: 'none', width: 32, height: 32, borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', cursor: 'pointer', color: '#64748b' }}><ion-icon name="close" style={{ fontSize: 20 }}></ion-icon></button>
                        </div>
                        <div style={{ flex: 1, overflowY: 'auto', padding: 24, background: '#f8fafc', display: 'flex', flexDirection: 'column', gap: 16 }}>
                            {activeChatLog.map((msg, i) => (
                                <div key={i} style={{ display: 'flex', flexDirection: 'column', alignItems: msg.role === 'user' ? 'flex-end' : 'flex-start' }}>
                                    <div style={{ maxWidth: '85%', padding: '12px 16px', borderRadius: msg.role === 'user' ? '14px 14px 0 14px' : '14px 14px 14px 0', background: msg.role === 'user' ? '#d4a574' : '#fff', color: msg.role === 'user' ? '#fff' : '#1e293b', boxShadow: '0 1px 3px rgba(0,0,0,0.05)', fontSize: 14, lineHeight: 1.5, border: msg.role === 'assistant' ? '1px solid #e2e8f0' : 'none' }}>{msg.content}</div>

```
