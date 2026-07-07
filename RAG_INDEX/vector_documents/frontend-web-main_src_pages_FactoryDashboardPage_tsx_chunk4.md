# Knowledge Document: FactoryDashboardPage.tsx (Chunk 5/14)

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
  "chunk_index": 4,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
                                                   o.id === order.id ? { ...o, progressPercent: val } : o
                                                    ),
                                                }));
                                            }}
                                            onMouseUp={(e) => updateOrderProgress(order.id, Number((e.target as HTMLInputElement).value))}
                                            onTouchEnd={(e) => updateOrderProgress(order.id, Number((e.target as HTMLInputElement).value))}
                                            disabled={updatingProgress === order.id}
                                            style={{
                                                flex: 1,
                                                accentColor: order.isAtRisk ? '#ef4444' : '#10b981',
                                                cursor: 'pointer',
                                                height: 4,
                                            }}
                                        />
                                        {updatingProgress === order.id && (
                                            <ion-icon name="sync" style={{ fontSize: 14, color: 'var(--text-muted)', animation: 'spin 1s linear infinite' }} />
                                        )}
                                    </div>
                                </div>
                                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12 }}>
                                    <span style={{ color: 'var(--text-muted)' }}>Con lai</span>
                                    <span style={{ fontWeight: 600, color: '#ef4444' }}>{((order.remainingQuantity || 0)).toLocaleString('vi-VN')} kg</span>
                                </div>
                                {order.internalDeadline && (
                                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12, marginTop: 4 }}>
                                        <span style={{ color: 'var(--text-muted)' }}>Han noi bo</span>
                                        <span style={{ fontWeight: 600, color: 'var(--text-primary)' }}>
                                            {new Date(order.internalDeadline).toLocaleDateString('vi-VN')}
                                        </span>

```
