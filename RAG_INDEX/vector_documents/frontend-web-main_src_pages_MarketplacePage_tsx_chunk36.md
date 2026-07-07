# Knowledge Document: MarketplacePage.tsx (Chunk 37/70)

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
  "chunk_index": 36,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
egory.label}
                        </button>
                    ))}
                    <div className="mp-top-search mp-spotlight-search" style={{marginLeft: 'auto'}}>
                        <span className="material-symbols-outlined">search</span>
                        <input
                            type="text"
                            placeholder="Tìm hạt, xưởng, hoặc thiết bị..."
                            value={searchQuery}
                            onChange={event => setSearchQuery(event.target.value)}
                            style={{ height: '38px', borderRadius: '10px' }}
                        />
                    </div>
                </section>

                {myPublishedTeams.length > 0 && (
                    <section className="mp-published-panel">
                        <h3><span className="material-symbols-outlined">storefront</span>Xưởng của bạn trên thị trường</h3>
                        <div className="mp-my-published-list">
                            {myPublishedTeams.map(team => (
                                <div key={team.id} className="mp-my-pub-item">
                                    <div>
                                        <strong>{team.name}</strong>
                                        <span className="mp-pub-badge">Đang hiển thị</span>
                                    </div>
                                    <button className="mp-edit-pub-btn" onClick={() => openEditPublishedTeam(team)}>Chỉnh sửa</button>
                                    <button className="mp-unpub-btn" onClick={() => handleUnpublish(team.id)}>Gỡ xuống</button>
                                </div>
                            ))}
                        </div>
                    </section>
                )}

                <section id="mp-partners" className="mp-partner-section">
                    <div className="mp-section-title-row">
                        <div>
                            <h2>Xưởng Đối Tác</h2>
                            <p>Những đơn vị rang uy tín hàng đầu trong mạng lưới ORCA</p>
                        </div>
                        <div style={{ display: 'flex', gap: 12 }}>
                            <select
                                value={minRatingFilter}
                                onChange={e => setMinRatingFilter(e.target.value)}

```
