# Knowledge Document: Marketplace.css (Chunk 35/44)

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
  "chunk_index": 34,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
plate-columns: minmax(0, 1fr) 108px;
    gap: 10px;
}

.mp-publish-upload-group > input {
    margin-top: 10px;
}

.mp-publish-upload,
.mp-publish-file {
    display: grid;
    place-items: center;
    gap: 6px;
    border: 1px dashed #3b3b3b;
    border-radius: 6px;
    background: rgba(255, 255, 255, 0.025);
    color: #d7d0c9;
    cursor: pointer;
}

.mp-publish-upload {
    min-height: 132px;
    padding: 18px 14px;
    text-align: center;
}

.mp-publish-upload input,
.mp-publish-file input {
    position: absolute;
    width: 1px;
    height: 1px;
    opacity: 0;
    pointer-events: none;
}

.mp-publish-upload .material-symbols-outlined {
    color: #e7a766;
    font-size: 34px;
}

.mp-publish-upload strong {
    color: #f4f1ec;
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: 13px;
}

.mp-publish-upload small {
    color: #8c8c8c;
    font-size: 12px;
}

.mp-publish-file {
    min-height: 42px;
    grid-template-columns: auto auto;
    justify-content: center;
    margin-top: 10px;
    padding: 8px 12px;
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: 12px;
    font-weight: 800;
}

.mp-publish-file .material-symbols-outlined {
    color: #e7a766;
    font-size: 20px;
}

.mp-publish-sheet .mp-factory-image-preview-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 10px;
}

.mp-publish-sheet .mp-factory-image-preview {
    margin-top: 0;
}

.mp-publish-sheet .mp-factory-image-preview img {
    border-color: #333;
    border-radius: 6px;
}

.mp-publish-sheet .mp-factory-image-preview button {
    border-color: #3d3d3d;
    color: #e8d8c8;
}

.mp-publish-sheet .mp-verification-form {
    margin-top: 24px;
    border-color: rgba(231, 179, 127, 0.18);
    border-radius: 6px;
    padding: 16px;
    background: #151515;
}

.mp-publish-sheet .mp-verification-form h3 {
    color: #f4f1ec;
    font-family: 'Montserrat', system-ui, sans-serif;
}

.mp-publish-sheet .mp-verification-form p {
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

```
