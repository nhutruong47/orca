# Knowledge Document: ProductivityAnalyticsPage.tsx (Chunk 12/12)

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
  "chunk_index": 11,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, production

## Source Code Chunk
```tsx
Target || 0).toLocaleString('vi-VN')} kg</td>
                                            <td style={{ padding: '10px 12px', fontWeight: 700, color: '#10b981' }}>{(o.completedQuantity || 0).toLocaleString('vi-VN')} kg</td>
                                            <td style={{ padding: '10px 12px', color: '#ef4444', fontWeight: 600 }}>{(o.remainingQuantity || 0).toLocaleString('vi-VN')} kg</td>
                                            <td style={{ padding: '10px 12px' }}>
                                                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                                    <div style={{ width: 60, background: 'var(--bg-input)', borderRadius: 4, height: 6 }}>
                                                        <div style={{ width: `${o.progressPercent || 0}%`, height: '100%', background: '#10b981', borderRadius: 4 }} />
                                                    </div>
                                                    <span style={{ fontSize: 12, fontWeight: 700, color: '#10b981', minWidth: 36 }}>{(o.progressPercent || 0).toFixed(0)}%</span>
                                                </div>
                                            </td>
                                            <td style={{ padding: '10px 12px' }}>
                                                {o.riskLevel && o.riskLevel !== 'NONE' ? (
                                                    <span style={{ fontSize: 11, fontWeight: 700, padding: '3px 10px', borderRadius: 20, background: `${RISK_COLOR[o.riskLevel]}20`, color: RISK_COLOR[o.riskLevel] }}>
                                                        {o.riskLevel}
                                                    </span>
                                                ) : (
                                                    <span style={{ fontSize: 12, color: '#10b981' }}>On dinh</span>
                                                )}
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </SectionCard>
                </div>
            )}
        </div>
    );
}

```
