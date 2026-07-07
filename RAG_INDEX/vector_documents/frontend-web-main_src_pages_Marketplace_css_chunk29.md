# Knowledge Document: Marketplace.css (Chunk 30/44)

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
  "chunk_index": 29,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
nospace;
    font-size: 12px;
    font-weight: 900;
    cursor: pointer;
}

.mp-manufacturing-market .mp-factory-grid {
    grid-template-columns: repeat(auto-fill, minmax(280px, 340px));
    gap: 22px;
    justify-content: start;
}

.mp-manufacturing-market .mp-factory-card {
    overflow: hidden;
    width: 100%;
    max-width: 340px;
    padding: 0;
    border-color: rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    background: #202325;
    box-shadow: none;
}

.mp-manufacturing-market .mp-factory-image {
    position: relative;
    aspect-ratio: 16 / 9;
    max-height: 190px;
    margin: 0;
    border: 0;
    border-radius: 0;
    background: #171a1b;
}

.mp-card-ribbon {
    position: absolute;
    left: 14px;
    top: 12px;
    border-radius: 4px;
    padding: 5px 8px;
    background: rgba(30, 18, 10, 0.78);
    color: #ffd9bd;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    font-weight: 900;
}

.mp-manufacturing-market .mp-factory-card-head {
    margin: 0;
    padding: 18px 18px 8px;
}

.mp-manufacturing-market .mp-factory-card h3 {
    color: #fff7ef;
    font-size: 17px;
}

.mp-manufacturing-market .mp-factory-card-head p {
    display: -webkit-box;
    min-height: 42px;
    margin-top: 8px;
    color: #a79d94;
    line-height: 1.55;
    overflow: hidden;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
}

.mp-card-rating {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    color: #ffd16a;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
}

.mp-card-rating .material-symbols-outlined {
    font-size: 15px;
    font-variation-settings: 'FILL' 1, 'wght' 500, 'GRAD' 0, 'opsz' 20;
}

.mp-card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    padding: 0 18px 16px;
}

.mp-card-tags span {
    border-radius: 4px;
    padding: 5px 8px;
    background: rgba(255, 255, 255, 0.06);
    color: #cfc5bd;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
}

.mp-manufacturing-market .mp-factory-actions {
    display: grid;
    grid-template-columns: 1fr;
    padding: 0 18px 18px;
}

.mp-manufacturing-market .mp-factory-actions button {
    min-height: 42px;
    border-color: rgba(255, 255, 255, 0.07);
    border-radius: 5px;
    background: #2b2e30;
    color: #fff7ef;
    font-family: 'Montserrat', sans-serif;

```
