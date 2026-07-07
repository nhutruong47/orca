# Knowledge Document: HomePage.css (Chunk 21/34)

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
  "chunk_index": 20,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
x, 2.3vw, 26px);
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
  line-height: 1;
}

.coffee-pricing-card p {
  color: var(--muted);
  line-height: 1.7;
}

.coffee-pricing-card span {
  display: flex;
  align-items: center;
  gap: 10px;
  color: var(--walnut);
}

.coffee-pricing-card span svg {
  color: var(--sage);
  flex: 0 0 auto;
}

.coffee-pricing-card .coffee-button {
  width: 100%;
  margin-top: auto;
}

.coffee-support {
  position: relative;
  padding: clamp(72px, 10vw, 128px) clamp(20px, 6vw, 86px);
  background:
    linear-gradient(180deg, #fbf6ed 0%, #f5eadb 100%);
  scroll-margin-top: 80px;
}

.coffee-support-grid {
  width: min(1120px, 100%);
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 16px;
}

.coffee-support-card {
  min-height: 260px;
  padding: 26px;
  display: flex;
  flex-direction: column;
  color: #201710;
  background: rgba(255, 253, 249, 0.78);
  border: 1px solid rgba(76, 57, 38, 0.12);
  border-radius: 8px;
  box-shadow: 0 18px 44px rgba(75, 47, 32, 0.08);
  transition: transform 220ms ease, box-shadow 220ms ease, border-color 220ms ease;
}

.coffee-support-card:hover {
  transform: translateY(-4px);
  border-color: rgba(128, 98, 65, 0.36);
  box-shadow: 0 26px 58px rgba(75, 47, 32, 0.12);
}

.coffee-support-icon {
  width: 48px;
  height: 48px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  background: #5e4228;
  border-radius: 8px;
}

.coffee-support-card h3 {
  margin: 22px 0 0;
  color: #201710;
  font-size: 1.05rem;
  font-weight: 850;
}

.coffee-support-card p {
  margin: 12px 0 20px;
  color: rgba(73, 48, 28, 0.66);
  font-size: 0.92rem;
  font-weight: 650;
  line-height: 1.6;
}

.coffee-support-card strong {
  margin-top: auto;
  color: #0f766e;
  font-size: 0.94rem;
  font-weight: 850;
}

@keyframes featureDrift {
  from {
    opacity: 0;
    transform: translateX(42vw) scale(0.7);
  }
}

@keyframes featureCenterZoom {
  from {
    transform: scale(1.02);
  }

  to {
    transform: scale(1.12);
  }

```
