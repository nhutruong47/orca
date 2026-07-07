# Knowledge Document: MarketplacePage.tsx (Chunk 70/70)

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
  "chunk_index": 69,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
>
                                                <div>
                                                    <strong style={{display: 'block', color: '#ece8e1', marginBottom: 4}}>{matchFactory.name}</strong>
                                                    <span style={{fontSize: 12, color: '#a79d94'}}>Phù hợp Profile • Còn công suất</span>
                                                </div>
                                            </div>
                                            <span className="material-symbols-outlined" style={{color: '#d4a574'}}>chevron_right</span>
                                        </div>
                                    )})}
                                </div>

                                <div style={{display: 'flex', gap: 12}}>
                                    <button style={{flex: 1, padding: 14, background: '#d4a574', color: '#1a1a1a', borderRadius: 8, fontWeight: 600, border: 'none', cursor: 'pointer'}} onClick={() => { setShowAiMatching(false); navigate('/orders'); }}>Theo dõi RFQ</button>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            )}

        </div>
    );
}

```
