# Knowledge Document: FactoryDashboardPage.tsx (Chunk 7/14)

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
  "chunk_index": 6,
  "total_chunks": 14
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: attendance, dashboard, production, factory, chat

## Source Code Chunk
```tsx
                                    <a href={`tel:${order.recipientPhone}`} style={{ display: 'flex', alignItems: 'center', gap: 4, fontSize: 11, color: '#10b981', fontWeight: 600, textDecoration: 'none' }}>
                                                Gọi ngay
                                            </a>
                                        )}
                                    </div>
                                )}
                                {order.shippingNote && (
                                    <div style={{ fontSize: 11, color: 'var(--text-muted)', marginTop: 4, fontStyle: 'italic' }}>
                                        Ghi chu: {order.shippingNote}
                                    </div>
                                )}
                            </div>
                        ))}
                    </div>
                )}
            </div>

            {/* Section B: Hom nay */}
            <div style={{ marginBottom: 32 }}>
                <h2 style={{ fontSize: 16, fontWeight: 700, marginBottom: 12, color: 'var(--text-primary)' }}>
                    San xuat hom nay
                </h2>
                <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border)', borderRadius: 14, padding: 20 }}>
                    {!todayTarget.id ? (
                        <div style={{ color: 'var(--text-muted)', textAlign: 'center', fontSize: 13 }}>
                            Hom nay chua co muc tieu nao duoc dat
                        </div>
                    ) : (
                        <>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 24, marginBottom: 20 }}>
                                <div style={{ position: 'relative', width: 100, height: 100 }}>
                                    <svg viewBox="0 0 100 100" style={{ transform: 'rotate(-90deg)' }}>
                                        <circle cx="50" cy="50" r="42" fill="none" stroke="var(--border)" strokeWidth="8" />
                                        <circle cx="50" cy="50" r="42" fill="none" stroke={progressColor} strokeWidth="8"
                                            strokeDasharray={`${completionRate * 2.64} 264`} strokeLinecap="round" />
                                    </svg>

```
