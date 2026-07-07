# Knowledge Document: MarketplacePage.tsx (Chunk 48/70)

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
  "chunk_index": 47,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
}}>
                                        <img src={selectedProduct.imageUrl} alt={selectedProduct.name} style={{ width: '100%', height: 300, objectFit: 'cover', borderRadius: 12, background: '#171a1b', border: '1px solid rgba(255,255,255,0.1)' }} />
                                    </div>
                                    <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                                        <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 12 }}>
                                            <h3 style={{ margin: 0, fontSize: 26, color: '#fff7ef' }}>{selectedProduct.name}</h3>
                                            {selectedProduct.status && <span style={{ background: '#d4a574', color: '#171a1b', padding: '4px 10px', borderRadius: 6, fontSize: 13, fontWeight: 700 }}>{selectedProduct.status}</span>}
                                        </div>
                                        <p style={{ margin: '0 0 20px', color: '#a79d94', fontSize: 15, lineHeight: 1.6 }}>{selectedProduct.description}</p>

                                        <div style={{ background: 'rgba(255,255,255,0.03)', padding: '16px 20px', borderRadius: 12, marginBottom: 20 }}>
                                            <div style={{ display: 'flex', alignItems: 'flex-end', gap: 6, marginBottom: 16 }}>
                                                <strong style={{ fontSize: 28, color: '#ffd9bd', lineHeight: 1 }}>{selectedProduct.price}</strong>
                                                <small style={{ color: '#a79d94', fontSize: 15, marginBottom: 2 }}>/{selectedProduct.unit}</small>
                                            </div>

                                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '14px 24px', fontSize: 14 }}>
                                                {selectedProduct.origin && <div style={{ display: 'flex', justifyContent: 'space-between' }}><span style={{ color: '#8f8580' }}>Xuất xứ:</span> <strong style={{ color: '#ece8e1', textAlign: 'right' }}>{selectedProduct.origin}</strong></div>}

```
