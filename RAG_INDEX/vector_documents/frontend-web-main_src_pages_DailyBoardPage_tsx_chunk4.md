# Knowledge Document: DailyBoardPage.tsx (Chunk 5/10)

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
  "chunk_index": 4,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
                color: 'var(--text-secondary)', fontSize: 18,
                    }}>
                        <ion-icon name="chevron-forward-outline" />
                    </button>
                </div>
            </div>

            {/* Tong quan */}
            <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 16, padding: 24, marginBottom: 20 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: 16 }}>
                    <div>
                        <div style={{ fontSize: 11, color: 'var(--text-muted)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: 1.5, marginBottom: 6 }}>Tong san luong</div>
                        <div style={{ fontSize: 40, fontWeight: 900, color: completionRate >= 100 ? '#10b981' : '#ef4444', lineHeight: 1 }}>
                            {totalActual.toLocaleString('vi-VN')}
                            <span style={{ fontSize: 16, fontWeight: 400, color: 'var(--text-muted)', marginLeft: 6 }}>kg</span>
                        </div>
                    </div>
                    <div style={{ textAlign: 'right' }}>
                        <div style={{ fontSize: 11, color: 'var(--text-muted)', marginBottom: 4 }}>Muc tieu</div>
                        <div style={{ fontSize: 22, fontWeight: 700, color: 'var(--text-secondary)' }}>{totalTarget.toLocaleString('vi-VN')} kg</div>
                    </div>
                </div>
                <ProgressBar value={completionRate} max={100} color={completionRate >= 100 ? '#10b981' : completionRate >= 80 ? '#f59e0b' : '#ef4444'} height={12} />
                <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 10, fontSize: 13 }}>
                    <span style={{ fontWeight: 700, color: completionRate >= 100 ? '#10b981' : '#ef4444' }}>{completionRate.toFixed(1)}%</span>
                    <span style={{ color: 'var(--text-muted)' }}>Con <strong style={{ color: 'var(--text-primary)' }}>{remaining.toLocaleString('vi-VN')} kg</strong></span>
                </div>
            </div>

            {/* KPI Pills */}
            <div style={{ display: 'flex', gap: 12, marginBottom: 20, flexWrap: 'wrap' }}>
                <MetricPill label="Dang lam" value={board?.totalWorkers || 0} unit=" nguoi" color="#3b82f6" />

```
