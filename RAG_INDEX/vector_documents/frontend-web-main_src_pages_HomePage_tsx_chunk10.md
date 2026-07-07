# Knowledge Document: HomePage.tsx (Chunk 11/17)

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
  "chunk_index": 10,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
key={`${slide.title}-${slide.slot}`}>
              <img src={slide.image} alt={slide.title} />
              <div>
                <h3>{slide.title}</h3>
                <p>{slide.text}</p>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section id="roles" className="coffee-roles">
        <div className="coffee-section-heading" data-reveal="up">
          <div>
            <span className="coffee-kicker">Role Management</span>
            <h2>Phân quyền rõ ràng cho từng nhóm người dùng.</h2>
            <p>Mỗi vai trò chỉ nhìn thấy đúng phần việc cần xử lý, giúp giảm nhầm lẫn khi nhiều bộ phận cùng tham gia sản xuất.</p>
          </div>
        </div>

        <div className="coffee-role-grid">
          {roles.map((role, index) => (
            <article className="coffee-role-card" key={role.name} data-reveal="product" style={{ transitionDelay: `${index * 100}ms` }}>
              <ShieldCheck size={22} />
              <h3>{role.name}</h3>
              <p>{role.text}</p>
            </article>
          ))}
        </div>
      </section>

      <section id="production" className="coffee-story coffee-story--production production-studio">
        <div className="production-studio__glow" aria-hidden="true" />
        <div className="production-studio__media" data-reveal="left">
          <article className="studio-video-card studio-video-card--main">
            <video autoPlay muted loop playsInline poster={productionPoster}>
              <source src={productionVideo} type="video/mp4" />
            </video>
            <div className="studio-video-card__shade" />
            <div className="studio-video-card__meta">
              <span>Warehouse check</span>
              <strong>Clipboard inventory</strong>
            </div>
          </article>

          <article className="studio-video-card studio-video-card--float">
            <video autoPlay muted loop playsInline poster={productionPoster}>
              <source src={roastingVideo} type="video/mp4" />
            </video>
            <div className="studio-video-card__shade" />
            <div className="studio-video-card__meta">
              <span>Batch camera</span>
              <strong>Roast flow</strong>
            </div>
          </article>

          <div className="studio-signal-card studio-signal-card--top">

```
