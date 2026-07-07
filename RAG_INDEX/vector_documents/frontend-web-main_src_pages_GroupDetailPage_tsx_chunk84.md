# Knowledge Document: GroupDetailPage.tsx (Chunk 85/136)

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
  "chunk_index": 84,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
        <div style={{ maxWidth: '85%', padding: '12px 16px', borderRadius: msg.role === 'user' ? '14px 14px 0 14px' : '14px 14px 14px 0', background: msg.role === 'user' ? '#d4a574' : '#fff', color: msg.role === 'user' ? '#fff' : '#1e293b', boxShadow: '0 1px 3px rgba(0,0,0,0.05)', fontSize: 14, lineHeight: 1.5, border: msg.role === 'assistant' ? '1px solid #e2e8f0' : 'none' }}>{msg.content}</div>
                                    <span style={{ fontSize: 11, color: '#94a3b8', marginTop: 4 }}>{msg.role === 'user' ? 'Bạn' : 'AI'} • {new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
                                </div>
                            ))}
                        </div>
                        <div style={{ padding: 16, borderTop: '1px solid #e2e8f0', textAlign: 'center' }}><button onClick={() => setShowChatHistory(false)} style={{ background: '#d4a574', color: '#fff', border: 'none', padding: '10px 24px', borderRadius: 8, fontWeight: 600, cursor: 'pointer' }}>Đóng</button></div>
                    </div>
                </div>
            )}
            {/* Stats Modal */}
            {showStatsModal && (
                <div className="modal-overlay" onClick={() => setShowStatsModal(false)} style={{ background: 'rgba(15, 23, 42, 0.75)', backdropFilter: 'blur(12px)', zIndex: 10000, position: 'fixed', inset: 0, display: 'grid', placeItems: 'center', transition: 'all 0.3s ease' }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 1200, width: '92%', background: 'var(--bg-card, #1e293b)', color: 'var(--text-primary, #f8fafc)', borderRadius: 24, padding: '32px', border: '1px solid var(--border, #334155)', maxHeight: '90vh', overflowY: 'auto', boxShadow: '0 25px 50px -12px rgba(0,0,0,0.5)', display: 'flex', flexDirection: 'column', gap: '24px' }}>
                        {/* Header */}
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border, #334155)', paddingBottom: 20 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                                <span style={{ width: 44, height: 44, borderRadius: 12, background: 'rgba(212,165,116,0.15)', display: 'grid', placeItems: 'center', color: '#d4a574' }}>

```
