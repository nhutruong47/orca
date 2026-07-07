# Knowledge Document: GroupDetailPage.tsx (Chunk 35/136)

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
  "chunk_index": 34,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
64748b',
                                    display: 'flex',
                                    alignItems: 'center',
                                    gap: 6
                                }}
                            >
                                <ion-icon name="people-outline"></ion-icon>
                                Tất cả công việc
                                <span style={{
                                    background: taskFilter === 'all' ? 'rgba(255,255,255,0.2)' : 'rgba(0,0,0,0.05)',
                                    padding: '1px 6px',
                                    borderRadius: 6,
                                    fontSize: 11,
                                    marginLeft: 6
                                }}>
                                    {latestGoalTasks.length}
                                </span>
                            </button>
                        )}
                    </div>
                </div>

                {/* Add task modal */}
                {showAddTask && isAdmin && (
                    <div className="modal-overlay" onClick={() => setShowAddTask(false)} style={{ background: 'rgba(0,0,0,0.6)', backdropFilter: 'blur(4px)', zIndex: 1000, position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                        <div className="modal" onClick={e => e.stopPropagation()} style={{ maxWidth: 600, width: '90%', background: 'var(--bg-panel, #fff)', color: 'var(--text-primary, #1a1a1a)', borderRadius: 16, padding: '32px', border: '1px solid rgba(255,255,255,0.1)', boxShadow: '0 25px 50px -12px rgba(0,0,0,0.25)' }}>
                            <h2 style={{ margin: '0 0 24px', fontSize: 20 }}>Tạo công việc mới</h2>
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
                                <div>
                                    <label style={{ display: 'block', fontSize: 14, fontWeight: 600, marginBottom: 8 }}>Loại công việc / Mục tiêu</label>
                                    <select value={selectedGoalId || ''} onChange={e => setSelectedGoalId(e.target.value)} style={{ width: '100%', padding: '12px 14px', borderRadius: 8, border: '1px solid var(--border, #cbd5e1)', fontSize: 14, background: 'var(--bg-input, #f8fafc)', color: 'var(--text-primary, #1a1a1a)' }}>

```
