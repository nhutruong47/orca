# Knowledge Document: WorkforcePage.tsx (Chunk 3/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/WorkforcePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 2,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, production

## Source Code Chunk
```tsx
                background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                    width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                    color: 'var(--text-secondary)', fontSize: 18,
                }}>
                    <ion-icon name="chevron-back-outline" />
                </button>
                <h1 style={{ fontSize: 20, fontWeight: 800, color: 'var(--text-primary)', margin: 0 }}>Nhan su Hom nay</h1>
            </div>

            {/* KPI Pills */}
            <div style={{ display: 'flex', gap: 12, marginBottom: 20, flexWrap: 'wrap' }}>
                <MetricPill label="Dang lam viec" value={wf.checkedIn?.length || 0} unit=" nguoi" color="#3b82f6" />
                <MetricPill label="Da check-out" value={wf.checkedOut?.length || 0} unit=" nguoi" color="#10b981" />
                <MetricPill label="Tong gio cong" value={(wf.totalWorkHours || 0).toFixed(1)} unit=" gio" color="#8b5cf6" />
                <MetricPill label="Chua check-out" value={wf.notCheckedOut || 0} unit=" nguoi" color="#f59e0b" />
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16, marginBottom: 20 }}>
                {/* Gio cong theo cong doan */}
                <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 16, padding: 20 }}>
                    <h2 style={{ fontSize: 14, fontWeight: 700, color: 'var(--text-primary)', marginBottom: 16 }}>Gio cong theo cong doan</h2>
                    {[
                        { label: 'Rang', hours: totalRoastHours, color: '#d97706' },
                        { label: 'QC / Xay', hours: totalQcHours, color: '#3b82f6' },
                        { label: 'Dong goi', hours: stageHours.DONG_GOI || 0, color: '#8b5cf6' },
                    ].map(row => (
                        <div key={row.label} style={{ marginBottom: 14 }}>
                            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 13, marginBottom: 6 }}>
                                <span style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>{row.label}</span>
                                <span style={{ fontWeight: 800, color: row.color }}>{row.hours.toFixed(1)} gio</span>
                            </div>

```
