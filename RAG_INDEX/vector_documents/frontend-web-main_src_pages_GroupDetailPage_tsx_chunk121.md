# Knowledge Document: GroupDetailPage.tsx (Chunk 122/136)

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
  "chunk_index": 121,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
d' }}>
                                                                <button onClick={async () => {
                                                                    if (!editingAttendance) return;
                                                                    try {
                                                                        await attendanceService.updateAttendance(item.id, {
                                                                            checkInTime: editingAttendance.checkInTime ? new Date(editingAttendance.checkInTime).toISOString() : undefined,
                                                                            checkOutTime: editingAttendance.checkOutTime ? new Date(editingAttendance.checkOutTime).toISOString() : undefined
                                                                        });
                                                                        setEditingAttendance(null);
                                                                        loadTeamAttendance();
                                                                    } catch(e) {
                                                                        alert('Lỗi khi cập nhật chấm công');
                                                                    }
                                                                }} style={{ background: '#10b981', color: '#fff', border: 'none', borderRadius: 6, padding: '4px 10px', fontSize: 12, cursor: 'pointer' }}>Lưu</button>
                                                                <button onClick={() => setEditingAttendance(null)} style={{ background: '#ef4444', color: '#fff', border: 'none', borderRadius: 6, padding: '4px 10px', fontSize: 12, cursor: 'pointer' }}>Hủy</button>
                                                            </div>
                                                        ) : (
                                                            <button onClick={() => {
                                                                // Convert to format required by datetime-local: YYYY-MM-DDThh:mm
                                                                const toLocalString = (dateStr: string) => {
                                                                    if (!dateStr) return '';

```
