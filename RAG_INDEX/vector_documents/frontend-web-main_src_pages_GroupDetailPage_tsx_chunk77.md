# Knowledge Document: GroupDetailPage.tsx (Chunk 78/136)

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
  "chunk_index": 77,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
ine"></ion-icon> Tạo vai trò
                            </button>
                            <div style={{ display: 'flex', gap: 10 }}>
                                <button onClick={() => setShowLabelModal(false)} style={{ padding: '10px 20px', borderRadius: 10, border: '1px solid #e2e8f0', background: '#fff', color: '#64748b', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>Hủy</button>
                                <button onClick={handleSaveLabels} disabled={loading} style={{ padding: '10px 20px', borderRadius: 10, border: 'none', background: '#d4a574', color: '#fff', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>
                                    {loading ? 'Đang lưu...' : 'Lưu'}
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Manage Roles Modal */}
            {showManageRolesModal && (
                <div className="modal-overlay" onClick={() => setShowManageRolesModal(false)} style={{ background: 'rgba(0,0,0,0.6)', backdropFilter: 'blur(4px)', zIndex: 1000 }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 400, background: '#fff', color: '#1a1a1a', borderRadius: 16, padding: '24px' }}>
                        <h2 style={{ margin: '0 0 8px', color: '#1e293b', fontSize: 18 }}>Quản lý vai trò</h2>
                        <p style={{ fontSize: 13, color: '#64748b', marginBottom: 20 }}>
                            Thêm các vai trò chuẩn để phân công nhanh cho thành viên.
                        </p>
                        
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 8, marginBottom: 20, maxHeight: 200, overflowY: 'auto' }}>
                            {teamRoles.length === 0 ? (
                                <div style={{ fontSize: 13, color: '#94a3b8', textAlign: 'center', padding: '10px 0' }}>Chưa có vai trò nào</div>
                            ) : (
                                teamRoles.map(role => (
                                    <div key={role} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 14px', background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: 8 }}>

```
