# Knowledge Document: GroupDetailPage.tsx (Chunk 74/136)

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
  "chunk_index": 73,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
         </div>
                        <div style={{ display: 'flex', gap: 8, justifyContent: 'flex-end', marginTop: 20, flexWrap: 'wrap' }}>
                            <button onClick={() => setShowCreateGoal(false)} style={{ padding: '10px 20px', borderRadius: 8, border: '1px solid #e2e8f0', background: '#fff', color: '#64748b', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>Hủy</button>
                            <button onClick={() => handleCreateGoal(false)} disabled={loading} style={{ padding: '10px 20px', borderRadius: 8, border: '1px solid #e2e8f0', background: '#f0fdf4', color: '#16a34a', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>{loading ? 'Đang tạo...' : 'Tạo thủ công'}</button>
                            <button onClick={() => handleCreateGoal(true)} disabled={loading || !trialActive} style={{ padding: '10px 20px', borderRadius: 8, border: 'none', background: '#d4a574', color: '#fff', fontSize: 13, fontWeight: 600, cursor: 'pointer', opacity: trialActive ? 1 : 0.5 }}>{loading ? 'Đang tạo...' : `AI tạo task (${trialDays} ngày)`}</button>
                        </div>
                    </div>
                </div>
            )}

            {/* Ad Settings Modal */}
            {showAdSettings && (
                <div className="modal-overlay" onClick={() => setShowAdSettings(false)} style={{ background: 'rgba(0,0,0,0.6)' }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 440, background: '#fff', color: '#1a1a1a', borderRadius: 16 }}>
                        <h2 style={{ marginBottom: 4, color: '#111' }}>Cài đặt Marketplace</h2>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '12px', background: '#f8fafc', borderRadius: 8, marginBottom: 16, marginTop: 16 }}>
                            <input type="checkbox" checked={isPublished} onChange={e => setIsPublished(e.target.checked)} style={{ width: 16, height: 16 }} />
                            <label style={{ fontSize: 14, fontWeight: 600 }}>Công khai trên Marketplace</label>
                        </div>
                        {isPublished && (
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>

```
