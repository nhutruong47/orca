# Knowledge Document: GroupDetailPage.tsx (Chunk 25/136)

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
  "chunk_index": 24,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
groupRole === 'ADMIN' || m.groupRole === 'OWNER' ? 'Trưởng nhóm' : 'Thành viên'}</div>
                                </div>
                                <div style={{ marginLeft: 'auto', fontSize: 18, fontWeight: 800, color: m.pct === 100 ? '#16a34a' : m.pct > 0 ? '#f59e0b' : '#94a3b8' }}>{m.pct}%</div>
                            </div>

                            {/* Tags / Job Labels */}
                            {((m.jobLabels && m.jobLabels.filter((l: string) => l.trim().length > 0).length > 0) || isAdmin) && (
                                <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, marginBottom: 12, minHeight: 24 }}>
                                    {m.jobLabels && m.jobLabels.filter((l: string) => l.trim().length > 0).length > 0 && (
                                        m.jobLabels.filter((l: string) => l.trim().length > 0).map((lbl: string, i: number) => (
                                            <span key={i} style={{ background: '#e0e7ff', color: '#4338ca', padding: '2px 8px', borderRadius: 6, fontSize: 10, fontWeight: 700, border: '1px solid #c7d2fe' }}>
                                                {lbl}
                                            </span>
                                        ))
                                    )}
                                    {isAdmin && (
                                        <button onClick={() => { setSelectedMemberForLabels(m); setEditingLabels(m.jobLabels?.join(', ') || ''); setShowLabelModal(true); }} style={{ background: '#f8fafc', border: '1px dashed #cbd5e1', color: '#64748b', borderRadius: 6, padding: '2px 8px', display: 'flex', alignItems: 'center', gap: 4, cursor: 'pointer', fontSize: 11, fontWeight: 600, transition: 'all 0.2s' }}>
                                            <ion-icon name="add"></ion-icon> Phân vai trò
                                        </button>
                                    )}
                                </div>
                            )}

                            <div style={{ height: 6, background: '#f1f5f9', borderRadius: 3, overflow: 'hidden', marginBottom: 6 }}>
                                <div style={{ height: '100%', background: m.pct === 100 ? '#16a34a' : m.pct > 0 ? '#f59e0b' : '#e2e8f0', borderRadius: 3, width: `${m.pct}%`, transition: 'width 0.4s' }} />
                            </div>

```
