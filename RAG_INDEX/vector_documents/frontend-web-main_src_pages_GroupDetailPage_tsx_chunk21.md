# Knowledge Document: GroupDetailPage.tsx (Chunk 22/136)

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
  "chunk_index": 21,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
ai trò</button>}

                    {isAdmin && <button onClick={() => setShowAddMember(true)} style={{ background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10, padding: '8px 16px', fontSize: 13, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, color: 'var(--text-secondary)' }}><ion-icon name="people-outline"></ion-icon> Mời</button>}
                    {isAdmin && <button onClick={handleDeleteTeam} style={{ background: '#fef2f2', border: '1px solid #fecaca', borderRadius: 10, padding: '8px', fontSize: 16, cursor: 'pointer', color: '#ef4444', display: 'flex' }}><ion-icon name="trash-outline"></ion-icon></button>}
                </div>
            </div>

            {/* ===== STATS CARDS ===== */}
            {isManager && totalTasks > 0 && (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 14, marginBottom: 18 }}>
                {[
                    { label: 'Tổng công việc', value: totalTasks, icon: 'clipboard-outline', bg: '#f9f1e3', color: '#d4a574' },
                    { label: 'Chưa bắt đầu', value: pendingTasks, icon: 'time-outline', bg: '#f8fafc', color: '#94a3b8' },
                    { label: 'Đang thực hiện', value: inProgressTasks, icon: 'sync-outline', bg: '#fff7ed', color: '#f59e0b' },
                    { label: 'Hoàn thành', value: completedTasks, icon: 'checkmark-circle-outline', bg: '#f0fdf4', color: '#16a34a' },
                ].map((s, i) => (
                    <div key={i} style={{ background: 'var(--bg-card)', borderRadius: 14, padding: '16px 18px', border: '1px solid var(--border)', display: 'flex', alignItems: 'center', gap: 14 }}>
                        <div style={{ width: 48, height: 48, borderRadius: 12, background: s.bg, display: 'flex', alignItems: 'center', justifyContent: 'center', color: s.color, fontSize: 24 }}>
                            <ion-icon name={s.icon}></ion-icon>
                        </div>
                        <div>
                            <div style={{ fontSize: 24, fontWeight: 800, color: 'var(--text-primary)' }}>{s.value}</div>
                            <div style={{ fontSize: 12, color: 'var(--text-secondary)', fontWeight: 500 }}>{s.label}</div>
                        </div>
                    </div>
                ))}
            </div>
            )}


```
