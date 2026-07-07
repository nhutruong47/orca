# Knowledge Document: FactoryDashboardPage.tsx (Chunk 8/14)

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
  "chunk_index": 7,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
                                <circle cx="50" cy="50" r="42" fill="none" stroke="var(--border)" strokeWidth="8" />
                                        <circle cx="50" cy="50" r="42" fill="none" stroke={progressColor} strokeWidth="8"
                                            strokeDasharray={`${completionRate * 2.64} 264`} strokeLinecap="round" />
                                    </svg>
                                    <div style={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', textAlign: 'center' }}>
                                        <div style={{ fontSize: 20, fontWeight: 800, color: progressColor }}>{completionRate.toFixed(0)}%</div>
                                        <div style={{ fontSize: 9, color: 'var(--text-muted)' }}>hoan thanh</div>
                                    </div>
                                </div>
                                <div style={{ flex: 1 }}>
                                    <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8 }}>
                                        <span style={{ color: 'var(--text-secondary)', fontSize: 13 }}>Muc tieu</span>
                                        <span style={{ fontWeight: 700, fontSize: 15 }}>{(todayTarget.targetQuantityKg || 0).toLocaleString('vi-VN')} kg</span>
                                    </div>
                                    <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8 }}>
                                        <span style={{ color: 'var(--text-secondary)', fontSize: 13 }}>Thuc te</span>
                                        <span style={{ fontWeight: 700, fontSize: 15, color: '#10b981' }}>{(todayTarget.totalActualKg || 0).toLocaleString('vi-VN')} kg</span>
                                    </div>
                                    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                        <span style={{ color: 'var(--text-secondary)', fontSize: 13 }}>Con lai</span>
                                        <span style={{ fontWeight: 700, fontSize: 15, color: '#ef4444' }}>{Math.max(0, (todayTarget.targetQuantityKg || 0) - (todayTarget.totalActualKg || 0)).toLocaleString('vi-VN')} kg</span>
                                    </div>
                                </div>

```
