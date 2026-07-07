# Knowledge Document: Marketplace.css (Chunk 16/44)

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
  "chunk_index": 15,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
2);
    color: var(--mp-primary-strong);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
}

.mp-partner-body {
    padding: 22px;
}

.mp-partner-heading {
    display: flex;
    align-items: start;
    justify-content: space-between;
    gap: 16px;
    margin-bottom: 10px;
}

.mp-partner-heading h3 {
    margin: 0;
    font-family: 'Montserrat', sans-serif;
    font-size: 20px;
}

.mp-partner-heading strong {
    display: inline-flex;
    align-items: center;
    gap: 3px;
    color: var(--mp-primary-strong);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
}

.mp-partner-heading .material-symbols-outlined {
    font-size: 18px;
    font-variation-settings: 'FILL' 1;
}

.mp-partner-body p {
    min-height: 52px;
    margin: 0 0 18px;
    color: var(--mp-muted);
    font-size: 14px;
    line-height: 1.55;
}

.mp-partner-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 20px;
}

.mp-partner-tags span {
    border: 1px solid var(--mp-outline);
    border-radius: 4px;
    padding: 4px 7px;
    background: var(--mp-surface-high);
    color: var(--mp-muted);
    font-family: 'Montserrat', sans-serif;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
}

.mp-partner-actions {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}

.mp-partner-body button {
    width: 100%;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: 10px;
    background: var(--mp-surface-high);
    color: var(--mp-text);
    font-family: 'JetBrains Mono', monospace;
    cursor: pointer;
}

.mp-partner-body button:hover {
    background: var(--mp-primary);
    color: #4c2700;
}

.mp-partner-actions button:last-child {
    border-color: rgba(255, 221, 195, 0.28);
    background: #ffb87b;
    color: #2e1500;
    font-weight: 800;
}

.mp-workshop-detail {
    width: min(1040px, calc(100vw - 32px));
    max-height: min(860px, calc(100vh - 32px));
    display: grid;
    grid-template-columns: minmax(280px, 0.9fr) minmax(0, 1.1fr);
    overflow: hidden;
    position: relative;
    border: 1px solid var(--mp-outline);
    border-radius: 10px;
    background: #1a1c1e;
    box-shadow: 0 28px 90px rgba(0, 0, 0, 0.58);
}

.mp-detail-close {
    position: absolute;
    top: 14px;
    right: 14px;
    z-index: 3;
    width: 38px;
    height: 38px;
    display: grid;

```
