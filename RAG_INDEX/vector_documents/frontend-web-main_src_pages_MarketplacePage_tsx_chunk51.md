# Knowledge Document: MarketplacePage.tsx (Chunk 52/70)

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
  "chunk_index": 51,
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
                            </>
                        )}
                    </div>
                </div>
            )}

            {selectedFactory && (
                <div className="mp-modal-overlay" onClick={() => setSelectedFactory(null)}>
                    <div className="mp-workshop-detail mp-profile-detail" onClick={event => event.stopPropagation()}>
                        <button className="mp-detail-close" onClick={() => setSelectedFactory(null)}>
                            <span className="material-symbols-outlined">close</span>
                        </button>
                        <aside className="mp-profile-side">
                            <span className={`mp-availability ${availabilityCopy(selectedFactory.availabilityStatus).className}`}>
                                {availabilityCopy(selectedFactory.availabilityStatus).label}
                            </span>
                            {(selectedFactory.factoryImages && selectedFactory.factoryImages.length > 0) ? (
                                <div className="mp-profile-gallery" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(80px, 1fr))', gap: '8px', marginBottom: '16px' }}>
                                    {selectedFactory.factoryImages.map((img, i) => (
                                        <img
                                            key={i}
                                            src={img}
                                            alt={`Ảnh ${i}`}
                                            style={{ width: '100%', height: '80px', objectFit: 'cover', borderRadius: '8px', border: '1px solid var(--border)' }}
                                            onError={handleFactoryImageError}
                                        />
                                    ))}
                                </div>
                            ) : (
                                <div className="mp-profile-image">
                                    <img
                                        src={getFactoryCardImage(selectedFactory)}
                                        alt={`Ảnh xưởng ${selectedFactory.name}`}
                                        onError={handleFactoryImageError}
                                    />
                                </div>
                            )}

```
