# Knowledge Document: GroupDetailPage.tsx (Chunk 19/136)

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
  "chunk_index": 18,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
1px 2px rgba(0,0,0,0.28)',
                                animation: 'pulse-ai-btn 2s infinite',
                                transition: 'all 0.3s ease'
                            }}
                        >
                            <ion-icon name="sparkles" style={{ fontSize: '18px' }}></ion-icon>
                            Phân chia công việc tự động
                        </button>
                    )}

                    <button onClick={() => setShowStatsModal(true)} style={{ background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: 'var(--text-secondary)' }} id="btn-stats-modal"><ion-icon name="bar-chart-outline"></ion-icon> Thống kê</button>
                    
                    {/* Chức năng vào ca / tan ca */}
                    {!isAdmin && canCheckIn && (
                        !myAttendance ? (
                            <button
                                onClick={handleCheckIn}
                                disabled={loadingAttendance}
                                style={{ background: 'linear-gradient(135deg, #10b981 0%, #059669 100%)', border: 'none', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 700, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: '#fff' }}
                            >
                                <ion-icon name="enter-outline"></ion-icon> Vào ca
                            </button>
                        ) : !myAttendance.checkOutTime ? (
                            <button
                                onClick={handleCheckOut}
                                disabled={loadingAttendance}
                                style={{ background: 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)', border: 'none', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 700, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: '#fff' }}
                            >
                                <ion-icon name="exit-outline"></ion-icon> Tan ca
                            </button>
                        ) : (

```
