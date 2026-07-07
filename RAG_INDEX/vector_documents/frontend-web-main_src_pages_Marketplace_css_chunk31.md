# Knowledge Document: Marketplace.css (Chunk 32/44)

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
  "chunk_index": 31,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
ure-price {
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

.mp-product-side-list {
    display: grid;
    gap: 22px;
}

.mp-product-card img {
    height: 170px;
}

.mp-product-card > div {
    padding: 18px;
}

.mp-product-card h3 {
    margin: 0 0 8px;
    color: #fff7ef;
    font-family: 'Montserrat', sans-serif;
    font-size: 16px;
}

.mp-product-card p {
    min-height: 40px;
    margin: 0 0 24px;
    color: #a79d94;
    font-size: 12px;
    line-height: 1.55;
}

.mp-product-card div div {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.mp-product-card strong {
    color: #fff7ef;
    font-size: 15px;
}

.mp-product-card button {
    width: 34px;
    height: 34px;
    display: grid;
    place-items: center;
    border: 0;
    border-radius: 10px;
    background: #171a1b;
    color: #ffd9bd;
}

.mp-manufacturing-market .mp-open-requests {
    display: none;
}

.mp-manufacturing-market .mp-cta {
    margin-top: 64px;
    border-color: rgba(255, 217, 189, 0.18);
    border-radius: 14px;
    padding: clamp(42px, 6vw, 58px);
    background:
        radial-gradient(circle at 50% 0%, rgba(255, 181, 121, 0.15), transparent 52%),
        linear-gradient(135deg, #2a2726, #1c1d1e);
}

.mp-manufacturing-market .mp-cta h2 {
    color: #ffd9bd;
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(2rem, 4vw, 3rem);
}

.mp-manufacturing-market .mp-cta p {
    color: #efe2d5;
    font-size: 14px;
}

.mp-manufacturing-market .mp-cta small {
    display: block;
    margin-top: 18px;
    color: #8f8580;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
}

.mp-manufacturing-market .mp-showcase-footer {
    margin-top: 88px;
    border-top-color: rgba(255, 255, 255, 0.08);
}

.mp-manufacturing-market .mp-showcase-footer span {
    color: #ffd9bd;
}

.mp-publish-sheet-overlay {
    position: fixed;
    inset: 0;
    z-index: 120;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.64);
    backdrop-filter: blur(10px);

```
