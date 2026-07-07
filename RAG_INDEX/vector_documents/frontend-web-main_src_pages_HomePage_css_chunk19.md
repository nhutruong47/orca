# Knowledge Document: HomePage.css (Chunk 20/34)

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
  "chunk_index": 19,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
 font-weight: 850;
}

.coffee-pricing .plan-description {
  margin: 12px 0 0;
  color: rgba(73, 48, 28, 0.58);
  font-size: 0.92rem;
  line-height: 1.45;
}

.coffee-pricing .accent-enterprise .plan-description {
  color: #7f9cbb;
}

.coffee-pricing .plan-action {
  width: 100%;
  min-height: 46px;
  margin: 22px 0 34px;
  padding: 0 20px;
  color: #15100d;
  background: rgba(255, 255, 255, 0.52);
  border: 1px solid rgba(76, 57, 38, 0.12);
  border-radius: 999px;
  font: inherit;
  font-size: 0.92rem;
  font-weight: 850;
  cursor: pointer;
  transition: transform 180ms ease, background 180ms ease, box-shadow 180ms ease;
}

.coffee-pricing .plan-action:hover {
  transform: translateY(-1px);
  background: #ffffff;
  box-shadow: 0 12px 26px rgba(75, 47, 32, 0.12);
}

.coffee-pricing .featured .plan-action {
  color: #ffffff;
  background: linear-gradient(90deg, #806241 0%, #3e2817 100%);
  border-color: transparent;
}

.coffee-pricing .accent-enterprise .plan-action {
  color: #061427;
  background: #ffffff;
  border-color: #ffffff;
}

.coffee-pricing .plan-features {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
  list-style: none;
}

.coffee-pricing .plan-features li {
  display: grid;
  grid-template-columns: 18px 1fr;
  gap: 12px;
  align-items: start;
  color: rgba(73, 48, 28, 0.82);
  font-size: 0.9rem;
  font-weight: 700;
  line-height: 1.45;
}

.coffee-pricing .accent-enterprise .plan-features li {
  color: #8fb5da;
}

.coffee-pricing .feature-check-circle {
  width: 18px;
  height: 18px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: #15a75a;
  border: 2px solid currentColor;
  border-radius: 999px;
  transform: translateY(1px);
}

.coffee-pricing .featured .feature-check-circle {
  color: #3d2b1c;
}

.coffee-pricing .accent-enterprise .feature-check-circle {
  color: #52dbd5;
}

.coffee-pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: clamp(16px, 2.3vw, 26px);
}

.coffee-pricing-card {
  min-height: 430px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.coffee-pricing-card h3 {
  margin: 0;
  color: var(--espresso);
  font-family: var(--display-font);
  font-size: clamp(1.8rem, 3vw, 2.5rem);
  font-weight: 800;
}

.coffee-pricing-card > strong {
  color: var(--walnut);
  font-size: clamp(2rem, 4vw, 3.4rem);

```
