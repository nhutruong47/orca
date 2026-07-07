# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 10/12)

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
  "chunk_index": 9,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
 => (
                                            <th key={h} style={{ textAlign: 'right', padding: '10px 12px', color: 'var(--text-muted)', fontWeight: 600 }}>{h}</th>
                                        ))}
                                    </tr>
                                </thead>
                                <tbody>
                                    {stageEff.map((s: any) => {
                                        const colors: Record<string, string> = { 'Rang': '#d97706', 'QC': '#3b82f6', 'Dong goi': '#8b5cf6' };
                                        return (
                                            <tr key={s.stage} style={{ borderBottom: '1px solid var(--border)' }}>
                                                <td style={{ padding: '12px 12px', fontWeight: 700, color: colors[s.stage] || 'var(--text-primary)' }}>{s.stage}</td>
                                                <td style={{ padding: '12px 12px', textAlign: 'right', color: 'var(--text-secondary)' }}>{(s.totalTargetKg || 0).toLocaleString('vi-VN')}</td>
                                                <td style={{ padding: '12px 12px', textAlign: 'right', fontWeight: 700, color: '#10b981' }}>{(s.totalActualKg || 0).toLocaleString('vi-VN')}</td>
                                                <td style={{ padding: '12px 12px', textAlign: 'right' }}>
                                                    <span style={{ fontWeight: 700, color: (s.efficiency || 0) >= 100 ? '#10b981' : (s.efficiency || 0) >= 80 ? '#f59e0b' : '#ef4444' }}>
                                                        {(s.efficiency || 0).toFixed(1)}%
                                                    </span>
                                                </td>
                                                <td style={{ padding: '12px 12px', textAlign: 'right', fontWeight: 700, color: '#8b5cf6' }}>{(s.avgProductivity || 0).toFixed(2)}</td>
                                                <td style={{ padding: '12px 12px', textAlign: 'right', color: '#ef4444' }}>{(s.failRate || 0).toFixed(1)}%</td>
                                            </tr>
                                        );
                                    })}
                                </tbody>
                            </table>
                        </div>
                    </SectionCard>
                </div>

```
