# Knowledge Document: HomePage.tsx (Chunk 16/17)

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
  "chunk_index": 15,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
coffee-support-card" key={item.title} data-reveal="product" style={{ transitionDelay: `${index * 80}ms` }}>
                <span className="coffee-support-icon">
                  <Icon size={22} />
                </span>
                <h3>{item.title}</h3>
                <p>{item.detail}</p>
                <strong>{item.action}</strong>
              </article>
            );
          })}
        </div>
      </section>

      <section id="reserve" className="coffee-reserve">
        <div className="coffee-reserve__inner" data-reveal="up">
          <img className="coffee-reserve__logo" src={orcaLogo} alt="" aria-hidden="true" />
          <h2>Đăng ký dùng thử ORCA.</h2>
          <p>Trải nghiệm quy trình quản lý xưởng, đơn hàng, nhân viên và batch sản xuất trong một workspace.</p>
          <button className="coffee-button coffee-button--dark" onClick={() => navigate('/register')}>
            Đăng ký dùng thử
          </button>
        </div>
        <Sprout className="coffee-reserve__mark" size={160} aria-hidden="true" />
      </section>

      <footer id="contact" className="coffee-contact-footer">
        <div className="coffee-contact-footer__veil" aria-hidden="true" />
        <div className="coffee-contact-footer__inner" data-reveal="up">
          <div className="orca-footer-content">
            <div className="orca-footer-info">
              <div className="orca-footer-brand">
                <img src={orcaLogo} alt="ORCA" className="orca-footer-logo" />
                <span className="orca-footer-name">ORCA</span>
              </div>
              <p className="orca-footer-tagline">Điều phối sản xuất cà phê bằng AI.</p>
              
              <ul className="orca-footer-details">
                <li>
                  <MapPin size={20} className="footer-icon" />
                  <div>
                    <strong>KTX Khu B, ĐHQG-HCM</strong>
                    <p>Đường Mạc Đĩnh Chi, Phường Đông Hòa, TP. Hồ Chí Minh</p>
                  </div>
                </li>
                <li>
                  <Phone size={20} className="footer-icon" />
                  <span>0328 416 716</span>
                </li>
                <li>
                  <Mail size={20} className="footer-icon" />
                  <span>orca@gmail.com</span>
                </li>
              </ul>
            </div>


```
