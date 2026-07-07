# Knowledge Document: HomePage.css (Chunk 12/34)

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
  "chunk_index": 11,
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
  color: var(--walnut);
  font-size: 0.95rem;
  font-weight: 800;
}

.coffee-product p {
  min-height: 52px;
  margin: 12px 0 14px;
  color: var(--muted);
  line-height: 1.7;
}

.coffee-product small {
  color: var(--sage);
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.coffee-product__cta {
  width: 100%;
  min-height: 42px;
  margin-top: 18px;
  color: var(--espresso);
  background: rgba(75, 47, 32, 0.06);
  border: 1px solid rgba(75, 47, 32, 0.14);
  border-radius: 8px;
  font: inherit;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  cursor: pointer;
  transition: transform 220ms ease, background-color 220ms ease, border-color 220ms ease;
}

.coffee-product__cta:hover {
  transform: translateY(-1px);
  background: rgba(75, 47, 32, 0.12);
  border-color: rgba(75, 47, 32, 0.26);
}

.coffee-reserve {
  min-height: 74svh;
  display: grid;
  place-items: center;
  color: var(--cream);
  background:
    linear-gradient(180deg, rgba(23, 16, 11, 0.72), rgba(23, 16, 11, 0.94)),
    url('/luxury-coffee-hero.png') center 62% / cover no-repeat;
  scroll-margin-top: 80px;
  overflow: hidden;
}

.coffee-reserve__inner {
  max-width: 760px;
  text-align: center;
}

.coffee-reserve svg {
  color: #e0a96d !important;
  filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.38));
}

.coffee-reserve h2 {
  margin-top: 20px;
  color: #d7a061 !important;
  text-shadow:
    0 18px 42px rgba(0, 0, 0, 0.58),
    0 0 26px rgba(215, 160, 97, 0.28);
}

.coffee-reserve p {
  margin-left: auto;
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

```
