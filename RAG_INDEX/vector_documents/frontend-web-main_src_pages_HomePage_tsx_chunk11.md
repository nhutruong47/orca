# Knowledge Document: HomePage.tsx (Chunk 12/17)

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
  "chunk_index": 11,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
ionPoster}>
              <source src={roastingVideo} type="video/mp4" />
            </video>
            <div className="studio-video-card__shade" />
            <div className="studio-video-card__meta">
              <span>Batch camera</span>
              <strong>Roast flow</strong>
            </div>
          </article>

          <div className="studio-signal-card studio-signal-card--top">
            <ClipboardCheck size={18} />
            <span>QC synced</span>
          </div>
          <div className="studio-signal-card studio-signal-card--bottom">
            <BarChart3 size={18} />
            <span>Live capacity</span>
          </div>
        </div>
        <div className="coffee-story__copy production-studio__copy" data-reveal="right">
          <span className="coffee-kicker">Workflow sản xuất</span>
          <h2>Giao việc, chạy batch, kiểm tra tiến độ.</h2>
          <p>
            Mỗi đơn hàng được chuyển thành workflow rõ ràng để quản lý xưởng, nhân viên rang,
            QC và đóng gói cùng nhìn một nguồn dữ liệu.
          </p>
          <div className="coffee-workflow-list production-studio__workflow">
            {workflowSteps.map((step, index) => (
              <div key={step} style={{ transitionDelay: `${index * 80}ms` }}>
                <strong>{index + 1}</strong>
                <span>{step}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="dashboard" className="coffee-dashboard-curved">
        <div className="coffee-curved-heading" data-reveal="up">
          <span className="coffee-kicker">Mọi hoạt động sản xuất trong một hệ thống duy nhất</span>
          <h2>Theo dõi đơn hàng, giao việc, tiến độ sản xuất và báo cáo vận hành từ một nơi duy nhất.</h2>
        </div>
        
        <div className="coffee-curved-wheel-container">
          <div className="coffee-curved-wheel" ref={wheelRef}>
            {[...Array(6)].map((_, setIndex) => 
              curvedShowcaseImages.map((item, i) => {
                const globalIndex = setIndex * curvedShowcaseImages.length + i;
                return (
                  <article 
                    className="coffee-curved-card" 
                    key={`${setIndex}-${i}`}
                    style={{ transform: `rotate(${globalIndex * 7.5}deg)` }}
                  >

```
