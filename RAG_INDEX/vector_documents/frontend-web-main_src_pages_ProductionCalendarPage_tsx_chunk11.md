# Knowledge Document: ProductionCalendarPage.tsx (Chunk 12/12)

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
  "chunk_index": 11,
  "total_chunks": 12
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
, height: 6 }}>
                                                        <div style={{ width: `${row.progressPercent}%`, height: '100%', background: '#10b981', borderRadius: 4 }} />
                                                    </div>
                                                    <span style={{ fontWeight: 700, color: '#10b981', fontSize: 12 }}>{row.progressPercent?.toFixed(0)}%</span>
                                                </div>
                                            </td>
                                            <td style={{ padding: '12px 16px' }}>
                                                {row.riskLevel !== 'NONE' && (
                                                    <span style={{ fontSize: 11, fontWeight: 700, padding: '2px 8px', borderRadius: 4, background: risk.bg, color: risk.color }}>
                                                        {row.riskLevel}
                                                    </span>
                                                )}
                                                {row.riskLevel === 'NONE' && <span style={{ color: '#10b981', fontSize: 12 }}>On dinh</span>}
                                            </td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    </div>
                </div>
            )}
        </div>
    );
}

```
