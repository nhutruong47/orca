# Knowledge Document: MarketplacePage.tsx (Chunk 49/70)

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
  "chunk_index": 48,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '14px 24px', fontSize: 14 }}>
                                                {selectedProduct.origin && <div style={{ display: 'flex', justifyContent: 'space-between' }}><span style={{ color: '#8f8580' }}>Xuất xứ:</span> <strong style={{ color: '#ece8e1', textAlign: 'right' }}>{selectedProduct.origin}</strong></div>}
                                                {selectedProduct.processing && <div style={{ display: 'flex', justifyContent: 'space-between' }}><span style={{ color: '#8f8580' }}>Sơ chế:</span> <strong style={{ color: '#ece8e1', textAlign: 'right' }}>{selectedProduct.processing}</strong></div>}
                                                {selectedProduct.roastLevel && <div style={{ display: 'flex', justifyContent: 'space-between' }}><span style={{ color: '#8f8580' }}>Mức rang:</span> <strong style={{ color: '#ece8e1', textAlign: 'right' }}>{selectedProduct.roastLevel}</strong></div>}
                                                {selectedProduct.quantity > 0 && <div style={{ display: 'flex', justifyContent: 'space-between' }}><span style={{ color: '#8f8580' }}>Tình trạng:</span> <strong style={{ color: '#5cb85c', textAlign: 'right' }}>Có sẵn ({selectedProduct.quantity}+ {selectedProduct.unit})</strong></div>}
                                            </div>
                                        </div>

                                        {selectedProduct.tasteNotes && selectedProduct.tasteNotes.trim() !== '' && (
                                            <div style={{ marginBottom: 20 }}>
                                                <strong style={{ display: 'block', marginBottom: 12, color: '#ece8e1', fontSize: 14 }}>Hương vị nổi bật (Taste Notes):</strong>
                                                <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
                                                    {selectedProduct.tasteNotes.split(',').map((note: string) => note.trim()).map((note: string) => (
                                                        <span key={note} style={{ background: 'rgba(212, 165, 116, 0.1)', color: '#d4a574', padding: '6px 14px', borderRadius: 20, fontSize: 13, fontWeight: 500, border: '1px solid rgba(212, 165, 116, 0.2)' }}>{note}</span>
                                                    ))}

```
