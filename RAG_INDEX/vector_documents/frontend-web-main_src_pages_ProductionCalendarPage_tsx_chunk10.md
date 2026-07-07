# Knowledge Document: ProductionCalendarPage.tsx (Chunk 11/12)

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
  "chunk_index": 10,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
fce7', color: '#16a34a' },
                                        LOW: { bg: '#dcfce7', color: '#16a34a' },
                                        MEDIUM: { bg: '#fef3c7', color: '#d97706' },
                                        HIGH: { bg: '#fee2e2', color: '#dc2626' },
                                        CRITICAL: { bg: '#dc2626', color: '#fff' },
                                    };
                                    const risk = riskColors[row.riskLevel] || riskColors.LOW;
                                    return (
                                        <tr key={row.orderId} style={{ borderBottom: '1px solid var(--border)' }}>
                                            <td style={{ padding: '12px 16px' }}>
                                                <div style={{ fontWeight: 700, color: '#8b5cf6', fontSize: 12 }}>{row.orderCode}</div>
                                                <div style={{ fontWeight: 600 }}>{row.title}</div>
                                            </td>
                                            <td style={{ padding: '12px 16px', color: 'var(--text-secondary)' }}>{row.customerName || '-'}</td>
                                            <td style={{ padding: '12px 16px', fontWeight: 600 }}>{row.outputTarget?.toLocaleString('vi-VN')} kg</td>
                                            <td style={{ padding: '12px 16px', color: '#10b981', fontWeight: 700 }}>{row.completedQuantity?.toLocaleString('vi-VN')} kg</td>
                                            <td style={{ padding: '12px 16px', color: '#ef4444', fontWeight: 600 }}>{row.remainingQuantity?.toLocaleString('vi-VN')} kg</td>
                                            <td style={{ padding: '12px 16px' }}>
                                                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                                    <div style={{ width: 60, background: 'var(--bg-input)', borderRadius: 4, height: 6 }}>
                                                        <div style={{ width: `${row.progressPercent}%`, height: '100%', background: '#10b981', borderRadius: 4 }} />
                                                    </div>
                                                    <span style={{ fontWeight: 700, color: '#10b981', fontSize: 12 }}>{row.progressPercent?.toFixed(0)}%</span>

```
