# Knowledge Document: MarketplacePage.tsx (Chunk 43/70)

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
  "chunk_index": 42,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
                            <button onClick={() => openEditPublishedTeam(factory)} style={{gridColumn: '1 / -1', background: 'var(--bg-input)', color: 'var(--text-primary)', padding: '8px', borderRadius: 8, border: 'none', cursor: 'pointer', fontWeight: 600, height: 38}}>{t.manageFactory}</button>
                                            ) : (
                                                <>
                                                    <button onClick={() => { setSelectedFactory(factory); setActiveProfileTab('overview'); }} style={{background: 'var(--bg-input)', color: 'var(--text-primary)', padding: '8px', borderRadius: 8, border: 'none', cursor: 'pointer', fontWeight: 600, height: 38, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>{t.viewCapacity}</button>
                                                    <button onClick={() => { const fact = factory; handleOrderClick(fact); }} style={{background: '#d4a574', color: '#1a1a1a', padding: '8px', borderRadius: 8, border: 'none', cursor: 'pointer', fontWeight: 600, height: 38, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>{t.sendRequest}</button>
                                                </>
                                            )}
                                        </div>
                                    </article>
                                );
                            })}
                        </div>
                    )}
                    {totalPages > 1 && (
                        <div className="mp-pagination">
                            <button disabled={currentPage === 1} onClick={() => setCurrentPage(p => Math.max(1, p - 1))}>
                                <span className="material-symbols-outlined" style={{ fontSize: 18 }}>chevron_left</span> Trước
                            </button>
                            <span className="mp-page-info">Trang {currentPage} / {totalPages}</span>
                            <button disabled={currentPage === totalPages} onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))}>
                                Sau <span className="material-symbols-outlined" style={{ fontSize: 18 }}>chevron_right</span>
                            </button>
                        </div>
                    )}
                </section>


```
