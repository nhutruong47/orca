# Knowledge Document: MarketplacePage.tsx (Chunk 35/70)

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
  "chunk_index": 34,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx

                    <aside className="mp-hero-control-card">
                        <h3>Quản lý Cửa hàng</h3>
                        <dl>
                            {factories.length > 0 && (
                                <div>
                                    <dt>Sản phẩm đang bán</dt>
                                    <dd>{factories.length}</dd>
                                </div>
                            )}
                            {manufacturingRequests.length > 0 && (
                                <div>
                                    <dt>Đơn hàng mới</dt>
                                    <dd>{manufacturingRequests.length}</dd>
                                </div>
                            )}
                            {totalCompletedOrders > 0 && (
                                <div>
                                    <dt>Lượt giao dịch</dt>
                                    <dd>{totalCompletedOrders}</dd>
                                </div>
                            )}
                        </dl>
                        <button type="button" onClick={openPublishModal}>
                            <span className="material-symbols-outlined">upload</span>
                            Đăng tải sản phẩm
                        </button>
                    </aside>
                </section>

                <section id="mp-filters" className="mp-category-row" aria-label="Bộ lọc thị trường">
                    {marketplaceCategories.map((category, index) => (
                        <button
                            key={category.label}
                            type="button"
                            className={
                                (index === 0 && !specialtyFilter && !factoryTypeFilter && !statusFilter)
                                    || (category.label === 'Nguyên liệu' && specialtyFilter === 'Cung ứng cà phê nhân')
                                    || (category.label === 'Dịch vụ rang' && specialtyFilter === 'Rang cà phê')
                                    || (category.label === 'Dịch vụ đóng gói' && specialtyFilter === 'Đóng gói')
                                    || (category.label === 'Dịch vụ trọn gói' && specialtyFilter === 'Gia công OEM')
                                    ? 'active'
                                    : ''
                            }

```
