# Knowledge Document: Marketplace.css (Chunk 22/44)

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
  "chunk_index": 21,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
;
    padding-top: 14px;
    border-top: 1px solid var(--mp-outline);
    color: var(--mp-muted);
    font-size: 13px;
    font-weight: 700;
}

.mp-filter-footer button {
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: 8px 12px;
    background: var(--mp-surface-high);
    color: var(--mp-text);
    cursor: pointer;
}

body.theme-dark .mp-market-hero {
    background:
        linear-gradient(135deg, rgba(30, 32, 34, 0.98), rgba(18, 20, 22, 0.92)),
        var(--mp-surface);
}

.mp-market-hero h1 {
    max-width: 820px;
    margin: 0 0 16px;
    color: var(--mp-heading);
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(2.1rem, 4vw, 3.7rem);
    line-height: 1.04;
}

.mp-market-hero p {
    max-width: 720px;
    margin: 0 0 24px;
    color: var(--mp-muted);
    font-size: 17px;
    line-height: 1.65;
}

.mp-capacity-metric span,
.mp-request-card dt {
    display: block;
    color: var(--mp-muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.mp-factory-grid,
.mp-request-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 18px;
}

.mp-factory-card,
.mp-request-card {
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: 18px;
    background: var(--mp-surface);
    box-shadow: 0 18px 46px rgba(50, 34, 20, 0.06);
}

.mp-factory-card-head {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 14px;
    margin-bottom: 14px;
}

.mp-factory-card h3,
.mp-request-card h3 {
    margin: 0;
    color: var(--mp-heading);
    font-family: 'Montserrat', sans-serif;
    font-size: 18px;
}

.mp-own-factory-badge {
    display: inline-flex;
    vertical-align: middle;
    margin-left: 8px;
    border-radius: 999px;
    padding: 4px 7px;
    background: rgba(22, 163, 74, 0.12);
    color: #15803d;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 800;
}

.mp-factory-card-head p {
    min-height: 0;
    margin: 5px 0 0;
    color: var(--mp-muted);
    font-size: 13px;
}

.mp-factory-image {
    width: 100%;
    aspect-ratio: 16 / 9;
    margin-bottom: 14px;
    overflow: hidden;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    background: var(--mp-surface-high);
}

.mp-factory-image img,

```
