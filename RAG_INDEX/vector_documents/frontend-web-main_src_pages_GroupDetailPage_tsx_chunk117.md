# Knowledge Document: GroupDetailPage.tsx (Chunk 118/136)

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
  "chunk_index": 117,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
ize: 11, padding: '2px 8px', borderRadius: 6, background: item.checkOutTime ? 'rgba(16,185,129,0.1)' : 'rgba(245,158,11,0.1)', color: item.checkOutTime ? '#10b981' : '#f59e0b', fontWeight: 700 }}>
                                                {item.checkOutTime ? 'Đã hoàn thành' : 'Đang làm việc'}
                                            </span>
                                        </div>
                                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))', gap: 16, fontSize: 14, color: '#8e8e93', marginTop: 8 }}>
                                            <div>🕒 Vào ca: <strong style={{ color: '#fff' }}>{item.checkInTime ? new Date(item.checkInTime).toLocaleTimeString('vi-VN') : '--:--'}</strong></div>
                                            <div>🕒 Tan ca: <strong style={{ color: '#fff' }}>{item.checkOutTime ? new Date(item.checkOutTime).toLocaleTimeString('vi-VN') : '--:--'}</strong></div>
                                            <div>⏱️ Tổng giờ: <strong style={{ color: '#10b981' }}>{item.actualWorkHours !== undefined ? `${item.actualWorkHours} giờ` : '--'}</strong></div>
                                            <div>💼 Vai trò: <strong style={{ color: '#fff' }}>{item.productionStage || 'Thường'}</strong></div>
                                        </div>
                                    </div>
                                ))
                            )}
                        </div>
                        <div style={{ display: 'flex', justifyContent: 'flex-end', borderTop: '1px solid #232328', paddingTop: 16 }}>
                            <button onClick={() => setShowAttendanceHistory(false)} style={{ background: 'rgba(255, 255, 255, 0.08)', color: '#ffffff', border: 'none', padding: '10px 24px', borderRadius: 10, fontWeight: 600, cursor: 'pointer', fontSize: 13 }}>Đóng</button>
                        </div>
                    </div>
                </div>
            )}

            {/* Modal Quản lý chấm công nhóm */}
            {showTeamAttendance && (
                <div className="modal-overlay" onClick={() => setShowTeamAttendance(false)} style={{ background: 'rgba(10, 10, 12, 0.85)', backdropFilter: 'blur(10px)', zIndex: 10000, position: 'fixed', inset: 0, display: 'grid', placeItems: 'center' }}>

```
