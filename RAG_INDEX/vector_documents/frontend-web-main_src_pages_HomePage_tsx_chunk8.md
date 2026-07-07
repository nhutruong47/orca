# Knowledge Document: HomePage.tsx (Chunk 9/17)

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
  "chunk_index": 8,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
một quy trình rõ ràng.
          </p>
          <div className="coffee-hero__actions">
            <button className="coffee-button coffee-button--light" onClick={() => scrollTo('pricing')}>
              Đăng ký dùng thử
            </button>
            <button className="coffee-button coffee-button--ghost" onClick={() => scrollTo('dashboard')}>
              Xem dashboard
            </button>
          </div>
        </div>

        <button className="coffee-scroll-cue" onClick={() => scrollTo('stats')} aria-label="Scroll to statistics">
          <ArrowDown size={18} />
        </button>
      </section>

      <section id="stats" className="coffee-ops-overview">
        <div className="coffee-ops-header" data-reveal="up">
          <span className="coffee-kicker">Năng lực vận hành</span>
          <h2>Các thành phần quản lý cốt lõi của ORCA.</h2>
          <p>Thay vì trình bày số liệu ước tính, trang chủ tập trung vào những nghiệp vụ chính mà hệ thống hỗ trợ.</p>
        </div>

        <div className="coffee-stat-grid">
          {stats.map((item, index) => {
            const Icon = item.icon;
            return (
              <article className="coffee-stat-card" key={item.label} data-reveal="product" style={{ transitionDelay: `${index * 90}ms` }}>
                <div className="coffee-stat-card__top">
                  <Icon size={20} />
                  <span>{item.label}</span>
                </div>
                <strong>{item.value}</strong>
                <p>{item.detail}</p>
              </article>
            );
          })}
        </div>

        <div id="problems" className="coffee-problem-panel" data-reveal="up">
          <div className="coffee-problem-panel__intro">
            <span className="coffee-kicker">Vấn đề khách hàng gặp</span>
            <h2>Khi sản xuất tăng tốc, dữ liệu bắt đầu rời rạc.</h2>
            <p>Các đội cà phê thường mất thời gian để nối lại thông tin giữa người bán, quản lý xưởng, QC và đóng gói.</p>
          </div>
          <div className="coffee-problem-list">
            {problems.map((problem, index) => (
              <article className="coffee-problem-row" key={problem}>
                <strong>{String(index + 1).padStart(2, '0')}</strong>
                <p>{problem}</p>
              </article>
            ))}
          </div>
        </div>
      </section>


```
