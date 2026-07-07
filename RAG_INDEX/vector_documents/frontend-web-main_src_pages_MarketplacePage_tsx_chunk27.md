# Knowledge Document: MarketplacePage.tsx (Chunk 28/70)

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
  "chunk_index": 27,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
        <div className="mp-detail-tags">
                                {factory.capabilitiesMock?.services.map(s => <span key={s}>{s}</span>)}
                            </div>
                        </div>
                        <div>
                            <h4 style={{marginBottom: '12px', color: '#d4a574'}}>Dòng cà phê</h4>
                            <div className="mp-detail-tags">
                                {factory.capabilitiesMock?.coffeeTypes.map(c => <span key={c}>{c}</span>)}
                            </div>
                        </div>
                        <div>
                            <h4 style={{marginBottom: '12px', color: '#d4a574'}}>Quy cách đóng gói</h4>
                            <div className="mp-detail-tags">
                                {factory.capabilitiesMock?.packagingFormats.map(p => <span key={p}>{p}</span>)}
                            </div>
                        </div>
                    </div>
                );
            case 'equipment':
                return (
                    <div className="mp-profile-overview" style={{display: 'flex', flexDirection: 'column', gap: '24px'}}>
                        <div>
                            <h4 style={{marginBottom: '12px', color: '#d4a574'}}>Máy rang</h4>
                            <div style={{display: 'flex', flexDirection: 'column', gap: '8px'}}>
                                {factory.equipmentMock?.roasters.map(r => (
                                    <div key={r.model} style={{display: 'flex', justifyContent: 'space-between', padding: '12px', background: 'rgba(255,255,255,0.03)', borderRadius: '8px', border: '1px solid rgba(255,255,255,0.05)'}}>
                                        <strong style={{color: '#ece8e1'}}>{r.model}</strong>
                                        <span style={{color: '#a79d94'}}>{r.capacity} • Đời {r.year}</span>
                                    </div>
                                ))}
                            </div>
                        </div>
                        <div>
                            <h4 style={{marginBottom: '12px', color: '#d4a574'}}>Máy đóng gói & Xay</h4>
                            <ul style={{color: '#a79d94', paddingLeft: '20px', lineHeight: '1.8'}}>
                                {factory.equipmentMock?.packaging.map(p => <li key={p}>{p}</li>)}

```
