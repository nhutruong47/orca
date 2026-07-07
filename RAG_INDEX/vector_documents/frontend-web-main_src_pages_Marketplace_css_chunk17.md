# Knowledge Document: Marketplace.css (Chunk 18/44)

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
  "chunk_index": 17,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
x;
    padding: 14px;
    background: rgba(255, 255, 255, 0.035);
}

.mp-detail-summary span,
.mp-detail-grid span {
    display: block;
    margin-bottom: 6px;
    color: rgba(214, 195, 181, 0.64);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
}

.mp-detail-summary strong {
    color: var(--mp-primary);
    font-size: 24px;
}

.mp-detail-desc {
    margin: 0 0 22px;
    color: rgba(226, 226, 229, 0.82);
    line-height: 1.7;
}

.mp-detail-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 24px;
}

.mp-detail-grid strong {
    color: var(--mp-text);
    line-height: 1.45;
}

.mp-detail-section {
    margin-top: 22px;
}

.mp-detail-section h3 {
    margin: 0 0 12px;
    color: var(--mp-primary);
    font-family: 'Montserrat', sans-serif;
    font-size: 16px;
}

.mp-detail-section p {
    margin: 0 0 12px;
    color: rgba(214, 195, 181, 0.72);
    line-height: 1.65;
}

.mp-detail-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.mp-detail-tags span {
    border: 1px solid var(--mp-outline);
    border-radius: 999px;
    padding: 7px 10px;
    background: rgba(255, 255, 255, 0.04);
    color: rgba(226, 226, 229, 0.82);
    font-size: 12px;
}

.mp-detail-actions {
    position: sticky;
    bottom: -34px;
    display: grid;
    grid-template-columns: 0.8fr 1.2fr;
    gap: 12px;
    margin: 28px -34px -34px;
    padding: 18px 34px;
    border-top: 1px solid var(--mp-outline);
    background: rgba(26, 28, 30, 0.94);
    backdrop-filter: blur(10px);
}

.mp-detail-actions button {
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: 12px 16px;
    background: var(--mp-surface-high);
    color: var(--mp-text);
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    cursor: pointer;
}

.mp-detail-actions button:last-child {
    border: 0;
    background: #ffb87b;
    color: #2e1500;
}

.mp-arrivals {
    margin-top: 58px;
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

```
