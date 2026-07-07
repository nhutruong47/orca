# Knowledge Document: FactoryDashboardPage.tsx (Chunk 10/14)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/FactoryDashboardPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "attendance",
  "tags": [
    "attendance",
    "dashboard",
    "production",
    "factory",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 9,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
     const actual = todayTarget[row.actual] || 0;
                                        const diff = actual - target;
                                        return (
                                            <tr key={row.key} style={{ borderBottom: '1px solid var(--border)' }}>
                                                <td style={{ padding: '10px 0', fontWeight: 600 }}>{row.label}</td>
                                                <td style={{ padding: '10px 0', textAlign: 'right' }}>{target.toLocaleString('vi-VN')} kg</td>
                                                <td style={{ padding: '10px 0', textAlign: 'right', color: '#10b981', fontWeight: 600 }}>{actual.toLocaleString('vi-VN')} kg</td>
                                                <td style={{ padding: '10px 0', textAlign: 'right', color: diff >= 0 ? '#10b981' : '#ef4444', fontWeight: 600 }}>
                                                    {diff >= 0 ? '+' : ''}{diff.toLocaleString('vi-VN')} kg
                                                </td>
                                            </tr>
                                        );
                                    })}
                                </tbody>
                            </table>
                            {todayTarget.productivityKgPerHour && (
                                <div style={{ marginTop: 12, display: 'flex', gap: 16, fontSize: 13 }}>
                                    <span style={{ color: 'var(--text-secondary)' }}>Nang suat: <strong style={{ color: 'var(--text-primary)' }}>{todayTarget.productivityKgPerHour} kg/gio</strong></span>
                                    <span style={{ color: 'var(--text-secondary)' }}>Tong gio cong: <strong style={{ color: 'var(--text-primary)' }}>{(todayTarget.totalWorkerHours || 0).toFixed(1)} gio</strong></span>
                                </div>
                            )}
                        </>
                    )}
                </div>
            </div>

            {/* Section C: Nhan su */}
            <div style={{ marginBottom: 32 }}>
                <h2 style={{ fontSize: 16, fontWeight: 700, marginBottom: 12, color: 'var(--text-primary)' }}>
                    Nhan su hom nay ({dashboard.staffToday})
                </h2>

```
