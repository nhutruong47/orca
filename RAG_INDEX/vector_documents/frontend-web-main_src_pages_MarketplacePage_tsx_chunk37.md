# Knowledge Document: MarketplacePage.tsx (Chunk 38/70)

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
  "chunk_index": 37,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
              <h2>Xưởng Đối Tác</h2>
                            <p>Những đơn vị rang uy tín hàng đầu trong mạng lưới ORCA</p>
                        </div>
                        <div style={{ display: 'flex', gap: 12 }}>
                            <select
                                value={minRatingFilter}
                                onChange={e => setMinRatingFilter(e.target.value)}
                                className="mp-filter-select"
                                style={{
                                    padding: '8px 12px',
                                    borderRadius: '8px',
                                    border: '1px solid var(--border)',
                                    background: 'var(--bg-secondary)',
                                    color: 'var(--text-primary)',
                                    fontSize: '13px',
                                    fontWeight: 600,
                                    outline: 'none',
                                    cursor: 'pointer'
                                }}
                            >
                                <option value="">Tất cả số sao</option>
                                <option value="5">5 Sao</option>
                                <option value="4">Từ 4 Sao</option>
                                <option value="3">Từ 3 Sao</option>
                                <option value="2">Từ 2 Sao</option>
                                <option value="1">Từ 1 Sao</option>
                                <option value="0">Từ 0 Sao</option>
                            </select>
                        </div>
                    </div>

                    {error && <div className="mp-error">{error}</div>}

                    {displayedFactories.length === 0 ? (
                        <div className="mp-empty mp-styled-empty">
                            <span className="material-symbols-outlined">factory</span>
                            <h3>Chưa có xưởng đối tác</h3>
                            <p>Đăng xưởng của bạn để bắt đầu nhận yêu cầu gia công và hiển thị trong mạng lưới ORCA.</p>
                            <button className="mp-publish-btn" onClick={openPublishModal}>Đăng xưởng ngay</button>
                        </div>
                    ) : (
                        <div className="mp-factory-grid">

```
