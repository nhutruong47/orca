# Knowledge Document: Marketplace.css (Chunk 14/44)

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
  "chunk_index": 13,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
p-muted);
}

.mp-quick-widget strong {
    color: var(--mp-text);
}

.mp-quick-widget button {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-top: 14px;
    padding: 10px;
    border: 1px solid var(--mp-outline);
    background: var(--mp-surface-high);
    color: var(--mp-primary-strong);
}

body.theme-dark .mp-showcase-overlay {
    background: linear-gradient(90deg, rgba(18, 20, 22, 0.98), rgba(18, 20, 22, 0.7) 48%, rgba(18, 20, 22, 0.15));
}

body.theme-dark .mp-showcase-content p {
    color: rgba(214, 195, 181, 0.82);
}

body.theme-dark .mp-quick-widget {
    background: rgba(26, 28, 30, 0.8);
}

body.theme-dark .mp-quick-widget h3 {
    color: var(--mp-primary);
}

body.theme-dark .mp-quick-widget div {
    color: rgba(226, 226, 229, 0.62);
}

body.theme-dark .mp-quick-widget button {
    border-color: rgba(255, 221, 195, 0.22);
    background: rgba(255, 255, 255, 0.05);
}

.mp-filter-row {
    max-width: var(--mp-page-max);
    margin: 0 auto 38px;
    display: flex;
    align-items: center;
    gap: 12px;
    overflow-x: auto;
    padding-bottom: 4px;
}

.mp-filter-row button {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    white-space: nowrap;
    border: 1px solid var(--mp-outline);
    border-radius: 999px;
    padding: 10px 18px;
    background: var(--mp-surface-high);
    color: var(--mp-muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    cursor: pointer;
}

.mp-filter-row button.active {
    background: #3b2312;
    border-color: #3b2312;
    color: #fff4e6;
}

.mp-filter-row button .material-symbols-outlined {
    color: currentColor;
}

.mp-filter-row button:not(.active):hover {
    background: #fffaf3;
    border-color: #b97a3e;
    color: #2b180c;
}

.mp-filter-row .mp-result-count {
    margin-left: auto;
}

.mp-published-panel,
.mp-partner-section,
.mp-arrivals,
.mp-cta,
.mp-showcase-footer {
    max-width: var(--mp-page-max);
    margin-inline: auto;
}

.mp-published-panel {
    margin-bottom: 36px;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: 18px;
    background: var(--mp-surface);
}

.mp-published-panel h3 {
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 0 0 12px;
    color: var(--mp-muted);
    font-size: 14px;
}

.mp-section-title-row {
    display: flex;

```
