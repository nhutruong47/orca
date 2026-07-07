# Knowledge Document: MarketplacePage.tsx (Chunk 47/70)

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
  "chunk_index": 46,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
                             </dl>
                                    <p>{request.details || 'Chưa cập nhật yêu cầu chi tiết'}</p>
                                </article>
                            ))}
                        </div>
                    )}
                </section>

                <section className="mp-cta">
                    <h2>Sẵn sàng đưa xưởng của bạn lên ORCA?</h2>
                    <p>Gia nhập cộng đồng xưởng rang lớn nhất Việt Nam. Quản lý bán hàng, tiếp cận khách hàng B2B và tối ưu hóa vận hành chỉ trong một nền tảng.</p>
                    <button onClick={openPublishModal}>Đăng ký trở thành Đối tác</button>
                    <small>Hơn 50 xưởng rang đã tin tưởng sử dụng</small>
                </section>

                <footer className="mp-showcase-footer">
                    <span>ORCA</span>
                    <p>© 2026 Coffee Workshop Ecosystem</p>
                    <div>
                        <a href="#">Điều khoản</a>
                        <a href="#">Hỗ trợ đối tác</a>
                    </div>
                </footer>
            </main>

            {selectedProduct && (
                <div className="mp-modal-overlay" onClick={() => setSelectedProduct(null)}>
                    <div className="mp-modal" onClick={event => event.stopPropagation()} style={{ maxWidth: 800 }}>
                        <div className="mp-modal-header">
                            <h2>{showProductFactories ? 'Xưởng nhận gia công' : 'Chi tiết sản phẩm'}</h2>
                            <button className="mp-modal-close" onClick={() => setSelectedProduct(null)}>×</button>
                        </div>

                        {!showProductFactories ? (
                            <>
                                <div style={{ display: 'flex', gap: 32, marginBottom: 24, marginTop: 10 }}>
                                    <div style={{ flex: '0 0 300px' }}>
                                        <img src={selectedProduct.imageUrl} alt={selectedProduct.name} style={{ width: '100%', height: 300, objectFit: 'cover', borderRadius: 12, background: '#171a1b', border: '1px solid rgba(255,255,255,0.1)' }} />
                                    </div>
                                    <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>

```
