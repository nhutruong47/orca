# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 11/12)

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
  "chunk_index": 10,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
 padding: '12px 12px', textAlign: 'right', color: '#ef4444' }}>{(s.failRate || 0).toFixed(1)}%</td>
                                            </tr>
                                        );
                                    })}
                                </tbody>
                            </table>
                        </div>
                    </SectionCard>
                </div>
            )}

            {/* Don hang chi tiet */}
            {orderAnalytics.length > 0 && (
                <div>
                    <SectionCard title="Chi tiet Don hang">
                        <div style={{ overflowX: 'auto' }}>
                            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
                                <thead>
                                    <tr style={{ borderBottom: '1px solid var(--border)' }}>
                                        {['Don hang', 'San luong', 'Da xong', 'Con lai', 'Tien do', 'Rui ro'].map(h => (
                                            <th key={h} style={{ textAlign: 'left', padding: '10px 12px', color: 'var(--text-muted)', fontWeight: 600 }}>{h}</th>
                                        ))}
                                    </tr>
                                </thead>
                                <tbody>
                                    {orderAnalytics.map((o: any) => (
                                        <tr key={o.orderId} style={{ borderBottom: '1px solid var(--border)' }}>
                                            <td style={{ padding: '10px 12px' }}>
                                                <div style={{ fontSize: 11, fontWeight: 800, color: '#8b5cf6' }}>{o.orderCode}</div>
                                                <div style={{ fontWeight: 600, color: 'var(--text-primary)' }}>{o.title}</div>
                                            </td>
                                            <td style={{ padding: '10px 12px' }}>{(o.outputTarget || 0).toLocaleString('vi-VN')} kg</td>
                                            <td style={{ padding: '10px 12px', fontWeight: 700, color: '#10b981' }}>{(o.completedQuantity || 0).toLocaleString('vi-VN')} kg</td>
                                            <td style={{ padding: '10px 12px', color: '#ef4444', fontWeight: 600 }}>{(o.remainingQuantity || 0).toLocaleString('vi-VN')} kg</td>

```
