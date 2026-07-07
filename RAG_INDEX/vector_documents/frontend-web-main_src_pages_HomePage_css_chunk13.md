# Knowledge Document: HomePage.css (Chunk 14/34)

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
  "chunk_index": 13,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
 {
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
  filter: saturate(1.06) contrast(1.04);
}

.coffee-workshop-card__image span {
  position: absolute;
  top: 14px;
  left: 14px;
  padding: 7px 10px;
  color: var(--cream);
  background: rgba(42, 27, 18, 0.72);
  border: 1px solid rgba(247, 234, 217, 0.16);
  border-radius: 4px;
  font-size: 0.64rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.coffee-workshop-card__body {
  padding: 22px;
}

.coffee-workshop-card__title {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 14px;
}

.coffee-workshop-card h3 {
  margin: 0;
  color: var(--espresso);
  font-size: clamp(1.2rem, 2vw, 1.55rem);
  line-height: 1.18;
}

.coffee-workshop-card small {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  color: var(--walnut);
  font-size: 0.72rem;
  font-weight: 800;
  white-space: nowrap;
}

.coffee-workshop-card p {
  min-height: 74px;
  margin: 12px 0 18px;
  color: var(--muted);
  line-height: 1.75;
}

.coffee-workshop-card__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.coffee-workshop-card__tags span {
  padding: 6px 10px;
  color: #684830;
  background: rgba(75, 47, 32, 0.08);
  border-radius: 4px;
  font-size: 0.82rem;
}

.coffee-features {
  overflow: hidden;
  background:
    linear-gradient(180deg, #fbf6ed 0%, #f0dfc8 100%);
  scroll-margin-top: 80px;
}

.coffee-feature-carousel {
  position: relative;
  max-width: 1180px;
  min-height: clamp(390px, 48vw, 580px);
  margin: 0 auto;
  display: grid;
  place-items: center;
  perspective: 1200px;
}

.coffee-feature-slide {
  position: absolute;
  width: clamp(230px, 31vw, 430px);
  overflow: hidden;
  color: var(--cream);
  background: var(--espresso);
  border: 1px solid rgba(75, 47, 32, 0.16);
  border-radius: 8px;
  box-shadow: 0 28px 80px rgba(75, 47, 32, 0.16);
  isolation: isolate;
  transition: transform 780ms cubic-bezier(0.22, 1, 0.36, 1), opacity 640ms ease, filter 640ms ease;

```
