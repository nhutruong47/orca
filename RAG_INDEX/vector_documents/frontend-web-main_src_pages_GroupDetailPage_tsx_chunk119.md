# Knowledge Document: GroupDetailPage.tsx (Chunk 120/136)

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
  "chunk_index": 119,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
2d2d34' }}>
                                            <th style={{ padding: '12px 8px', textAlign: 'left', color: '#8e8e93' }}>Nhân viên</th>
                                            <th style={{ padding: '12px 8px', textAlign: 'left', color: '#8e8e93' }}>Ngày</th>
                                            <th style={{ padding: '12px 8px', textAlign: 'left', color: '#8e8e93' }}>Vào ca</th>
                                            <th style={{ padding: '12px 8px', textAlign: 'left', color: '#8e8e93' }}>Tan ca</th>
                                            <th style={{ padding: '12px 8px', textAlign: 'left', color: '#8e8e93' }}>Giờ làm</th>
                                            <th style={{ padding: '12px 8px', textAlign: 'right', color: '#8e8e93' }}>Thao tác</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {teamAttendanceData.map((item, idx) => {
                                            const isEditing = editingAttendance?.id === item.id;
                                            return (
                                                <tr key={idx} style={{ borderBottom: '1px solid #232328' }}>
                                                    <td style={{ padding: '12px 8px', fontWeight: 600 }}>{item.userName || item.userId.substring(0,8)}</td>
                                                    <td style={{ padding: '12px 8px', color: '#d4a574' }}>{new Date(item.date).toLocaleDateString('vi-VN')}</td>
                                                    <td style={{ padding: '12px 8px' }}>
                                                        {isEditing ? (
                                                            <input type="datetime-local" value={editingAttendance?.checkInTime || ''} onChange={e => setEditingAttendance(prev => prev ? {...prev, checkInTime: e.target.value} : null)} style={{ background: '#2c2c2e', color: '#fff', border: '1px solid #3a3a3c', borderRadius: 6, padding: '4px 8px', fontSize: 12 }} />
                                                        ) : (
                                                            item.checkInTime ? new Date(item.checkInTime).toLocaleTimeString('vi-VN') : '--:--'
                                                        )}

```
