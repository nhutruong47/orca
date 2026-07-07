# Knowledge Document: HomePage.css (Chunk 13/34)

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
  "chunk_index": 12,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
 auto;
  margin-right: auto;
  color: rgba(255, 231, 199, 0.9) !important;
  text-shadow: 0 10px 28px rgba(0, 0, 0, 0.42);
}

.coffee-reserve .coffee-button {
  margin-top: 30px;
  background: var(--cream);
  color: var(--espresso);
}

.coffee-reserve__mark {
  position: absolute;
  right: clamp(16px, 8vw, 110px);
  bottom: clamp(16px, 6vw, 70px);
  opacity: 0.08;
}

[data-reveal] {
  opacity: 0;
  transform: translateY(42px) scale(0.985);
  transition: opacity 760ms ease, transform 880ms cubic-bezier(0.22, 1, 0.36, 1);
}

[data-reveal="left"] {
  transform: translateX(-44px) translateY(22px) scale(0.985);
}

[data-reveal="right"] {
  transform: translateX(44px) translateY(22px) scale(0.985);
}

[data-reveal="zoom"] {
  transform: translateY(30px) scale(0.965);
}

[data-reveal="product"] {
  transform: translateY(54px) scale(0.96);
  filter: blur(8px);
}

[data-reveal].is-visible {
  opacity: 1;
  transform: translateY(0) scale(1);
  filter: blur(0);
}

.coffee-product.is-visible:hover {
  transform: translateY(-8px) scale(1.012);
  background: rgba(255, 255, 255, 0.58);
  border-color: rgba(75, 47, 32, 0.24);
  box-shadow: 0 38px 90px rgba(75, 47, 32, 0.22);
}

.coffee-product.is-visible:hover .coffee-product__image img {
  transform: scale(1.09);
  filter: saturate(1.06) contrast(1.04);
}

.coffee-workshops {
  background: #fbf6ed;
  scroll-margin-top: 80px;
}

.coffee-workshop-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: clamp(16px, 2.3vw, 26px);
}

.coffee-workshop-card {
  overflow: hidden;
  background: rgba(255, 255, 255, 0.78);
  border: 1px solid rgba(75, 47, 32, 0.1);
  border-radius: 8px;
  box-shadow: 0 24px 62px rgba(75, 47, 32, 0.09);
  transition-property: opacity, transform, border-color, box-shadow;
}

.coffee-workshop-card.is-visible:hover {
  transform: translateY(-6px);
  border-color: rgba(75, 47, 32, 0.24);
  box-shadow: 0 34px 82px rgba(75, 47, 32, 0.16);
}

.coffee-workshop-card__image {
  position: relative;
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background: #d8c5ad;
}

.coffee-workshop-card__image img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  transform: scale(1.02);
  transition: transform 760ms cubic-bezier(0.22, 1, 0.36, 1), filter 320ms ease;
}

.coffee-workshop-card:hover .coffee-workshop-card__image img {
  transform: scale(1.08);

```
