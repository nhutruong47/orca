# Knowledge Document: GroupDetailPage.tsx (Chunk 20/136)

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
  "chunk_index": 19,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
linear-gradient(135deg, #ef4444 0%, #dc2626 100%)', border: 'none', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 700, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: '#fff' }}
                            >
                                <ion-icon name="exit-outline"></ion-icon> Tan ca
                            </button>
                        ) : (
                            <span style={{ fontSize: 12, fontWeight: 700, color: '#10b981', padding: '6px 12px', background: 'rgba(16,185,129,0.1)', borderRadius: 8 }}>
                                ✓ Đã hoàn thành ca
                            </span>
                        )
                    )}

                    {!isAdmin && (
                        <button
                            onClick={() => {
                                loadAttendanceHistory();
                                setShowAttendanceHistory(true);
                            }}
                            style={{ background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: 'var(--text-secondary)' }}
                        >
                            <ion-icon name="time-outline"></ion-icon> Lịch sử ca
                        </button>
                    )}

                    {isAdmin && (
                        <button
                            onClick={() => {
                                loadTeamAttendance();
                                setShowTeamAttendance(true);
                            }}
                            style={{ background: '#e0e7ff', border: '1px solid #c7d2fe', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 700, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: '#4338ca' }}
                        >
                            <ion-icon name="people-circle-outline"></ion-icon> Quản lý chấm công
                        </button>
                    )}


```
