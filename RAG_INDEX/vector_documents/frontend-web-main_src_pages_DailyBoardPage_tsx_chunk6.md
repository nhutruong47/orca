# Knowledge Document: DailyBoardPage.tsx (Chunk 7/10)

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
  "chunk_index": 6,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
isplay: 'flex', flexDirection: 'column', gap: 12 }}>
                        {board.orderRows.map((row: any) => (
                            <div key={row.orderId} style={{
                                background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14,
                                padding: 20, borderLeft: `4px solid ${RISK_COLOR[row.riskLevel] || '#10b981'}`
                            }}>
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 12 }}>
                                    <div>
                                        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
                                            <span style={{ fontSize: 12, fontWeight: 800, color: '#8b5cf6' }}>{row.orderCode}</span>
                                            {row.riskLevel !== 'NONE' && (
                                                <span style={{ fontSize: 10, fontWeight: 700, padding: '2px 8px', borderRadius: 4, background: `${RISK_COLOR[row.riskLevel]}20`, color: RISK_COLOR[row.riskLevel] }}>
                                                    {RISK_LABEL[row.riskLevel]}
                                                </span>
                                            )}
                                        </div>
                                        <div style={{ fontSize: 15, fontWeight: 700, color: 'var(--text-primary)' }}>{row.title}</div>
                                        {row.customerName && <div style={{ fontSize: 12, color: 'var(--text-muted)', marginTop: 2 }}>{row.customerName}</div>}
                                    </div>
                                    <div style={{ textAlign: 'right' }}>
                                        <div style={{ fontSize: 22, fontWeight: 900, color: '#10b981' }}>
                                            {row.completedQuantity?.toLocaleString('vi-VN')}
                                        </div>
                                        <div style={{ fontSize: 12, color: 'var(--text-muted)' }}>/ {row.outputTarget?.toLocaleString('vi-VN')} kg</div>
                                    </div>
                                </div>


```
