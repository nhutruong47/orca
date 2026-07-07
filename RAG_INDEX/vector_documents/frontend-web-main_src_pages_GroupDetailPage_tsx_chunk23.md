# Knowledge Document: GroupDetailPage.tsx (Chunk 24/136)

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
  "chunk_index": 23,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
ng: '6px 14px', borderRadius: 20, border: memberRoleFilter === 'NONE' ? '1px solid var(--accent-primary, #d4a574)' : '1px solid var(--border, #e2e8f0)', background: memberRoleFilter === 'NONE' ? 'var(--accent-primary, #d4a574)' : 'transparent', color: memberRoleFilter === 'NONE' ? '#fff' : 'var(--text-secondary, #64748b)', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>Chưa phân vai</button>
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 260px))', gap: 14, marginBottom: 18 }}>
                    {visibleMemberStats.filter(m => {
                        if (memberRoleFilter === 'ALL') return true;
                        const roles = (m.jobLabels || []).filter((l: string) => l.trim().length > 0);
                        if (memberRoleFilter === 'NONE') return roles.length === 0;
                        return roles.includes(memberRoleFilter);
                    }).map(m => {
                        const displayName = m.fullName || m.username;
                    return (
                        <div key={m.userId} style={{ minWidth: 220, background: 'var(--bg-card, #fff)', borderRadius: 14, padding: '16px 20px', border: '1px solid var(--border, #e2e8f0)', flexShrink: 0 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 10 }}>
                                <div style={{ width: 36, height: 36, borderRadius: '50%', background: m.color, display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontWeight: 700, fontSize: 14 }}>{getInitials(displayName)}</div>
                                <div>
                                    <div style={{ fontWeight: 700, fontSize: 14, color: '#1e293b' }}>{displayName}</div>
                                    <div style={{ fontSize: 11, color: '#64748b' }}>{m.groupRole === 'ADMIN' || m.groupRole === 'OWNER' ? 'Trưởng nhóm' : 'Thành viên'}</div>
                                </div>
                                <div style={{ marginLeft: 'auto', fontSize: 18, fontWeight: 800, color: m.pct === 100 ? '#16a34a' : m.pct > 0 ? '#f59e0b' : '#94a3b8' }}>{m.pct}%</div>
                            </div>

                            {/* Tags / Job Labels */}

```
