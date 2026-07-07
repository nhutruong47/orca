# Knowledge Document: MarketplacePage.tsx (Chunk 40/70)

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
  "chunk_index": 39,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
s-outlined verified-icon" title={t.verifiedFactory} style={{fontSize: 16, color: '#10b981'}}>verified</span>}</h3>
                                                <span className="mp-fcard-location"><span className="material-symbols-outlined" style={{fontSize: 14}}>location_on</span> {t[factory.region || ''] || factory.region || t.vietnam}</span>
                                            </div>
                                            <div className="mp-fcard-type" style={{color: 'var(--text-muted)', fontSize: 13, marginBottom: 8}}>
                                                {t[factory.factoryType || ''] || factory.factoryType || t.roastery} • {factory.yearsInOperationMock} {t.yearsInOperation}
                                            </div>
                                            <div className="mp-fcard-tags" style={{display: 'flex', gap: 6, flexWrap: 'wrap', marginBottom: 16}}>
                                                {factory.specializationsMock?.slice(0, 3).map(tag => (
                                                    <span key={tag} style={{background: 'rgba(255,255,255,0.05)', padding: '4px 8px', borderRadius: 4, fontSize: 12, border: '1px solid rgba(255,255,255,0.1)'}}>{t[tag.replace(' ', '_')] || tag}</span>
                                                ))}
                                            </div>
                                            <div className="mp-fcard-metrics" style={{display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 8, marginBottom: 16, padding: '12px 0', borderTop: '1px solid var(--border)', borderBottom: '1px solid var(--border)'}}>
                                                <div className="mp-metric" style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4}}>
                                                    <span style={{fontSize: 14, fontWeight: 600, color: '#10b981'}}>{factory.trustScoreMock}</span>
                                                    <span style={{fontSize: 11, color: 'var(--text-muted)'}}>{t.trustScore}</span>
                                                </div>
                                                <div className="mp-metric" style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4}}>

```
