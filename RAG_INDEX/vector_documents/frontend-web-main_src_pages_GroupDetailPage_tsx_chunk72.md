# Knowledge Document: GroupDetailPage.tsx (Chunk 73/136)

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
  "chunk_index": 72,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
 8, fontSize: 12, fontWeight: 600 }}><ion-icon name="checkmark-circle" style={{ color: '#10b981' }}></ion-icon> {successMsg}</div>}
                    </div>
                </div>
            )}

            {/* Create Goal Modal */}
            {showCreateGoal && (
                <div className="modal-overlay" onClick={() => setShowCreateGoal(false)} style={{ background: 'rgba(0,0,0,0.6)' }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 440, background: '#fff', color: '#1a1a1a', borderRadius: 16 }}>
                        <h2 style={{ marginBottom: 4, color: '#111' }}>Tạo mục tiêu mới</h2>
                        <p style={{ fontSize: 13, color: '#6b7280', marginBottom: 20 }}>AI sẽ tự động chia nhỏ thành các task.</p>
                        {error && <div style={{ background: '#fef2f2', color: '#dc2626', padding: '8px 12px', borderRadius: 8, fontSize: 13, marginBottom: 12 }}>{error}</div>}
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                            <input value={goalTitle} onChange={e => setGoalTitle(e.target.value)} placeholder="Tên mục tiêu *" style={{ padding: '10px 14px', borderRadius: 8, border: '1px solid #e2e8f0', fontSize: 14 }} autoFocus />
                            <input value={goalTarget} onChange={e => setGoalTarget(e.target.value)} placeholder="Sản lượng mục tiêu" style={{ padding: '10px 14px', borderRadius: 8, border: '1px solid #e2e8f0', fontSize: 14 }} />
                            <input type="datetime-local" value={goalDeadline} onChange={e => setGoalDeadline(e.target.value)} style={{ padding: '10px 14px', borderRadius: 8, border: '1px solid #e2e8f0', fontSize: 14 }} />
                        </div>
                        <div style={{ display: 'flex', gap: 8, justifyContent: 'flex-end', marginTop: 20, flexWrap: 'wrap' }}>
                            <button onClick={() => setShowCreateGoal(false)} style={{ padding: '10px 20px', borderRadius: 8, border: '1px solid #e2e8f0', background: '#fff', color: '#64748b', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>Hủy</button>

```
