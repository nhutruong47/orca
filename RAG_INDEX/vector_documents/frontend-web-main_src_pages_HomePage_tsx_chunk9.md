# Knowledge Document: HomePage.tsx (Chunk 10/17)

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
  "chunk_index": 9,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
ng, QC và đóng gói.</p>
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

      <section id="solution" className="coffee-story coffee-story--solution">
        <div className="coffee-story__media" data-reveal="left">
          <video autoPlay muted loop playsInline poster={solutionPoster} aria-label="Cafe workers operating a coffee machine station">
            <source src={solutionVideo} type="video/mp4" />
          </video>
        </div>
        <div className="coffee-story__copy" data-reveal="right">
          <span className="coffee-kicker">Giải pháp ORCA</span>
          <h2>Một hệ điều hành cho xưởng cà phê.</h2>
          <p>
            ORCA chuẩn hóa toàn bộ vòng đời sản xuất: từ nhận đơn, phân công, theo dõi batch,
            QC đến bàn giao. Đội vận hành biết việc nào đang chạy, ai phụ trách và điểm nghẽn nằm ở đâu.
          </p>
          <div className="coffee-solution-list">
            {solutions.map((solution) => (
              <div key={solution}>
                <CheckCircle size={18} />
                <span>{solution}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="features" className="coffee-features">
        <div className="coffee-section-heading coffee-section-heading--center" data-reveal="up">
          <span className="coffee-kicker">Các tính năng chính</span>
          <h2>Quản lý vận hành</h2>
        </div>

        <div className="coffee-feature-carousel" aria-label="Tính năng ORCA tự động chuyển động">
          {featureSlots.map((slide) => (
            <article className={`coffee-feature-slide coffee-feature-slide--${slide.slot}`} key={`${slide.title}-${slide.slot}`}>
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

```
