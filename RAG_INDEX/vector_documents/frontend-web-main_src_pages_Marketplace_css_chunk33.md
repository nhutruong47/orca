# Knowledge Document: Marketplace.css (Chunk 34/44)

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
  "chunk_index": 33,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
m-group input,
.mp-publish-sheet .mp-form-group select,
.mp-publish-sheet .mp-form-group textarea {
    min-height: 48px;
    border: 1px solid #2d2d2d;
    border-radius: 4px;
    background: #1b1b1b;
    color: #f1eee8;
    padding: 12px;
    font-size: 14px;
    box-shadow: none;
}

.mp-publish-sheet .mp-form-group select {
    color-scheme: dark;
}

.mp-publish-sheet .mp-form-group textarea {
    min-height: 112px;
    resize: vertical;
    line-height: 1.55;
}

.mp-publish-sheet .mp-form-group input::placeholder,
.mp-publish-sheet .mp-form-group textarea::placeholder {
    color: #707780;
}

.mp-publish-sheet .mp-form-group input:focus,
.mp-publish-sheet .mp-form-group select:focus,
.mp-publish-sheet .mp-form-group textarea:focus {
    border-color: #e7b37f;
    box-shadow: 0 0 0 3px rgba(231, 179, 127, 0.12);
}

.mp-publish-chip-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.mp-publish-chip-grid button {
    min-height: 34px;
    border: 1px solid #3d3d3d;
    border-radius: 999px;
    padding: 8px 15px;
    background: linear-gradient(180deg, #343434, #292929);
    color: #f3eee8;
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: 11px;
    font-weight: 800;
    cursor: pointer;
    transition: border-color 0.18s ease, background 0.18s ease, color 0.18s ease;
}

.mp-publish-chip-grid button.selected {
    border-color: #e7b37f;
    background: rgba(231, 179, 127, 0.18);
    color: #ffd9b6;
}

.mp-publish-section {
    margin: 28px 0 18px;
}

.mp-publish-section h3 {
    position: relative;
    margin: 0;
    padding-left: 12px;
    color: #ece8e1;
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: 20px;
    font-weight: 850;
    line-height: 1.25;
}

.mp-publish-section h3::before {
    content: '';
    position: absolute;
    left: 0;
    top: 2px;
    bottom: 2px;
    width: 3px;
    border-radius: 999px;
    background: #e7a766;
}

.mp-publish-capacity-row {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 108px;
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

```
