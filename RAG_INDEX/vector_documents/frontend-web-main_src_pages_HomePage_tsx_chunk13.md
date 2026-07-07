# Knowledge Document: HomePage.tsx (Chunk 14/17)

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
  "chunk_index": 13,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
="coffee-kicker">Sản phẩm nổi bật</span>
            <h2>Các sản phẩm nổi tiếng trên thị trường.</h2>
            <p>Những dòng sản phẩm cà phê chất lượng cao được đánh giá tốt nhất.</p>
          </div>
          <button className="coffee-text-link" onClick={() => navigate('/login?returnUrl=/dat-hang')}>
            Xem tất cả sản phẩm <ArrowRight size={18} />
          </button>
        </div>

        <div className="coffee-workshop-grid">
          {workshops.map((workshop, index) => (
            <article className="coffee-workshop-card" key={workshop.name} data-reveal="product" style={{ transitionDelay: `${index * 120}ms` }}>
              <div className="coffee-workshop-card__image">
                <img src={workshop.image} alt={workshop.name} />
                <span>Best Seller</span>
              </div>
              <div className="coffee-workshop-card__body">
                <div className="coffee-workshop-card__title">
                  <h3>{workshop.name}</h3>
                  <small><Star size={13} fill="currentColor" /> {workshop.rating}</small>
                </div>
                <p>{workshop.description}</p>
                <div className="coffee-workshop-card__tags">
                  {workshop.tags.map((tag) => (
                    <span key={tag}>{tag}</span>
                  ))}
                </div>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section id="pricing" className="coffee-pricing">
        <div className="coffee-section-heading coffee-section-heading--center" data-reveal="up">
          <span className="coffee-kicker">Pricing</span>
          <h2>Chọn gói phù hợp với quy mô vận hành.</h2>
        </div>
        <div className="upgrade-grid" style={{ padding: '20px 0' }}>
          {pricingPlans.map((plan, index) => (
            <article
              key={plan.id}
              className={`plan-card accent-${plan.accent}${plan.featured ? ' featured' : ''}`}
              data-reveal="product"
              style={{ transitionDelay: `${index * 100}ms` }}
            >
              {plan.featured && (
                <div className="plan-badge-wrapper">
                  <span className="plan-badge">★ Phổ biến nhất</span>
                </div>
              )}

              <div className="plan-name">{plan.name}</div>

              <div className="plan-price">

```
