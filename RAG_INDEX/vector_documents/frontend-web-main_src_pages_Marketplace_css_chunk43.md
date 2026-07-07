# Knowledge Document: Marketplace.css (Chunk 44/44)

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
  "chunk_index": 43,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
g-market .mp-cta p { color: #6b5344; }
body.theme-light .mp-manufacturing-market .mp-cta small { color: #9b8b7e; }

/* Pagination Styles */
.mp-pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 16px;
    margin-top: 40px;
    grid-column: 1 / -1;
}

.mp-pagination button {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: var(--mp-surface-high, #212836);
    color: var(--text-primary, #ece8e1);
    border: 1px solid var(--border, rgba(255,255,255,0.1));
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.2s;
    outline: none;
}

.mp-pagination button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.mp-pagination button:not(:disabled):hover {
    background: var(--bg-hover, rgba(255,255,255,0.05));
    border-color: rgba(255,255,255,0.2);
}

.mp-page-info {
    color: var(--text-muted, #9ca3af);
    font-size: 14px;
    font-weight: 500;
}

body.theme-light .mp-pagination button {
    background: #fffcf8;
    color: #322214;
    border-color: var(--mp-outline);
}

body.theme-light .mp-pagination button:not(:disabled):hover {
    background: #f6f1e8;
    border-color: rgba(50, 34, 20, 0.2);
}

body.theme-light .mp-page-info {
    color: #6b5344;
}


```
