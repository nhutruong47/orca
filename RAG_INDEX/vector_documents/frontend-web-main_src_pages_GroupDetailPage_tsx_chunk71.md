# Knowledge Document: GroupDetailPage.tsx (Chunk 72/136)

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
  "chunk_index": 71,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                    <div style={{ padding: '0 32px 24px' }}>
                            {error && <div style={{ background: '#fef2f2', color: '#dc2626', padding: '8px 12px', borderRadius: 8, fontSize: 13, marginBottom: 12 }}>{error}</div>}
                            <label style={{ display: 'block', fontSize: 13, fontWeight: 700, color: '#374151', marginBottom: 8 }}>Email người được mời</label>
                            <input
                                value={inviteEmail}
                                onChange={e => setInviteEmail(e.target.value)}
                                placeholder="name@example.com"
                                style={{ width: '100%', padding: '10px 12px', borderRadius: 10, border: '1px solid #e2e8f0', marginBottom: 12, fontSize: 14 }}
                            />
                            <p style={{ fontSize: 12, color: '#6b7280', margin: '0 0 12px' }}>Chỉ chủ nhóm hoặc quản trị viên mới có thể gửi lời mời.</p>
                            <div style={{ display: 'flex', gap: 8 }}>
                                <button onClick={closeModal} style={{ flex: 1, background: '#f8fafc', color: '#1f2937', border: '1px solid #e2e8f0', padding: '12px', borderRadius: 10, fontWeight: 700, fontSize: 14, cursor: 'pointer' }}>Hủy</button>
                                <button onClick={handleInviteMember} disabled={loading} style={{ flex: 1, background: loading ? '#e5e7eb' : '#d4a574', color: loading ? '#9ca3af' : '#fff', border: 'none', padding: '12px', borderRadius: 10, fontWeight: 700, fontSize: 14, cursor: loading ? 'not-allowed' : 'pointer' }}>{loading ? 'Đang gửi...' : 'Gửi lời mời'}</button>
                            </div>
                        </div>
                        {successMsg && <div style={{ position: 'absolute', bottom: 20, left: '50%', transform: 'translateX(-50%)', background: '#111827', color: '#fff', padding: '8px 16px', borderRadius: 8, fontSize: 12, fontWeight: 600 }}><ion-icon name="checkmark-circle" style={{ color: '#10b981' }}></ion-icon> {successMsg}</div>}
                    </div>
                </div>
            )}

            {/* Create Goal Modal */}
            {showCreateGoal && (
                <div className="modal-overlay" onClick={() => setShowCreateGoal(false)} style={{ background: 'rgba(0,0,0,0.6)' }}>

```
