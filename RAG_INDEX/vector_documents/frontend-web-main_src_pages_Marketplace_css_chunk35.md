# Knowledge Document: Marketplace.css (Chunk 36/44)

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
  "chunk_index": 35,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
 p {
    color: #9d948c;
}

.mp-publish-sheet .mp-verification-grid {
    grid-template-columns: 1fr;
}

.mp-publish-sheet .mp-verification-wide {
    grid-column: 1 / -1;
}

.mp-publish-sheet .mp-verification-status.not_submitted {
    background: rgba(231, 179, 127, 0.14);
    color: #ffd9b6;
}

.mp-publish-bottom-bar {
    position: sticky;
    bottom: -22px;
    z-index: 2;
    display: grid;
    grid-template-columns: 0.82fr 1.18fr;
    gap: 10px;
    margin: 26px -22px -22px;
    padding: 14px 18px 18px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(18, 18, 18, 0.9);
    backdrop-filter: blur(14px);
}

.mp-publish-bottom-bar .mp-cancel-btn,
.mp-publish-bottom-bar .mp-submit-btn {
    min-height: 46px;
    border-radius: 999px;
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: 13px;
    font-weight: 850;
}

.mp-publish-bottom-bar .mp-cancel-btn {
    border-color: #3a3a3a;
    background: #222;
    color: #f1eee8;
}

.mp-publish-bottom-bar .mp-submit-btn {
    background: #eceff3;
    color: #1f1f1f;
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.28);
}

.mp-verification-form {
    margin-top: 18px;
    border: 1px solid rgba(139, 94, 60, 0.22);
    border-radius: 10px;
    padding: 18px;
    background: #fffaf3;
}

.mp-verification-form h3 {
    margin: 0 0 6px;
    color: #24150a;
    font-size: 17px;
}

.mp-verification-form p {
    margin: 0;
    color: #6b5343;
    font-size: 14px;
    line-height: 1.55;
}

.mp-verification-form-head {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 14px;
    margin-bottom: 16px;
}

.mp-verification-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
}

.mp-verification-note {
    margin-bottom: 14px;
    border: 1px solid rgba(220, 38, 38, 0.18);
    border-radius: 8px;
    padding: 10px 12px;
    background: #fff1f2;
    color: #b91c1c;
    font-size: 13px;
    font-weight: 700;
}

.mp-factory-image-preview {
    margin-top: 10px;
    display: grid;
    gap: 8px;
}

.mp-factory-image-preview-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 10px;
    margin-top: 10px;
}

.mp-factory-image-preview img {
    aspect-ratio: 16 / 9;
    border: 1px solid var(--mp-outline, var(--border));
    border-radius: 8px;

```
