# Knowledge Document: DailyBoardPage.tsx (Chunk 6/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DailyBoardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 5,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
-text-muted)' }}>Con <strong style={{ color: 'var(--text-primary)' }}>{remaining.toLocaleString('vi-VN')} kg</strong></span>
                </div>
            </div>

            {/* KPI Pills */}
            <div style={{ display: 'flex', gap: 12, marginBottom: 20, flexWrap: 'wrap' }}>
                <MetricPill label="Dang lam" value={board?.totalWorkers || 0} unit=" nguoi" color="#3b82f6" />
                <MetricPill label="Tong gio cong" value={((board?.totalWorkerHours || 0)).toFixed(1)} unit=" gio" color="#8b5cf6" />
                <MetricPill label="Don hang" value={board?.orderRows?.length || 0} unit="" color="#f59e0b" />
            </div>

            {/* Cong doan */}
            <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 16, padding: 24, marginBottom: 20 }}>
                <h2 style={{ fontSize: 15, fontWeight: 700, color: 'var(--text-primary)', marginBottom: 20 }}>San luong theo cong doan</h2>
                <StageRow label="Rang" target={roast.targetKg || 0} actual={roast.actualKg || 0} color="#d97706" />
                <StageRow label="QC" target={qc.targetKg || 0} actual={qc.actualKg || 0} color="#3b82f6" />
                <StageRow label="Dong goi" target={packaging.targetKg || 0} actual={packaging.actualKg || 0} color="#8b5cf6" />
            </div>

            {/* Don hang */}
            <div>
                <h2 style={{ fontSize: 15, fontWeight: 700, color: 'var(--text-primary)', marginBottom: 12 }}>
                    Don hang ({board?.orderRows?.length || 0})
                </h2>
                {!board?.orderRows?.length ? (
                    <div style={{ textAlign: 'center', padding: 40, background: 'var(--bg-card)', borderRadius: 14, border: '1px solid var(--border)', color: 'var(--text-muted)', fontSize: 13 }}>
                        Khong co don hang nao trong ngay nay
                    </div>
                ) : (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                        {board.orderRows.map((row: any) => (
                            <div key={row.orderId} style={{
                                background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14,
                                padding: 20, borderLeft: `4px solid ${RISK_COLOR[row.riskLevel] || '#10b981'}`

```
