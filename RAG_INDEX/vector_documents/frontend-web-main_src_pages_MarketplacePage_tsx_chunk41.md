# Knowledge Document: MarketplacePage.tsx (Chunk 42/70)

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
  "chunk_index": 41,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
                <div style={{display: 'flex', justifyContent: 'space-between'}}>
                                                    <span style={{color: 'var(--text-muted)'}}>{t.availableCapacity}</span>
                                                    <strong style={{color: 'var(--text-primary)'}}>{factory.availableCapacityMock}</strong>
                                                </div>
                                                <div style={{display: 'flex', justifyContent: 'space-between'}}>
                                                    <span style={{color: 'var(--text-muted)'}}>{t.moq}</span>
                                                    <strong style={{color: 'var(--text-primary)'}}>{factory.moqMock}</strong>
                                                </div>
                                                <div style={{display: 'flex', justifyContent: 'space-between'}}>
                                                    <span style={{color: 'var(--text-muted)'}}>{t.leadTime}</span>
                                                    <strong style={{color: 'var(--text-primary)'}}>{factory.leadTimeMock?.replace('Ngày', language === 'en' ? 'Days' : 'Ngày')}</strong>
                                                </div>
                                            </div>
                                        </div>
                                        <div className="mp-factory-actions" style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, padding: '0 16px 16px', marginTop: 'auto'}}>
                                            {isOwnFactory ? (
                                                <button onClick={() => openEditPublishedTeam(factory)} style={{gridColumn: '1 / -1', background: 'var(--bg-input)', color: 'var(--text-primary)', padding: '8px', borderRadius: 8, border: 'none', cursor: 'pointer', fontWeight: 600, height: 38}}>{t.manageFactory}</button>
                                            ) : (
                                                <>

```
