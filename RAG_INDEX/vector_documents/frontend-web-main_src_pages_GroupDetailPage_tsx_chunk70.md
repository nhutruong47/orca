# Knowledge Document: GroupDetailPage.tsx (Chunk 71/136)

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
  "chunk_index": 70,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
ay: 'flex', justifyContent: 'center', gap: 24, background: 'linear-gradient(transparent, rgba(0,0,0,0.8))' }}>
                        <button style={{ width: 64, height: 64, borderRadius: '50%', background: '#374151', border: 'none', color: '#fff', fontSize: 24, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}><ion-icon name="mic-outline"></ion-icon></button>
                        <button style={{ width: 64, height: 64, borderRadius: '50%', background: '#374151', border: 'none', color: '#fff', fontSize: 24, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}><ion-icon name="videocam-outline"></ion-icon></button>
                        <button onClick={() => setShowVideoCall(false)} style={{ width: 64, height: 64, borderRadius: '50%', background: '#ef4444', border: 'none', color: '#fff', fontSize: 24, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}><ion-icon name="call-outline" style={{ transform: 'rotate(135deg)' }}></ion-icon></button>
                    </div>
                </div>
            )}

            {/* Invite Modal */}
            {showAddMember && (
                <div className="modal-overlay" onClick={closeModal} style={{ background: 'rgba(0,0,0,0.6)', backdropFilter: 'blur(8px)' }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 480, padding: 0, borderRadius: 20, overflow: 'hidden', background: '#fff', border: 'none', color: '#1a1a1a', boxShadow: '0 25px 50px -12px rgba(0,0,0,0.25)' }}>
                        <div style={{ padding: '24px 32px', textAlign: 'center' }}>
                            <h2 style={{ fontSize: 24, fontWeight: 800, color: '#111827', margin: '0 0 8px' }}>Mời thành viên</h2>
                            <p style={{ fontSize: 13, color: '#6b7280', margin: 0 }}>Gửi lời mời bằng email cho người bạn muốn thêm vào nhóm.</p>
                        </div>
                        <div style={{ padding: '0 32px 24px' }}>
                            {error && <div style={{ background: '#fef2f2', color: '#dc2626', padding: '8px 12px', borderRadius: 8, fontSize: 13, marginBottom: 12 }}>{error}</div>}
                            <label style={{ display: 'block', fontSize: 13, fontWeight: 700, color: '#374151', marginBottom: 8 }}>Email người được mời</label>

```
