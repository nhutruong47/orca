# Knowledge Document: GroupDetailPage.tsx (Chunk 23/136)

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
  "chunk_index": 22,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
      </div>
                        <div>
                            <div style={{ fontSize: 24, fontWeight: 800, color: 'var(--text-primary)' }}>{s.value}</div>
                            <div style={{ fontSize: 12, color: 'var(--text-secondary)', fontWeight: 500 }}>{s.label}</div>
                        </div>
                    </div>
                ))}
            </div>
            )}

            {/* ===== EMPTY STATE / ANALYTICS ===== */}
            {/* ===== MEMBER CARDS ===== */}
            {showMemberRoles && visibleMemberStats.length > 0 && (
            <>
                <div style={{ display: 'flex', gap: 8, marginBottom: 16, flexWrap: 'wrap' }}>
                    <button onClick={() => setMemberRoleFilter('ALL')} style={{ padding: '6px 14px', borderRadius: 20, border: memberRoleFilter === 'ALL' ? '1px solid var(--accent-primary, #d4a574)' : '1px solid var(--border, #e2e8f0)', background: memberRoleFilter === 'ALL' ? 'var(--accent-primary, #d4a574)' : 'transparent', color: memberRoleFilter === 'ALL' ? '#fff' : 'var(--text-secondary, #64748b)', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>Tất cả</button>
                    {Array.from(new Set(visibleMemberStats.flatMap(m => m.jobLabels || []).filter((l: string) => l.trim().length > 0))).map(role => (
                        <button key={role} onClick={() => setMemberRoleFilter(role)} style={{ padding: '6px 14px', borderRadius: 20, border: memberRoleFilter === role ? '1px solid var(--accent-primary, #d4a574)' : '1px solid var(--border, #e2e8f0)', background: memberRoleFilter === role ? 'var(--accent-primary, #d4a574)' : 'transparent', color: memberRoleFilter === role ? '#fff' : 'var(--text-secondary, #64748b)', fontSize: 13, fontWeight: 600, cursor: 'pointer', textTransform: 'capitalize' }}>
                            {role}
                        </button>
                    ))}
                    <button onClick={() => setMemberRoleFilter('NONE')} style={{ padding: '6px 14px', borderRadius: 20, border: memberRoleFilter === 'NONE' ? '1px solid var(--accent-primary, #d4a574)' : '1px solid var(--border, #e2e8f0)', background: memberRoleFilter === 'NONE' ? 'var(--accent-primary, #d4a574)' : 'transparent', color: memberRoleFilter === 'NONE' ? '#fff' : 'var(--text-secondary, #64748b)', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>Chưa phân vai</button>

```
