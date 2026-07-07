# Knowledge Document: FactoryDashboardPage.tsx (Chunk 11/14)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/FactoryDashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "dashboard",
    "production",
    "factory",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 10,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
                       )}
                        </>
                    )}
                </div>
            </div>

            {/* Section C: Nhan su */}
            <div style={{ marginBottom: 32 }}>
                <h2 style={{ fontSize: 16, fontWeight: 700, marginBottom: 12, color: 'var(--text-primary)' }}>
                    Nhan su hom nay ({dashboard.staffToday})
                </h2>
                <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14, padding: 16 }}>
                    {dashboard.staffDetails?.length === 0 ? (
                        <div style={{ color: 'var(--text-muted)', textAlign: 'center', fontSize: 13, padding: 20 }}>Chua co nhan vien check-in</div>
                    ) : (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                            {dashboard.staffDetails?.map((staff: any) => (
                                <div key={staff.userId} style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '10px 0', borderBottom: '1px solid var(--border)' }}>
                                    <div style={{ width: 36, height: 36, borderRadius: '50%', background: 'var(--accent-primary)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontWeight: 700, fontSize: 13, flexShrink: 0 }}>
                                        {(staff.userName || '?').charAt(0).toUpperCase()}
                                    </div>
                                    <div style={{ flex: 1 }}>
                                        <div style={{ fontWeight: 600, fontSize: 14 }}>{staff.userName}</div>
                                        <div style={{ fontSize: 12, color: 'var(--text-secondary)' }}>
                                            {SHIFT_LABELS[staff.shiftType] || staff.shiftType} · {STAGE_LABELS[staff.stage] || staff.stage}
                                            {staff.orderTitle && ` · ${staff.orderTitle}`}
                                        </div>
                                    </div>
                                    <div style={{ textAlign: 'right' }}>
                                        <div style={{ fontWeight: 700, fontSize: 14, color: staff.workHours ? '#10b981' : 'var(--text-muted)' }}>

```
