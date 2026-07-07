# Knowledge Document: MarketplacePage.tsx (Chunk 51/70)

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
  "chunk_index": 50,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
ories?.length > 0 ? selectedProduct.factories.map((factory: MarketplaceFactory) => (
                                        <div key={factory.id} style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid rgba(255, 255, 255, 0.08)', padding: 14, borderRadius: 10, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                                            <div>
                                                <p style={{ margin: '0 0 4px', color: '#ece8e1', fontWeight: 600, fontSize: 14 }}>{factory.name}</p>
                                                <p style={{ margin: 0, color: '#a79d94', fontSize: 12 }}>{displayText(factory.region)} • {factory.factoryType || 'Đối tác ORCA'}</p>
                                            </div>
                                            <button type="button" style={{ background: '#d4a574', color: '#fff', border: 'none', borderRadius: 8, padding: '8px 14px', fontSize: 12, fontWeight: 700, cursor: 'pointer' }} onClick={() => {
                                                setSelectedProduct(null);
                                                handleOrderClick(factory);
                                            }}>
                                                Gửi RFQ
                                            </button>
                                        </div>
                                    )) : (
                                        <div style={{ padding: 20, textAlign: 'center', color: '#8f8580' }}>Không tìm thấy xưởng gia công phù hợp</div>
                                    )}
                                </div>
                                <div className="mp-modal-actions" style={{ display: 'flex', gap: 12 }}>
                                    <button type="button" className="mp-cancel-btn" onClick={() => setShowProductFactories(false)} style={{ flex: 1 }}>Quay lại</button>
                                </div>
                            </>
                        )}
                    </div>
                </div>
            )}

            {selectedFactory && (
                <div className="mp-modal-overlay" onClick={() => setSelectedFactory(null)}>
                    <div className="mp-workshop-detail mp-profile-detail" onClick={event => event.stopPropagation()}>

```
