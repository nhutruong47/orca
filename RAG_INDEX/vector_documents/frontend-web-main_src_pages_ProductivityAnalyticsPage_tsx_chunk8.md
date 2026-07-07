# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 9/12)

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
  "chunk_index": 8,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
 {/* Thong ke don hang */}
                <SectionCard title="Thong ke Don hang">
                    <div style={{ display: 'flex', flexDirection: 'column', gap: 0 }}>
                        {[
                            { label: 'Da hoan thanh', value: os.completed || 0, color: '#10b981' },
                            { label: 'Dang san xuat', value: os.inProduction || 0, color: '#3b82f6' },
                            { label: 'Cho xu ly', value: os.pending || 0, color: '#f59e0b' },
                            { label: 'Co nguy co tre', value: os.atRisk || 0, color: '#ef4444' },
                        ].map((row, i, arr) => (
                            <div key={row.label} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 0', borderBottom: i < arr.length - 1 ? '1px solid var(--border)' : 'none' }}>
                                <span style={{ fontSize: 13, color: 'var(--text-secondary)' }}>{row.label}</span>
                                <span style={{ fontSize: 20, fontWeight: 900, color: row.color }}>{row.value}</span>
                            </div>
                        ))}
                    </div>
                </SectionCard>
            </div>

            {/* Bang chi tiet cong doan */}
            {stageEff.length > 0 && (
                <div style={{ marginBottom: 20 }}>
                    <SectionCard title="Chi tiet Hieu suat Cong doan">
                        <div style={{ overflowX: 'auto' }}>
                            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
                                <thead>
                                    <tr style={{ borderBottom: '1px solid var(--border)' }}>
                                        {['Cong doan', 'Muc tieu (kg)', 'Thuc te (kg)', 'Hieu suat', 'Nang suat (kg/gio)', 'Ty le loi'].map(h => (
                                            <th key={h} style={{ textAlign: 'right', padding: '10px 12px', color: 'var(--text-muted)', fontWeight: 600 }}>{h}</th>
                                        ))}
                                    </tr>
                                </thead>
                                <tbody>
                                    {stageEff.map((s: any) => {

```
