# Knowledge Document: HomePage.css (Chunk 11/34)

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
  "chunk_index": 10,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
04));
  transform-origin: center;
  will-change: transform;
}

.coffee-cinema__panel div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: clamp(32px, 6vw, 72px);
}

.coffee-cinema__panel svg {
  color: var(--caramel);
  margin-bottom: 24px;
}

.coffee-cinema h2,
.coffee-cinema p {
  color: var(--cream);
}

.coffee-cinema p {
  color: rgba(247, 234, 217, 0.72);
}

.coffee-products {
  background: linear-gradient(180deg, #fbf6ed 0%, #efe1cc 100%);
  scroll-margin-top: 80px;
}

.coffee-section-heading {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: clamp(30px, 5vw, 54px);
}

.coffee-section-heading p {
  max-width: 620px;
  margin-top: 10px;
  color: var(--muted);
}

.coffee-section-heading--center {
  max-width: 840px;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  display: block;
}

.coffee-text-link {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 42px;
  color: var(--walnut);
  background: transparent;
  border: 0;
  font: inherit;
  font-size: 0.86rem;
  cursor: pointer;
  transition: color 220ms ease, transform 220ms ease;
}

.coffee-text-link:hover {
  color: var(--espresso);
  transform: translateX(3px);
}

.coffee-product-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: clamp(16px, 2.4vw, 28px);
}

.coffee-product {
  overflow: hidden;
  background: rgba(255, 255, 255, 0.46);
  border: 1px solid rgba(75, 47, 32, 0.14);
  border-radius: 8px;
  box-shadow: 0 24px 64px rgba(75, 47, 32, 0.12);
  transform-origin: center bottom;
  transition-property: opacity, transform, box-shadow, border-color, background-color;
}

.coffee-product__image {
  aspect-ratio: 4 / 5;
  overflow: hidden;
  background: #d9c4aa;
}

.coffee-product__image img {
  transform: scale(1.015);
  transition: transform 780ms cubic-bezier(0.22, 1, 0.36, 1), filter 420ms ease;
}

.coffee-product:hover .coffee-product__image img {
  transform: scale(1.06);
}

.coffee-product__body {
  padding: 22px;
}

.coffee-product__top {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 16px;
}

.coffee-product h3 {
  margin: 0;
  color: var(--espresso);
  font-family: var(--display-font);
  font-size: clamp(1.45rem, 2.2vw, 2rem);
  font-weight: 800;
  letter-spacing: 0;
}

.coffee-product__top span {

```
