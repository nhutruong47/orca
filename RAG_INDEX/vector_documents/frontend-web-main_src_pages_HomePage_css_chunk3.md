# Knowledge Document: HomePage.css (Chunk 4/34)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/HomePage.css",
  "language": "css",
  "module": "pages",
  "business_domain": "dashboard",
  "tags": [
    "dashboard",
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 3,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
background: var(--cream);
}

.coffee-button--ghost {
  color: var(--cream);
  background: rgba(247, 234, 217, 0.08);
  border-color: rgba(247, 234, 217, 0.28);
}

.coffee-button--dark {
  color: var(--cream);
  background: var(--espresso);
}

.coffee-scroll-cue {
  position: absolute;
  left: 50%;
  bottom: 24px;
  z-index: 3;
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  color: var(--cream);
  background: rgba(31, 20, 13, 0.42);
  border: 1px solid rgba(247, 234, 217, 0.22);
  border-radius: 999px;
  transform: translateX(-50%);
  cursor: pointer;
  animation: coffeeCue 1.8s ease-in-out infinite;
}

.coffee-story,
.coffee-products,
.coffee-reserve,
.coffee-cinema,
.coffee-workshops,
.coffee-features,
.coffee-roles,
.coffee-ai-section,
.coffee-ops-overview,
.coffee-problems,
.coffee-dashboard-section,
.coffee-pricing {
  position: relative;
  padding: clamp(76px, 10vw, 132px) clamp(20px, 6vw, 86px);
}

.coffee-ops-overview {
  background:
    linear-gradient(180deg, #f6ead8 0%, #fbf6ed 100%);
  scroll-margin-top: 80px;
}

.coffee-ops-header {
  max-width: 920px;
  margin-bottom: clamp(28px, 5vw, 52px);
}

.coffee-ops-header h2,
.coffee-problem-panel__intro h2 {
  margin: 0;
  color: var(--espresso);
  font-family: var(--display-font);
  font-size: clamp(2.7rem, 6vw, 5.4rem);
  font-weight: 800;
  line-height: 1;
  letter-spacing: 0;
}

.coffee-ops-header p,
.coffee-problem-panel__intro p {
  max-width: 680px;
  margin: 20px 0 0;
  color: var(--muted);
  line-height: 1.85;
}

.coffee-stat-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 14px;
}

.coffee-stat-card,
.coffee-pricing-card {
  border: 1px solid rgba(75, 47, 32, 0.14);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.54);
  box-shadow: 0 24px 64px rgba(75, 47, 32, 0.1);
  transition-property: opacity, transform, box-shadow, border-color, background-color;
}

.coffee-stat-card {
  min-height: 210px;
  display: flex;
  flex-direction: column;
  padding: 24px;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.68), rgba(255, 255, 255, 0.36));
}

.coffee-stat-card svg {
  color: var(--caramel);
}

.coffee-stat-card__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 38px;
}

.coffee-stat-card__top span {
  color: rgba(64, 43, 30, 0.64);
  font-size: 0.7rem;

```
