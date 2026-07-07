# Knowledge Document: Marketplace.css (Chunk 13/44)

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
  "chunk_index": 12,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
ified {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 18px;
    border-radius: 999px;
    padding: 7px 12px;
    background: rgba(255, 221, 195, 0.1);
    color: var(--mp-primary-strong);
    font-family: 'Montserrat', sans-serif;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

.mp-showcase-content h1 {
    margin: 0 0 16px;
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(2.2rem, 4vw, 3rem);
    line-height: 1.08;
    color: var(--mp-text);
}

.mp-showcase-content h1 span {
    color: var(--mp-primary-strong);
}

.mp-showcase-content p {
    max-width: 640px;
    margin: 0 0 28px;
    color: var(--mp-muted);
    font-size: 18px;
    line-height: 1.55;
}

.mp-hero-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
}

.mp-hero-buttons button,
.mp-quick-widget button,
.mp-section-title-row button,
.mp-cta button {
    border: 0;
    border-radius: 8px;
    cursor: pointer;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
}

.mp-hero-buttons button:first-child,
.mp-cta button {
    padding: 13px 28px;
    background: #ffb87b;
    color: #2e1500;
}

.mp-hero-buttons button:last-child {
    padding: 13px 28px;
    border: 1px solid var(--mp-outline);
    background: var(--mp-surface-high);
    color: var(--mp-text);
}

.mp-quick-widget {
    position: absolute;
    right: 30px;
    top: 50%;
    z-index: 2;
    width: 286px;
    transform: translateY(-50%);
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: 24px;
    background: rgba(255, 252, 248, 0.84);
    backdrop-filter: blur(8px);
}

.mp-quick-widget h3 {
    margin: 0 0 18px;
    font-family: 'Montserrat', sans-serif;
    color: var(--mp-text);
}

.mp-quick-widget div {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    padding: 9px 0;
    color: var(--mp-muted);
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

```
