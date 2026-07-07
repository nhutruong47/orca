# Knowledge Document: Marketplace.css (Chunk 15/44)

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
  "chunk_index": 14,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
);
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
    align-items: end;
    justify-content: space-between;
    gap: 24px;
    margin-bottom: 28px;
}

.mp-section-title-row h2,
.mp-arrivals-header h2 {
    margin: 0;
    font-family: 'Montserrat', sans-serif;
    font-size: 24px;
    font-weight: 900;
    color: var(--mp-heading);
    background: none;
    -webkit-text-fill-color: currentColor;
    text-shadow: 0 1px 0 rgba(255, 255, 255, 0.35);
}

.mp-section-title-row p {
    margin: 5px 0 0;
    color: var(--mp-muted);
}

.mp-section-title-row button {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: transparent;
    color: var(--mp-primary);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
}

.mp-partner-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 24px;
}

.mp-partner-card {
    overflow: hidden;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    background: var(--mp-surface);
    transition: transform 0.28s ease, border-color 0.28s ease;
}

.mp-partner-card:hover {
    transform: translateY(-4px);
    border-color: rgba(255, 221, 195, 0.3);
}

.mp-partner-image {
    position: relative;
    height: 196px;
    overflow: hidden;
}

.mp-partner-image img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.55s ease;
}

.mp-partner-card:hover .mp-partner-image img {
    transform: scale(1.08);
}

.mp-partner-image span {
    position: absolute;
    top: 14px;
    left: 14px;
    border-radius: 999px;
    padding: 6px 10px;
    background: rgba(0, 0, 0, 0.62);
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

```
