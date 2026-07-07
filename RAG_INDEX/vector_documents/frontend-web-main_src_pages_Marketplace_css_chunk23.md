# Knowledge Document: Marketplace.css (Chunk 24/44)

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
  "chunk_index": 23,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
r(--mp-surface-high);
}

.mp-capacity-metric strong {
    display: block;
    margin-top: 6px;
    color: var(--mp-heading);
    font-size: 13px;
    line-height: 1.35;
    overflow-wrap: anywhere;
}

.mp-verification-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
    margin: 14px 0;
}

.mp-verification-strip span {
    border: 1px solid var(--mp-outline);
    border-radius: 999px;
    padding: 5px 8px;
    color: var(--mp-muted);
    font-size: 11px;
    font-weight: 700;
}

.mp-factory-actions {
    display: grid;
    grid-template-columns: auto repeat(3, minmax(0, 1fr));
    gap: 8px;
    align-items: center;
}

.mp-factory-actions label {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: var(--mp-muted);
    font-size: 12px;
    font-weight: 700;
}

.mp-factory-actions button {
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: 9px 10px;
    background: var(--mp-surface-high);
    color: var(--mp-text);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    cursor: pointer;
}

.mp-factory-actions button:last-child {
    border-color: transparent;
    background: #ffb87b;
    color: #2e1500;
    font-weight: 900;
}

.mp-factory-actions button:disabled,
.mp-detail-actions button:disabled {
    cursor: not-allowed;
    opacity: 0.55;
    filter: grayscale(0.35);
}

.mp-compare-panel,
.mp-open-requests {
    margin-top: 42px;
}

.mp-compare-table-wrap {
    overflow-x: auto;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    background: var(--mp-surface);
}

.mp-compare-table {
    width: 100%;
    min-width: 720px;
    border-collapse: collapse;
}

.mp-compare-table th,
.mp-compare-table td {
    border-bottom: 1px solid var(--mp-outline);
    padding: 13px 14px;
    text-align: left;
    color: var(--mp-text);
    vertical-align: top;
}

.mp-compare-table th {
    color: var(--mp-muted);
    font-size: 12px;
    text-transform: uppercase;
}

.mp-request-card > span {
    display: inline-block;
    margin-bottom: 10px;
    border-radius: 999px;
    padding: 5px 9px;
    background: var(--mp-surface-high);
    color: var(--mp-primary-strong);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 800;
}

.mp-request-card dl {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 10px;

```
