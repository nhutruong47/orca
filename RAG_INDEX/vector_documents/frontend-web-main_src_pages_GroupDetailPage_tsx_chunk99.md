# Knowledge Document: GroupDetailPage.tsx (Chunk 100/136)

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
  "chunk_index": 99,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
,0.6)', display: 'flex', flexDirection: 'column', gap: '20px', fontFamily: "'Inter', sans-serif" }}>
                        {/* Header */}
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #232328', paddingBottom: 16 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                                <span style={{ width: 44, height: 44, borderRadius: 10, background: 'rgba(59, 130, 246, 0.15)', display: 'grid', placeItems: 'center', color: '#3b82f6' }}>
                                    <ion-icon name="calendar-outline" style={{ fontSize: 24 }}></ion-icon>
                                </span>
                                <div>
                                    <h2 style={{ margin: 0, fontSize: 20, fontWeight: 700, color: '#ffffff', letterSpacing: '-0.02em' }}>
                                        Lịch trình & Kế hoạch Sản xuất
                                    </h2>
                                    <p style={{ margin: '4px 0 0', fontSize: 13, color: '#8e8e93' }}>Theo dõi lịch hạn công việc và tiến độ trực quan</p>
                                </div>
                            </div>
                            <button onClick={() => setShowScheduleModal(false)} style={{ background: 'rgba(255, 255, 255, 0.08)', border: 'none', width: 36, height: 36, borderRadius: '50%', display: 'grid', placeItems: 'center', cursor: 'pointer', color: '#ffffff', transition: 'background 0.2s' }} onMouseEnter={e => e.currentTarget.style.background = 'rgba(255, 255, 255, 0.15)'} onMouseLeave={e => e.currentTarget.style.background = 'rgba(255, 255, 255, 0.08)'}><ion-icon name="close" style={{ fontSize: 22 }}></ion-icon></button>
                        </div>

                        {/* Calendar Body Layout (Split Panel) */}
                        {(() => {
                            const year = calendarDate.getFullYear();
                            const month = calendarDate.getMonth();

                            // Days calculations
                            const numDays = new Date(year, month + 1, 0).getDate();
                            const startDay = new Date(year, month, 1).getDay(); // Sunday=0, Monday=1
                            const offset = startDay === 0 ? 6 : startDay - 1; // Align to Monday start


```
