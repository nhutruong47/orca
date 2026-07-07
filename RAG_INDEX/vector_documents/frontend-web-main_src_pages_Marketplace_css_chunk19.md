# Knowledge Document: Marketplace.css (Chunk 20/44)

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
  "chunk_index": 19,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
ly: 'Montserrat', sans-serif;
}

.mp-side-product p {
    margin: 0 20px 22px;
    color: var(--mp-muted);
}

.mp-cta {
    margin-top: 60px;
    border: 1px solid rgba(255, 221, 195, 0.18);
    border-radius: 8px;
    padding: clamp(36px, 6vw, 56px);
    text-align: center;
    background: rgba(255, 221, 195, 0.05);
}

.mp-cta h2 {
    margin: 0 0 14px;
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(2rem, 4vw, 3rem);
    color: var(--mp-primary);
}

.mp-cta p {
    max-width: 680px;
    margin: 0 auto 28px;
    color: var(--mp-muted);
    font-size: 18px;
}

.mp-showcase-footer {
    margin-top: 60px;
    padding: 30px 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    border-top: 1px solid var(--mp-outline);
    color: var(--mp-muted);
}

.mp-showcase-footer span {
    color: var(--mp-primary);
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
}

.mp-showcase-footer div {
    display: flex;
    gap: 22px;
}

.mp-showcase-footer a:hover {
    color: var(--mp-primary);
}

.mp-styled-empty .material-symbols-outlined {
    font-size: 48px;
    opacity: 0.5;
}

@media (min-width: 1420px) {
    .mp-partner-grid {
        grid-template-columns: repeat(4, minmax(0, 1fr));
    }
}

@media (max-width: 1180px) {
    .mp-quick-widget {
        display: none;
    }

    .mp-partner-grid,
    .mp-arrivals-grid {
        grid-template-columns: 1fr 1fr;
    }

    .mp-feature-product {
        grid-column: 1 / -1;
    }
}

@media (max-width: 860px) {
    .mp-sidenav {
        display: none;
    }

    .mp-topbar {
        left: 0;
    }

    .mp-main {
        margin-left: 0;
    }

    .mp-partner-grid,
    .mp-arrivals-grid {
        grid-template-columns: 1fr;
    }

    .mp-feature-product {
        min-height: 520px;
    }

    .mp-section-title-row,
    .mp-showcase-footer {
        align-items: flex-start;
        flex-direction: column;
    }

    .mp-workshop-detail {
        grid-template-columns: 1fr;
        overflow-y: auto;
    }

    .mp-detail-media {
        min-height: 320px;
    }
}

@media (max-width: 560px) {
    .mp-topbar {
        height: auto;
        align-items: stretch;
        flex-direction: column;
        padding-block: 12px;
    }

    .mp-top-actions {
        justify-content: space-between;
    }

    .mp-main {
        padding-top: 138px;
    }


```
