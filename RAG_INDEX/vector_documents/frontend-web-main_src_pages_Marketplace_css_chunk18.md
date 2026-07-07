# Knowledge Document: Marketplace.css (Chunk 19/44)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/Marketplace.css",
  "language": "css",
  "module": "pages",
  "business_domain": "factory",
  "tags": [
    "factory",
    "chat"
  ],
  "logical_type": "Generic",
  "chunk_index": 18,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
58px;
}

.mp-arrivals-header {
    display: flex;
    align-items: center;
    gap: 18px;
    margin-bottom: 26px;
}

.mp-arrivals-header div {
    height: 1px;
    flex: 1;
    background: var(--mp-outline);
}

.mp-arrivals-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    grid-template-rows: repeat(2, minmax(240px, 1fr));
    gap: 24px;
}

.mp-feature-product,
.mp-side-product {
    position: relative;
    overflow: hidden;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    background: var(--mp-surface-high);
}

.mp-feature-product {
    grid-row: span 2;
    min-height: 620px;
}

.mp-feature-product img,
.mp-side-product img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.8s ease;
}

.mp-feature-product:hover img,
.mp-side-product:hover img {
    transform: scale(1.05);
}

.mp-feature-product::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, transparent 20%, rgba(0, 0, 0, 0.82));
}

.mp-feature-product div {
    position: absolute;
    left: 34px;
    right: 34px;
    bottom: 34px;
    z-index: 1;
}

.mp-feature-product span {
    display: inline-block;
    margin-bottom: 14px;
    border-radius: 4px;
    padding: 6px 10px;
    background: rgba(255, 221, 195, 0.14);
    color: var(--mp-primary);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    text-transform: uppercase;
}

.mp-feature-product h3 {
    margin: 0 0 10px;
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(2rem, 4vw, 3rem);
    color: #fff;
}

.mp-feature-product p {
    max-width: 560px;
    color: rgba(226, 226, 229, 0.84);
}

.mp-feature-product strong {
    color: var(--mp-primary);
    font-size: 30px;
    font-weight: 300;
}

.mp-side-product {
    display: flex;
    flex-direction: column;
}

.mp-side-product img {
    height: 155px;
}

.mp-side-product h3 {
    margin: 18px 20px 6px;
    font-family: 'Montserrat', sans-serif;
}

.mp-side-product p {
    margin: 0 20px 22px;
    color: var(--mp-muted);
}

.mp-cta {
    margin-top: 60px;
    border: 1px solid rgba(255, 221, 195, 0.18);
    border-radius: 8px;
    padding: clamp(36px, 6vw, 56px);
    text-align: center;
    background: rgba(255, 221, 195, 0.05);
}

.mp-cta h2 {
    margin: 0 0 14px;
    font-family: 'Montserrat', sans-serif;

```
