# Knowledge Document: MarketplacePage.tsx (Chunk 41/70)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/MarketplacePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "notification",
    "factory",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 40,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
 600, color: '#10b981'}}>{factory.trustScoreMock}</span>
                                                    <span style={{fontSize: 11, color: 'var(--text-muted)'}}>{t.trustScore}</span>
                                                </div>
                                                <div className="mp-metric" style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4}}>
                                                    <span style={{fontSize: 14, fontWeight: 600, color: '#f59e0b'}}>{factory.ratingMock?.toFixed(1)}★</span>
                                                    <span style={{fontSize: 11, color: 'var(--text-muted)'}}>{t.rating} ({factory.reviewCountMock})</span>
                                                </div>
                                                <div className="mp-metric" style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4}}>
                                                    <span style={{fontSize: 14, fontWeight: 600}}>{factory.completedOrdersMock}</span>
                                                    <span style={{fontSize: 11, color: 'var(--text-muted)'}}>{t.orders}</span>
                                                </div>
                                                <div className="mp-metric" style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4}}>
                                                    <span style={{fontSize: 14, fontWeight: 600}}>{factory.onTimeRateMock}%</span>
                                                    <span style={{fontSize: 11, color: 'var(--text-muted)'}}>{t.onTime}</span>
                                                </div>
                                            </div>
                                            <div className="mp-fcard-capacity" style={{display: 'flex', flexDirection: 'column', gap: 8, fontSize: 13, marginBottom: 16}}>
                                                <div style={{display: 'flex', justifyContent: 'space-between'}}>
                                                    <span style={{color: 'var(--text-muted)'}}>{t.availableCapacity}</span>
                                                    <strong style={{color: 'var(--text-primary)'}}>{factory.availableCapacityMock}</strong>
                                                </div>

```
