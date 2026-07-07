# Knowledge Document: HomePage.css (Chunk 10/34)

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
  "chunk_index": 9,
  "total_chunks": 34
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, production

## Source Code Chunk
```css
vw, 5.6rem);
  font-weight: 800;
  line-height: 1;
  letter-spacing: 0;
}

.coffee-story__copy p,
.coffee-cinema p,
.coffee-reserve p {
  max-width: 620px;
  margin: 24px 0 0;
  color: var(--muted);
  font-size: 1rem;
  line-height: 1.9;
}

.coffee-story__metrics {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin-top: 34px;
}

.coffee-story__metrics div {
  padding: 18px;
  border: 1px solid rgba(75, 47, 32, 0.16);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.35);
}

.coffee-story__metrics strong,
.coffee-story__metrics span {
  display: block;
}

.coffee-story__metrics strong {
  color: var(--walnut);
  font-size: clamp(1.45rem, 2.6vw, 2rem);
  line-height: 1;
}

.coffee-story__metrics span {
  margin-top: 8px;
  color: rgba(64, 43, 30, 0.62);
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.coffee-solution-list,
.coffee-workflow-list {
  display: grid;
  gap: 12px;
  margin-top: 30px;
}

.coffee-solution-list div,
.coffee-workflow-list div {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px;
  color: var(--walnut);
  background: rgba(255, 255, 255, 0.42);
  border: 1px solid rgba(75, 47, 32, 0.13);
  border-radius: 8px;
}

.coffee-solution-list svg {
  flex: 0 0 auto;
  color: var(--sage);
}

.coffee-workflow-list strong {
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  flex: 0 0 auto;
  color: var(--cream);
  background: var(--espresso);
  border-radius: 999px;
  font-size: 0.86rem;
}

.coffee-cinema {
  background: #fbf6ed;
}

.coffee-cinema__panel {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(300px, 0.8fr);
  align-items: stretch;
  min-height: 520px;
  overflow: hidden;
  color: var(--cream);
  background: var(--espresso);
  border-radius: 8px;
}

.coffee-cinema__panel img {
  min-height: 420px;
  filter: saturate(0.92) contrast(1.08);
  transform: scale(var(--coffee-cinema-scale, 1.04));
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


```
