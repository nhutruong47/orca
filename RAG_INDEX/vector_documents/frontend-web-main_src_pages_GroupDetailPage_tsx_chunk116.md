# Knowledge Document: GroupDetailPage.tsx (Chunk 117/136)

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
  "chunk_index": 116,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
inset: 0, display: 'grid', placeItems: 'center' }}>
                    <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 900, minWidth: 'min(90vw, 750px)', width: '100%', background: '#121214', color: '#ffffff', borderRadius: 20, padding: '32px', border: '1px solid #232328', maxHeight: '80vh', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '24px' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #232328', paddingBottom: 16 }}>
                            <h3 style={{ margin: 0, fontSize: 18, fontWeight: 700, color: '#ffffff' }}>Lịch sử vào/ra ca của bạn</h3>
                            <button onClick={() => setShowAttendanceHistory(false)} style={{ background: 'rgba(255, 255, 255, 0.08)', border: 'none', width: 32, height: 32, borderRadius: '50%', cursor: 'pointer', color: '#fff', display: 'grid', placeItems: 'center' }}>✕</button>
                        </div>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                            {attendanceHistory.length === 0 ? (
                                <div style={{ textAlign: 'center', padding: '30px 0', color: '#8e8e93' }}>Chưa có lịch sử chấm công nào.</div>
                            ) : (
                                attendanceHistory.map((item, idx) => (
                                    <div key={idx} style={{ background: '#1c1c1e', border: '1px solid #2d2d34', borderRadius: 12, padding: 14, display: 'flex', flexDirection: 'column', gap: 8 }}>
                                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                            <span style={{ fontWeight: 700, color: '#d4a574' }}>Ngày {new Date(item.date).toLocaleDateString('vi-VN')}</span>
                                            <span style={{ fontSize: 11, padding: '2px 8px', borderRadius: 6, background: item.checkOutTime ? 'rgba(16,185,129,0.1)' : 'rgba(245,158,11,0.1)', color: item.checkOutTime ? '#10b981' : '#f59e0b', fontWeight: 700 }}>
                                                {item.checkOutTime ? 'Đã hoàn thành' : 'Đang làm việc'}
                                            </span>
                                        </div>

```
