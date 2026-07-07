# Knowledge Document: Marketplace.css (Chunk 23/44)

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
  "chunk_index": 22,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
ont-size: 10px;
    font-weight: 800;
}

.mp-factory-card-head p {
    min-height: 0;
    margin: 5px 0 0;
    color: var(--mp-muted);
    font-size: 13px;
}

.mp-factory-image {
    width: 100%;
    aspect-ratio: 16 / 9;
    margin-bottom: 14px;
    overflow: hidden;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    background: var(--mp-surface-high);
}

.mp-factory-image img,
.mp-profile-image img,
.mp-factory-image-preview img {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: cover;
}

.mp-availability {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    border-radius: 999px;
    padding: 6px 9px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 800;
}

.mp-availability.available {
    background: rgba(22, 163, 74, 0.12);
    color: #15803d;
}

.mp-availability.limited {
    background: rgba(217, 119, 6, 0.12);
    color: #b45309;
}

.mp-availability.booked {
    background: rgba(220, 38, 38, 0.12);
    color: #b91c1c;
}

.mp-availability.unknown {
    background: #fbf7f1;
    color: #5b3a1f;
}

.mp-factory-trust {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-block: 1px solid var(--mp-outline);
    padding: 12px 0;
    margin-bottom: 14px;
}

.mp-factory-trust span {
    color: var(--mp-muted);
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
}

.mp-factory-trust strong {
    color: var(--mp-heading);
    font-family: 'JetBrains Mono', monospace;
    font-size: 18px;
}

.mp-card-capacity-grid,
.mp-profile-grid,
.mp-profile-side-metrics {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 10px;
}

.mp-card-capacity-grid {
    grid-template-columns: repeat(5, minmax(0, 1fr));
}

.mp-capacity-metric {
    min-width: 0;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: 10px;
    background: var(--mp-surface-high);
}

.mp-capacity-metric strong {
    display: block;
    margin-top: 6px;
    color: var(--mp-heading);
    font-size: 13px;
    line-height: 1.35;
    overflow-wrap: anywhere;
}

.mp-verification-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
    margin: 14px 0;
}

.mp-verification-strip span {
    border: 1px solid var(--mp-outline);
    border-radius: 999px;

```
