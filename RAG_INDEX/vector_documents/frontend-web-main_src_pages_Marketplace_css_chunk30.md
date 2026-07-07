# Knowledge Document: Marketplace.css (Chunk 31/44)

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
  "chunk_index": 30,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
10px;
    text-transform: uppercase;
}

.mp-manufacturing-market .mp-factory-actions {
    display: grid;
    grid-template-columns: 1fr;
    padding: 0 18px 18px;
}

.mp-manufacturing-market .mp-factory-actions button {
    min-height: 42px;
    border-color: rgba(255, 255, 255, 0.07);
    border-radius: 5px;
    background: #2b2e30;
    color: #fff7ef;
    font-family: 'Montserrat', sans-serif;
    font-size: 13px;
}

.mp-product-section {
    margin-top: 64px;
}

.mp-product-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.65fr) minmax(280px, 0.85fr);
    gap: 24px;
}

.mp-feature-product-card,
.mp-product-card {
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    background: #202325;
}

.mp-feature-product-card {
    position: relative;
    min-height: 500px;
}

.mp-feature-product-card img,
.mp-product-card img {
    width: 100%;
    display: block;
    object-fit: cover;
}

.mp-feature-product-card img {
    height: 100%;
    position: absolute;
    inset: 0;
}

.mp-feature-product-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(0, 0, 0, 0.04) 20%, rgba(0, 0, 0, 0.84));
}

.mp-feature-product-card > div {
    position: absolute;
    left: 34px;
    right: 34px;
    bottom: 34px;
    z-index: 1;
}

.mp-feature-product-card span {
    display: inline-block;
    margin-bottom: 14px;
    border-radius: 3px;
    padding: 6px 9px;
    background: rgba(255, 217, 189, 0.22);
    color: #ffd9bd;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 900;
    text-transform: uppercase;
}

.mp-feature-product-card h3 {
    margin: 0 0 12px;
    color: #fff;
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 900;
    line-height: 1.04;
}

.mp-feature-product-card p {
    max-width: 540px;
    margin: 0 0 20px;
    color: #ded4ca;
    line-height: 1.55;
}

.mp-feature-price {
    display: flex;
    align-items: center;
    gap: 6px;
}

.mp-feature-price strong {
    color: #ffd9bd;
    font-size: 28px;
    font-weight: 500;
}

.mp-feature-price small {
    color: #a79d94;
}

.mp-feature-price button {
    margin-left: 22px;
    border: 0;
    border-radius: 999px;
    padding: 11px 22px;
    background: #fff7ef;
    color: #2a1609;
    font-weight: 800;
}


```
