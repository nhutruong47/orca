# Knowledge Document: HomePage.tsx (Chunk 15/17)

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
  "chunk_index": 14,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
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
                <strong className="price-value">{plan.price}</strong>
                <span className="price-note">{plan.priceNote}</span>
              </div>

              <div className="plan-sub-info">
                <div className="plan-subtitle">{plan.subTitle}</div>
                <p className="plan-description">{plan.description}</p>
              </div>

              <button
                type="button"
                className="plan-action"
                onClick={() => navigate('/login?returnUrl=/upgrade')}
              >
                {plan.id === 'starter' ? 'Bắt đầu' : 'Nâng cấp ngay'}
              </button>

              <ul className="plan-features">
                {plan.features.map((feature) => (
                  <li key={feature}>
                    <span className="feature-check-circle">
                      <Check size={10} strokeWidth={4} />
                    </span>
                    <span className="feature-text">{feature}</span>
                  </li>
                ))}
              </ul>
            </article>
          ))}
        </div>
      </section>

      <section id="support" className="coffee-support">
        <div className="coffee-section-heading coffee-section-heading--center" data-reveal="up">
          <span className="coffee-kicker">Support</span>
          <h2>Luôn có đội hỗ trợ khi xưởng cần xử lý nhanh.</h2>
        </div>

        <div className="coffee-support-grid">
          {supportOptions.map((item, index) => {
            const Icon = item.icon;

            return (
              <article className="coffee-support-card" key={item.title} data-reveal="product" style={{ transitionDelay: `${index * 80}ms` }}>
                <span className="coffee-support-icon">
                  <Icon size={22} />
                </span>
                <h3>{item.title}</h3>
                <p>{item.detail}</p>
                <strong>{item.action}</strong>
              </article>
            );
          })}

```
