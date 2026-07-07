# Knowledge Document: Marketplace.css (Chunk 21/44)

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
  "chunk_index": 20,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
-template-columns: 1fr;
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

    .mp-showcase-hero {
        min-height: 520px;
    }

    .mp-showcase-content {
        padding: 28px 22px;
    }

    .mp-hero-buttons {
        flex-direction: column;
    }

    .mp-detail-content {
        padding: 22px;
    }

    .mp-detail-summary,
    .mp-detail-grid,
    .mp-detail-actions {
        grid-template-columns: 1fr;
    }

    .mp-detail-actions {
        margin: 24px -22px -22px;
        padding: 16px 22px;
    }

    .mp-partner-actions {
        grid-template-columns: 1fr;
    }
}

/* === B2B Manufacturing Marketplace Flow === */
.mp-manufacturing-market .mp-main {
    --mp-page-max: 1560px;
}

.mp-market-hero,
.mp-compare-panel,
.mp-open-requests {
    max-width: var(--mp-page-max);
    margin-inline: auto;
}

.mp-market-hero {
    margin-bottom: 32px;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: clamp(28px, 4vw, 48px);
    background:
        linear-gradient(135deg, rgba(255, 252, 248, 0.96), rgba(246, 241, 232, 0.9)),
        var(--mp-surface);
}

.mp-filter-panel {
    max-width: var(--mp-page-max);
    margin: 0 auto 30px;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: 18px;
    background: var(--mp-surface);
}

.mp-filter-grid {
    display: grid;
    grid-template-columns: repeat(6, minmax(0, 1fr));
    gap: 12px;
}

.mp-filter-panel .mp-form-group {
    margin-bottom: 0;
}

.mp-filter-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-top: 14px;
    padding-top: 14px;
    border-top: 1px solid var(--mp-outline);
    color: var(--mp-muted);
    font-size: 13px;
    font-weight: 700;
}

.mp-filter-footer button {
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    padding: 8px 12px;
    background: var(--mp-surface-high);
    color: var(--mp-text);
    cursor: pointer;
}

body.theme-dark .mp-market-hero {
    background:

```
