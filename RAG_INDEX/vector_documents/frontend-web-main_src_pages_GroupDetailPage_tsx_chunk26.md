# Knowledge Document: GroupDetailPage.tsx (Chunk 27/136)

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
  "chunk_index": 26,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
v>
                    );
                })}
            </div>
            </>
            )}

            {/* ===== DB ROADMAP: same source as task table ===== */}
            {isAdmin && latestGoal && (
            <div style={{ background: 'var(--bg-card)', borderRadius: 14, border: '1px solid var(--border)', overflow: 'hidden', marginBottom: 18, boxShadow: '0 10px 26px rgba(0,0,0,0.06)' }}>
                <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border)', background: 'var(--bg-secondary)', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: 16 }}>
                    <div style={{ display: 'flex', alignItems: 'flex-start', gap: 12, minWidth: 0 }}>
                        <span style={{ width: 36, height: 36, borderRadius: 10, background: 'rgba(212, 165, 116, 0.15)', color: 'var(--accent-primary)', display: 'grid', placeItems: 'center', flexShrink: 0 }}>
                            <ion-icon name="flag-outline" style={{ fontSize: 18 }}></ion-icon>
                        </span>
                        <div style={{ minWidth: 0 }}>
                            <div style={{ fontSize: 11, color: 'var(--accent-primary)', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: 4 }}>Muc tieu san xuat</div>
                            <h3 style={{ margin: 0, fontSize: 17, fontWeight: 800, color: 'var(--text-primary)', lineHeight: 1.35 }}>{latestGoal.title}</h3>
                            <div style={{ marginTop: 6, color: 'var(--text-secondary)', fontSize: 13 }}>{latestGoal.outputTarget || latestGoal.rawInstruction}</div>
                        </div>
                    </div>
                    <span style={{ background: 'rgba(212, 165, 116, 0.15)', color: 'var(--accent-primary)', padding: '5px 10px', borderRadius: 8, fontSize: 11, fontWeight: 800, whiteSpace: 'nowrap' }}>CAP NHAT MOI NHAT</span>
                </div>
                <div style={{ padding: 20 }}>
                    <div style={{ fontSize: 11, fontWeight: 800, color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: 10 }}>Roadmap tu task database</div>
                    <table style={{ width: '100%', borderCollapse: 'collapse', border: '1px solid var(--border)', borderRadius: 10, overflow: 'hidden' }}>
                        <thead>

```
