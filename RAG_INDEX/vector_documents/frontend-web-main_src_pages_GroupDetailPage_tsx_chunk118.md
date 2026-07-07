# Knowledge Document: GroupDetailPage.tsx (Chunk 119/136)

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
  "chunk_index": 118,
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
                </div>
            )}

            {/* Modal Quản lý chấm công nhóm */}
            {showTeamAttendance && (
                <div className="modal-overlay" onClick={() => setShowTeamAttendance(false)} style={{ background: 'rgba(10, 10, 12, 0.85)', backdropFilter: 'blur(10px)', zIndex: 10000, position: 'fixed', inset: 0, display: 'grid', placeItems: 'center' }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 1000, minWidth: 'min(90vw, 850px)', width: '100%', background: '#121214', color: '#ffffff', borderRadius: 20, padding: '32px', border: '1px solid #232328', maxHeight: '85vh', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '24px' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #232328', paddingBottom: 16 }}>
                            <h3 style={{ margin: 0, fontSize: 18, fontWeight: 700, color: '#ffffff' }}>Quản lý chấm công toàn nhóm</h3>
                            <button onClick={() => setShowTeamAttendance(false)} style={{ background: 'rgba(255, 255, 255, 0.08)', border: 'none', width: 32, height: 32, borderRadius: '50%', cursor: 'pointer', color: '#fff', display: 'grid', placeItems: 'center' }}>✕</button>
                        </div>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                            {teamAttendanceData.length === 0 ? (
                                <div style={{ textAlign: 'center', padding: '30px 0', color: '#8e8e93' }}>Chưa có lịch sử chấm công nào trong nhóm.</div>
                            ) : (
                                <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
                                    <thead>
                                        <tr style={{ background: '#1c1c1e', borderBottom: '1px solid #2d2d34' }}>
                                            <th style={{ padding: '12px 8px', textAlign: 'left', color: '#8e8e93' }}>Nhân viên</th>
                                            <th style={{ padding: '12px 8px', textAlign: 'left', color: '#8e8e93' }}>Ngày</th>
                                            <th style={{ padding: '12px 8px', textAlign: 'left', color: '#8e8e93' }}>Vào ca</th>

```
