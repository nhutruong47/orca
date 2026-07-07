# Knowledge Document: MarketplacePage.tsx (Chunk 29/70)

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
  "chunk_index": 28,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx

                            </div>
                        </div>
                        <div>
                            <h4 style={{marginBottom: '12px', color: '#d4a574'}}>Máy đóng gói & Xay</h4>
                            <ul style={{color: '#a79d94', paddingLeft: '20px', lineHeight: '1.8'}}>
                                {factory.equipmentMock?.packaging.map(p => <li key={p}>{p}</li>)}
                                {factory.equipmentMock?.grinders.map(p => <li key={p}>{p}</li>)}
                            </ul>
                        </div>
                        <div>
                            <h4 style={{marginBottom: '12px', color: '#d4a574'}}>Thiết bị kiểm định (QC)</h4>
                            <div className="mp-detail-tags">
                                {factory.equipmentMock?.qc.map(q => <span key={q} style={{background: 'transparent', border: '1px dashed #d4a574', color: '#d4a574'}}>{q}</span>)}
                            </div>
                        </div>
                    </div>
                );
            case 'certificates':
                return (
                    <div className="mp-profile-overview" style={{display: 'flex', flexDirection: 'column', gap: '16px'}}>
                        {renderVerification(factory)}
                        <div style={{display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '16px'}}>
                            {factory.certificatesMock?.map(cert => (
                                <div key={cert.name} style={{display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '16px', background: 'rgba(255,255,255,0.03)', borderRadius: '8px', border: '1px solid rgba(255,255,255,0.05)'}}>
                                    <div>
                                        <h4 style={{margin: '0 0 4px 0', color: '#ece8e1', fontSize: '15px'}}>{cert.name}</h4>
                                        <span style={{fontSize: '13px', color: '#a79d94'}}>Ngày cấp: {cert.issueDate} • Hết hạn: {cert.expDate}</span>
                                    </div>
                                    <span style={{color: '#10b981', display: 'flex', alignItems: 'center', gap: '4px', fontSize: '13px', fontWeight: 600}}>
                                        <span className="material-symbols-outlined" style={{fontSize: '16px'}}>verified</span> {cert.status}

```
