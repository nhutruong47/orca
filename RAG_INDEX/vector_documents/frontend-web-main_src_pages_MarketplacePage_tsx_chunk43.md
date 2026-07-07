# Knowledge Document: MarketplacePage.tsx (Chunk 44/70)

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
  "chunk_index": 43,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
Pages}</span>
                            <button disabled={currentPage === totalPages} onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))}>
                                Sau <span className="material-symbols-outlined" style={{ fontSize: 18 }}>chevron_right</span>
                            </button>
                        </div>
                    )}
                </section>

                <section id="mp-products" className="mp-product-section">
                    <div className="mp-section-title-row">
                        <div>
                            <h2>Sản phẩm Mới</h2>
                        </div>
                    </div>
                    <div className="mp-marquee-container">
                        <div className="mp-marquee-track">
                            {[...featuredProducts, ...featuredProducts].map((product, index) => (
                                <article className="mp-clean-product-card" key={product.name + index}>
                                    <div className="mp-cpc-image" onClick={() => { setSelectedProduct({ ...product, factories: featuredFactories.slice((index % featuredProducts.length) % featuredFactories.length, ((index % featuredProducts.length) % featuredFactories.length) + 2) }); setShowProductFactories(false); }}>
                                        <img src={product.imageUrl} alt={product.name} />
                                    </div>
                                    <div className="mp-cpc-info">
                                        <h3>{product.name.toUpperCase()}</h3>
                                        <p>{product.origin || product.description}</p>
                                        <strong>{product.price}</strong>
                                    </div>
                                </article>
                            ))}
                        </div>
                    </div>
                </section>

                {selectedCompareFactories.length > 0 && (
                    <section className="mp-compare-panel">
                        <div className="mp-section-title-row">
                            <div>
                                <h2>So sánh xưởng</h2>
                                <p>So sánh 2-4 xưởng theo chỉ số năng lực chính.</p>
                            </div>

```
