# Knowledge Document: Marketplace.css (Chunk 25/44)

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
  "chunk_index": 24,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
equest-card > span {
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
    margin: 14px 0;
}

.mp-request-card dd {
    margin: 4px 0 0;
    color: var(--mp-heading);
    font-weight: 800;
}

.mp-request-card p {
    margin: 0;
    color: var(--mp-muted);
    line-height: 1.55;
}

.mp-profile-detail {
    grid-template-columns: 340px minmax(0, 1fr);
    background: var(--mp-surface);
}

.mp-profile-side {
    padding: 30px;
    background: var(--mp-surface-high);
    border-right: 1px solid var(--mp-outline);
}

.mp-profile-image {
    width: 100%;
    aspect-ratio: 4 / 3;
    margin-top: 18px;
    overflow: hidden;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    background: var(--mp-surface);
}

.mp-profile-side h2 {
    margin: 18px 0 8px;
    color: var(--mp-heading);
    font-family: 'Montserrat', sans-serif;
    font-size: 30px;
    line-height: 1.08;
}

.mp-profile-side p {
    color: var(--mp-muted);
}

.mp-profile-side-metrics {
    grid-template-columns: 1fr;
    margin: 22px 0;
}

.mp-profile-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 22px;
}

.mp-profile-tabs button {
    border: 1px solid var(--mp-outline);
    border-radius: 999px;
    padding: 8px 12px;
    background: var(--mp-surface-high);
    color: var(--mp-muted);
    cursor: pointer;
}

.mp-profile-tabs button.active {
    background: var(--mp-primary);
    color: #4c2700;
}

.mp-profile-overview > p,
.mp-empty-inline,
.mp-modal-note {
    color: var(--mp-muted);
    line-height: 1.65;
}

.mp-empty-inline {
    border: 1px dashed var(--mp-outline);
    border-radius: 8px;
    padding: 16px;
    background: var(--mp-surface-high);
}

.mp-verification-list {
    display: grid;
    gap: 8px;
}

.mp-verification-list span {
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--mp-muted);
    font-weight: 700;
}

.mp-verification-list .verified {
    color: var(--mp-success);
}

.mp-review-list {
    display: grid;
    gap: 12px;
}

.mp-review-list article {

```
