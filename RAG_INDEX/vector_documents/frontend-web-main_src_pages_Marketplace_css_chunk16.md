# Knowledge Document: Marketplace.css (Chunk 17/44)

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
  "chunk_index": 16,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
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
    place-items: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    background: rgba(18, 20, 22, 0.78);
    color: var(--mp-text);
    cursor: pointer;
}

.mp-detail-media {
    min-height: 620px;
    position: relative;
    overflow: hidden;
}

.mp-detail-media img {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: cover;
    filter: grayscale(0.35) brightness(0.84);
}

.mp-detail-media__overlay {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 34px;
    background: linear-gradient(180deg, transparent 20%, rgba(0, 0, 0, 0.82));
}

.mp-detail-media__overlay span {
    width: fit-content;
    margin-bottom: 12px;
    padding: 6px 10px;
    border-radius: 999px;
    background: rgba(255, 221, 195, 0.12);
    color: var(--mp-primary-strong);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
}

.mp-detail-media__overlay h2 {
    margin: 0 0 8px;
    color: #fff;
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(2rem, 4vw, 3rem);
    line-height: 1.05;
}

.mp-detail-media__overlay p {
    margin: 0;
    color: rgba(226, 226, 229, 0.76);
}

.mp-detail-content {
    padding: 34px;
    overflow-y: auto;
    color: var(--mp-text);
}

.mp-detail-summary {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    margin-bottom: 22px;
}

.mp-detail-summary div,
.mp-detail-grid div {
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
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

```
