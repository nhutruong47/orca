# Knowledge Document: Marketplace.css (Chunk 29/44)

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
  "chunk_index": 28,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
r: #a89f98;
    font-size: 12px;
}

.mp-hero-control-card dd {
    margin: 0;
    color: #fff;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 900;
}

.mp-hero-control-card button {
    width: 100%;
    min-height: 42px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    border: 1px solid rgba(255, 181, 121, 0.28);
    border-radius: 6px;
    background: rgba(255, 181, 121, 0.08);
    color: #ffd4b4;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 900;
    cursor: pointer;
}

.mp-category-row {
    max-width: var(--mp-page-max);
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin: 0 auto 36px;
}

.mp-category-row button {
    min-height: 38px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 0 18px;
    background: #25282a;
    color: #efe7dd;
    font-family: 'Montserrat', sans-serif;
    font-size: 13px;
    font-weight: 800;
    cursor: pointer;
}

.mp-category-row button.active {
    border-color: transparent;
    background: #ffd9bd;
    color: #2a1609;
}

.mp-category-row .material-symbols-outlined {
    font-size: 17px;
}

.mp-manufacturing-market .mp-section-title-row {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 24px;
}

.mp-manufacturing-market .mp-section-title-row h2 {
    margin: 0;
    color: #fff7ef;
    font-family: 'Montserrat', sans-serif;
    font-size: 23px;
    font-weight: 900;
}

.mp-manufacturing-market .mp-section-title-row p {
    margin: 4px 0 0;
    color: #a79d94;
    font-size: 13px;
}

.mp-view-all-btn,
.mp-manufacturing-market .mp-section-title-row > button {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    border: 0;
    background: transparent;
    color: #ffd9bd;
    font-family: 'JetBrains Mono', monospace;
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

```
