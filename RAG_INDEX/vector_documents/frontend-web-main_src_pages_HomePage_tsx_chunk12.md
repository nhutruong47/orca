# Knowledge Document: HomePage.tsx (Chunk 13/17)

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
  "chunk_index": 12,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
((_, setIndex) => 
              curvedShowcaseImages.map((item, i) => {
                const globalIndex = setIndex * curvedShowcaseImages.length + i;
                return (
                  <article 
                    className="coffee-curved-card" 
                    key={`${setIndex}-${i}`}
                    style={{ transform: `rotate(${globalIndex * 7.5}deg)` }}
                  >
                    <div className="card-inner">
                      <img src={item.image} alt={item.title} />
                      <div className="glass-label">{item.title}</div>
                    </div>
                  </article>
                );
              })
            )}
          </div>
        </div>
      </section>

      <section id="ai" className="coffee-ai-section">
        <div className="coffee-ai-hero" data-reveal="up">
          <div>
            <span className="coffee-kicker">Công nghệ AI</span>
            <h2>AI hỗ trợ quản lý sản xuất cà phê.</h2>
            <p>
              ORCA giúp chủ xưởng biết hôm nay cần làm gì, ai đang làm việc gì và đơn hàng nào có nguy cơ bị chậm.
            </p>
          </div>
          <div className="coffee-ai-orb" aria-hidden="true">
            <Brain size={58} />
            <Sparkles size={22} />
          </div>
        </div>

        <div className="coffee-ai-grid">
          {aiFeatures.map((feature, index) => {
            const Icon = feature.icon;
            return (
              <article className="coffee-ai-card" key={feature.title} data-reveal="product" style={{ transitionDelay: `${index * 90}ms` }}>
                <Icon size={22} />
                <h3>{feature.title}</h3>
                <p>{feature.text}</p>
              </article>
            );
          })}
        </div>
      </section>

      <section id="workshops" className="coffee-workshops">
        <div className="coffee-section-heading" data-reveal="up">
          <div>
            <span className="coffee-kicker">Sản phẩm nổi bật</span>
            <h2>Các sản phẩm nổi tiếng trên thị trường.</h2>
            <p>Những dòng sản phẩm cà phê chất lượng cao được đánh giá tốt nhất.</p>
          </div>
          <button className="coffee-text-link" onClick={() => navigate('/login?returnUrl=/dat-hang')}>
            Xem tất cả sản phẩm <ArrowRight size={18} />
          </button>
        </div>


```
