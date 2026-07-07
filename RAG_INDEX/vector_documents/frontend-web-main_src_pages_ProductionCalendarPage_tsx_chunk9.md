# Knowledge Document: ProductionCalendarPage.tsx (Chunk 10/12)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProductionCalendarPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 9,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
                             {day?.totalWorkers || 0} nguoi
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Don hang table */}
            {calendar.length > 0 && (
                <div style={{ marginTop: 32 }}>
                    <h2 style={{ fontSize: 16, fontWeight: 700, marginBottom: 12, color: 'var(--text-primary)' }}>Tong hop don hang trong tuan</h2>
                    <div style={{ overflowX: 'auto' }}>
                        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13, background: 'var(--bg-card)', borderRadius: 14, overflow: 'hidden', border: '1px solid var(--border)' }}>
                            <thead>
                                <tr style={{ background: 'var(--bg-input)' }}>
                                    {['Don hang', 'Khach hang', 'San luong', 'Da xong', 'Con lai', 'Tien do', 'Rui ro'].map(h => (
                                        <th key={h} style={{ padding: '12px 16px', textAlign: 'left', color: 'var(--text-muted)', fontWeight: 600, borderBottom: '1px solid var(--border)' }}>{h}</th>
                                    ))}
                                </tr>
                            </thead>
                            <tbody>
                                {calendar.flatMap((day: any) => day?.orderRows || []).filter((v: any, i: number, arr: any[]) =>
                                    arr.findIndex((r: any) => r.orderId === v.orderId) === i
                                ).map((row: any) => {
                                    const riskColors: Record<string, { bg: string; color: string }> = {
                                        NONE: { bg: '#dcfce7', color: '#16a34a' },
                                        LOW: { bg: '#dcfce7', color: '#16a34a' },
                                        MEDIUM: { bg: '#fef3c7', color: '#d97706' },
                                        HIGH: { bg: '#fee2e2', color: '#dc2626' },
                                        CRITICAL: { bg: '#dc2626', color: '#fff' },
                                    };

```
