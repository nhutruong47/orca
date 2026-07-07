# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 4/12)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductivityAnalyticsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 3,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
geData = stageEff.map((s: any) => ({
        name: s.stage,
        'Muc tieu': s.totalTargetKg || 0,
        'Thuc te': s.totalActualKg || 0,
    }));

    const RISK_COLOR: Record<string, string> = { NONE: '#10b981', LOW: '#10b981', MEDIUM: '#f59e0b', HIGH: '#ef4444', CRITICAL: '#dc2626' };

    return (
        <div style={{ padding: '24px 28px', margin: '0 auto' }}>
            {/* Header */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 20 }}>
                <button onClick={() => navigate(`/groups/${teamId}`)} style={{
                    background: 'var(--bg-input)', border: '1px solid var(--border)', borderRadius: 10,
                    width: 36, height: 36, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                    color: 'var(--text-secondary)', fontSize: 18,
                }}>
                    <ion-icon name="chevron-back-outline" />
                </button>
                <h1 style={{ fontSize: 20, fontWeight: 800, color: 'var(--text-primary)', margin: 0 }}>Phan tich Nang suat</h1>
            </div>

            {/* Date filter */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', marginBottom: 20, flexWrap: 'wrap' }}>
                <input type="date" value={startDate} onChange={e => setStartDate(e.target.value)}
                    style={{ padding: '8px 14px', borderRadius: 10, border: '1px solid var(--border)', background: 'var(--bg-input)', color: 'var(--text-primary)', fontSize: 13 }} />
                <span style={{ color: 'var(--text-muted)', fontSize: 13 }}>den</span>
                <input type="date" value={endDate} onChange={e => setEndDate(e.target.value)}
                    style={{ padding: '8px 14px', borderRadius: 10, border: '1px solid var(--border)', background: 'var(--bg-input)', color: 'var(--text-primary)', fontSize: 13 }} />
                <button onClick={loadAnalytics} style={{
                    padding: '8px 16px', borderRadius: 10, border: 'none',
                    background: 'linear-gradient(135deg, #10b981, #059669)', color: '#fff',
                    fontSize: 13, fontWeight: 700, cursor: 'pointer'
                }}>Tai lai</button>
            </div>

            {/* KPI */}
            <div style={{ display: 'flex', gap: 12, marginBottom: 20, flexWrap: 'wrap' }}>

```
