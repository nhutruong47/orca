# Knowledge Document: Marketplace.css (Chunk 33/44)

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
  "chunk_index": 32,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
rket .mp-showcase-footer {
    margin-top: 88px;
    border-top-color: rgba(255, 255, 255, 0.08);
}

.mp-manufacturing-market .mp-showcase-footer span {
    color: #ffd9bd;
}

.mp-publish-sheet-overlay {
    position: fixed;
    inset: 0;
    z-index: 120;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.64);
    backdrop-filter: blur(10px);
    padding: 20px;
}

.mp-publish-sheet {
    width: min(800px, 100vw);
    max-height: 90vh;
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.08), transparent 72px),
        #111111;
    color: #f4f1ec;
    box-shadow: 0 24px 80px rgba(0, 0, 0, 0.6);
}

.mp-publish-header {
    position: sticky;
    top: 0;
    z-index: 2;
    height: 64px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 0 22px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    background: linear-gradient(180deg, #3f3c39 0%, #1b1b1b 100%);
}

.mp-publish-header h2 {
    margin: 0;
    color: #e7b37f;
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: 18px;
    font-weight: 800;
    line-height: 1.2;
}

.mp-publish-back {
    width: 30px;
    height: 30px;
    display: grid;
    place-items: center;
    border: 0;
    border-radius: 50%;
    background: transparent;
    color: #e7b37f;
    cursor: pointer;
}

.mp-publish-back:hover {
    background: rgba(231, 179, 127, 0.12);
}

.mp-publish-form {
    flex: 1;
    overflow-y: auto;
    padding: 22px 22px 22px;
    scrollbar-color: #e7b37f #151515;
}

.mp-publish-sheet .mp-form-group {
    margin-bottom: 20px;
}

.mp-publish-sheet .mp-form-group label {
    margin-bottom: 8px;
    color: #d7d0c9;
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: 12px;
    font-weight: 750;
    text-transform: none;
    letter-spacing: 0;
}

.mp-publish-sheet .mp-form-group input,
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

```
