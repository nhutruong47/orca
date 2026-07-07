# Knowledge Document: HomePage.css (Chunk 5/34)

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
  "chunk_index": 4,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
 column;
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
  font-weight: 800;
  letter-spacing: 0.12em;
  text-align: right;
  text-transform: uppercase;
}

.coffee-stat-card strong {
  color: var(--espresso);
  font-size: clamp(1.45rem, 2.4vw, 2.05rem);
  font-weight: 800;
  line-height: 1.12;
}

.coffee-stat-card p {
  margin: 14px 0 0;
  color: var(--muted);
  line-height: 1.65;
}

.coffee-problem-panel {
  margin-top: clamp(26px, 4vw, 44px);
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(320px, 1.1fr);
  gap: clamp(28px, 5vw, 70px);
  align-items: start;
  padding: clamp(26px, 5vw, 54px);
  color: var(--cream);
  background:
    linear-gradient(135deg, rgba(185, 135, 86, 0.18), transparent 46%),
    #1f140d;
  border: 1px solid rgba(75, 47, 32, 0.22);
  border-radius: 8px;
  box-shadow: 0 34px 92px rgba(75, 47, 32, 0.2);
}

.coffee-problem-panel .coffee-kicker,
.coffee-problem-panel__intro h2 {
  color: var(--cream);
}

.coffee-problem-panel__intro p {
  color: rgba(247, 234, 217, 0.68);
}

.coffee-problem-list {
  display: grid;
  gap: 12px;
}

.coffee-problem-row {
  display: grid;
  grid-template-columns: auto auto 1fr;
  gap: 14px;
  align-items: start;
  padding: 18px;
  background: rgba(255, 255, 255, 0.055);
  border: 1px solid rgba(247, 234, 217, 0.08);
  border-radius: 8px;
  transition: transform 260ms ease, background-color 260ms ease, border-color 260ms ease;
}

.coffee-problem-row:hover {
  transform: translateX(4px);
  background: rgba(255, 255, 255, 0.085);
  border-color: rgba(247, 234, 217, 0.16);
}

.coffee-problem-row strong {
  color: var(--caramel);
  font-size: 0.78rem;
  letter-spacing: 0.12em;
}

.coffee-problem-row svg {
  color: var(--caramel);
}

.coffee-problem-row p {
  margin: 0;
  color: rgba(247, 234, 217, 0.74);
  line-height: 1.72;
}

.coffee-stat-card.is-visible:hover,
.coffee-pricing-card.is-visible:hover {
  transform: translateY(-6px);
  border-color: rgba(75, 47, 32, 0.26);
  background: rgba(255, 255, 255, 0.72);

```
