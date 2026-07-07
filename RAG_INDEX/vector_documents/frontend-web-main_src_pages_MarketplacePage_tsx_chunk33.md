# Knowledge Document: MarketplacePage.tsx (Chunk 34/70)

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
  "chunk_index": 33,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
/orders')}>
                        <span className="material-symbols-outlined">receipt_long</span>
                    </button>
                    <button aria-label="Bộ lọc" onClick={() => document.getElementById('mp-filters')?.scrollIntoView({ behavior: 'smooth', block: 'center' })}>
                        <span className="material-symbols-outlined">tune</span>
                    </button>
                    <button aria-label="Language Toggle" onClick={() => setLanguage(lang => lang === 'vi' ? 'en' : 'vi')} style={{ fontSize: '13px', fontWeight: 'bold', padding: '0 8px', borderRadius: '4px', border: '1px solid rgba(255,255,255,0.2)' }}>
                        {language === 'vi' ? 'EN' : 'VI'}
                    </button>
                    <div className="mp-user-avatar">{(user?.username || user?.fullName || 'O').charAt(0).toUpperCase()}</div>
                </div>
            </header>

            <main className="mp-main">
                <section className="mp-market-hero">
                    <div className="mp-market-hero-copy">
                        <span className="mp-verified">
                            <span className="material-symbols-outlined">verified</span>
                            Hệ sinh thái đối tác
                        </span>
                        <h1><span style={{color: "#F59E0B"}}>Mạng Lưới</span> Xưởng Rang <em>Chuyên Nghiệp</em></h1>
                        <p>Kết nối trực tiếp với những xưởng rang thủ công và công nghiệp hàng đầu Việt Nam. Nâng tầm chất lượng cà phê cho doanh nghiệp của bạn.</p>
                        <div className="mp-hero-buttons">
                            <button onClick={() => document.getElementById('mp-partners')?.scrollIntoView({ behavior: 'smooth' })}>Tìm đối tác ngay</button>
                            <button onClick={() => document.getElementById('mp-products')?.scrollIntoView({ behavior: 'smooth' })}>Tìm hiểu thêm</button>
                        </div>
                    </div>
                    <aside className="mp-hero-control-card">
                        <h3>Quản lý Cửa hàng</h3>
                        <dl>
                            {factories.length > 0 && (
                                <div>
                                    <dt>Sản phẩm đang bán</dt>
                                    <dd>{factories.length}</dd>
                                </div>

```
