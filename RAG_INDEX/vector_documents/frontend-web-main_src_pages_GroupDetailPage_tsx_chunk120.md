# Knowledge Document: GroupDetailPage.tsx (Chunk 121/136)

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
  "chunk_index": 120,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
)} style={{ background: '#2c2c2e', color: '#fff', border: '1px solid #3a3a3c', borderRadius: 6, padding: '4px 8px', fontSize: 12 }} />
                                                        ) : (
                                                            item.checkInTime ? new Date(item.checkInTime).toLocaleTimeString('vi-VN') : '--:--'
                                                        )}
                                                    </td>
                                                    <td style={{ padding: '12px 8px' }}>
                                                        {isEditing ? (
                                                            <input type="datetime-local" value={editingAttendance?.checkOutTime || ''} onChange={e => setEditingAttendance(prev => prev ? {...prev, checkOutTime: e.target.value} : null)} style={{ background: '#2c2c2e', color: '#fff', border: '1px solid #3a3a3c', borderRadius: 6, padding: '4px 8px', fontSize: 12 }} />
                                                        ) : (
                                                            item.checkOutTime ? new Date(item.checkOutTime).toLocaleTimeString('vi-VN') : '--:--'
                                                        )}
                                                    </td>
                                                    <td style={{ padding: '12px 8px', color: '#10b981', fontWeight: 700 }}>
                                                        {item.actualWorkHours !== undefined ? `${item.actualWorkHours}h` : '--'}
                                                    </td>
                                                    <td style={{ padding: '12px 8px', textAlign: 'right' }}>
                                                        {isEditing ? (
                                                            <div style={{ display: 'flex', gap: 6, justifyContent: 'flex-end' }}>
                                                                <button onClick={async () => {
                                                                    if (!editingAttendance) return;
                                                                    try {
                                                                        await attendanceService.updateAttendance(item.id, {

```
