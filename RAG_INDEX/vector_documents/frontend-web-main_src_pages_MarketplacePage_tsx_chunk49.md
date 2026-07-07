# Knowledge Document: MarketplacePage.tsx (Chunk 50/70)

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
  "chunk_index": 49,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
s.split(',').map((note: string) => note.trim()).map((note: string) => (
                                                        <span key={note} style={{ background: 'rgba(212, 165, 116, 0.1)', color: '#d4a574', padding: '6px 14px', borderRadius: 20, fontSize: 13, fontWeight: 500, border: '1px solid rgba(212, 165, 116, 0.2)' }}>{note}</span>
                                                    ))}
                                                </div>
                                            </div>
                                        )}
                                    </div>
                                </div>

                                <div className="mp-modal-actions" style={{ display: 'flex', gap: 12, marginTop: 'auto' }}>
                                    <button type="button" className="mp-cancel-btn" onClick={() => setSelectedProduct(null)} style={{ flex: 1, padding: '14px', fontSize: 15, fontWeight: 600 }}>Đóng</button>
                                    <button type="button" className="mp-submit-btn" style={{ flex: 2, padding: '14px', fontSize: 15, fontWeight: 600 }} onClick={() => setShowProductFactories(true)}>
                                        Tìm xưởng gia công
                                    </button>
                                </div>
                            </>
                        ) : (
                            <>
                                <p style={{ margin: '10px 0 20px', color: '#a79d94', fontSize: 13, lineHeight: 1.5 }}>
                                    Các xưởng sau có năng lực và sẵn sàng gia công <strong>{selectedProduct.name}</strong>.
                                </p>
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 12, maxHeight: 300, overflowY: 'auto', marginBottom: 24, paddingRight: 8 }}>
                                    {selectedProduct.factories?.length > 0 ? selectedProduct.factories.map((factory: MarketplaceFactory) => (
                                        <div key={factory.id} style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid rgba(255, 255, 255, 0.08)', padding: 14, borderRadius: 10, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                                            <div>

```
