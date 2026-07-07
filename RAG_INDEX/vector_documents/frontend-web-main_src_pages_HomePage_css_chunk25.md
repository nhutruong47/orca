# Knowledge Document: HomePage.css (Chunk 26/34)

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
  "chunk_index": 25,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
ffee-pricing-card h3,
.coffee-pricing-card > strong {
  color: #12211f !important;
}

/* Problem section: warm brown panel, without the old warning icons. */
.coffee-problem-panel {
  width: auto;
  margin: clamp(26px, 4vw, 44px) 0 0 !important;
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(320px, 1.1fr);
  align-items: start;
  gap: clamp(28px, 5vw, 70px);
  min-height: auto;
  padding: clamp(26px, 5vw, 54px) !important;
  overflow: hidden;
  color: var(--cream) !important;
  background:
    radial-gradient(circle at 82% 20%, rgba(255, 209, 102, 0.13), transparent 28%),
    linear-gradient(135deg, rgba(111, 75, 34, 0.22), transparent 46%),
    #412D15 !important;
  border: 1px solid rgba(247, 234, 217, 0.1) !important;
  border-radius: 8px !important;
  box-shadow: 0 34px 92px rgba(75, 47, 32, 0.2) !important;
}

.coffee-problem-panel::before {
  display: none;
}

.coffee-problem-panel__intro,
.coffee-problem-list {
  position: relative;
  z-index: 1;
}

.coffee-problem-panel .coffee-kicker {
  display: block;
  margin-bottom: 14px;
  color: var(--readable-gold) !important;
  font-size: clamp(0.86rem, 1.12vw, 1.08rem);
  font-weight: 950;
  letter-spacing: 0.12em;
  text-shadow:
    0 0 16px rgba(255, 209, 102, 0.42),
    0 2px 10px rgba(0, 0, 0, 0.46);
  text-transform: uppercase;
}

.coffee-problem-panel__intro h2 {
  max-width: none;
  margin: 0;
  color: #fffdf7 !important;
  font-family: var(--display-font);
  font-size: clamp(2.7rem, 6vw, 5.4rem);
  font-weight: 800;
  line-height: 1;
  letter-spacing: 0;
  text-shadow:
    0 12px 38px rgba(0, 0, 0, 0.72),
    0 0 36px rgba(255, 209, 102, 0.22),
    0 0 72px rgba(255, 209, 102, 0.16);
}

.coffee-problem-panel__intro h2::first-line {
  color: inherit;
}

.coffee-problem-panel__intro p {
  display: block;
  max-width: 680px;
  margin: 20px 0 0;
  color: rgba(255, 250, 240, 0.9) !important;
  font-weight: 650;
  line-height: 1.85;
  text-shadow: 0 3px 14px rgba(0, 0, 0, 0.42);
}

.coffee-problem-list {
  display: grid;
  gap: 16px;
}

.coffee-problem-row {
  min-height: auto;
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: start;
  gap: 14px;
  padding: 18px !important;
  background: rgba(255, 255, 255, 0.055) !important;
  border: 1px solid rgba(247, 234, 217, 0.08) !important;
  border-radius: 8px !important;
  box-shadow: none;
}

.coffee-problem-row:hover {

```
