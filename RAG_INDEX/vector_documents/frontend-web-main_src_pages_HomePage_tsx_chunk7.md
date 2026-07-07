# Knowledge Document: HomePage.tsx (Chunk 8/17)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/HomePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "factory",
  "tags": [
    "factory",
    "dashboard",
    "admin",
    "workspace",
    "production",
    "warehouse",
    "inventory",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 7,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
th) % featureSlides.length;
    return {
      ...featureSlides[index],
      slot: offset === 0 ? 'center' : offset < 0 ? 'left' : 'right'
    };
  });

  return (
    <main className="coffee-home">
      <header className={`coffee-nav${navScrolled ? ' coffee-nav--scrolled' : ''}${navHidden ? ' coffee-nav--hidden' : ''}`} aria-label="Điều hướng chính">
        <div className="coffee-nav__inner">
          <button className="coffee-nav__brand" onClick={() => scrollTo('hero')} aria-label="Trang chủ ORCA">
            <img src={orcaLogo} alt="ORCA" className="coffee-nav__brand-img" />
          </button>

          <nav className="coffee-nav__links" aria-label="Các mục trên trang">
            {navItems.map((item) => (
              <button
                key={item.target}
                className={`coffee-nav__item${item.target === 'hero' ? ' coffee-nav__item--active' : ''}`}
                onClick={() => scrollTo(item.target)}
              >
                <span>{item.label}</span>
              </button>
            ))}
          </nav>

          <div className="coffee-nav__auth" aria-label="Tài khoản">
            <button type="button" onClick={() => navigate('/login')}>Đăng nhập</button>
            <button type="button" onClick={() => navigate('/register')}>Đăng ký</button>
          </div>
        </div>
      </header>

      <section id="hero" className="coffee-hero">
        <div className="coffee-hero__image" aria-hidden="true">
          <video autoPlay muted loop playsInline poster={productionPoster}>
            <source src={productionVideo} type="video/mp4" />
          </video>
        </div>
        <div className="coffee-hero__veil" aria-hidden="true" />

        <div className="coffee-hero__content">
          <span className="coffee-kicker">Coffee Production Management Platform</span>
          <h1>ORCA</h1>
          <p>
            Nền tảng quản lý sản xuất cà phê giúp xưởng, đơn hàng, nhân viên và batch vận hành
            trong một quy trình rõ ràng.
          </p>
          <div className="coffee-hero__actions">
            <button className="coffee-button coffee-button--light" onClick={() => scrollTo('pricing')}>
              Đăng ký dùng thử
            </button>
            <button className="coffee-button coffee-button--ghost" onClick={() => scrollTo('dashboard')}>
              Xem dashboard
            </button>

```
