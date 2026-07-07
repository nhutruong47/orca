# Knowledge Document: Marketplace.css (Chunk 37/44)

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
  "chunk_index": 36,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
3px;
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
    background: var(--mp-surface-high, var(--bg-tertiary));
}

.mp-factory-image-preview button {
    width: fit-content;
    border: 1px solid var(--mp-outline, var(--border));
    border-radius: 8px;
    padding: 8px 12px;
    background: transparent;
    color: var(--mp-muted, var(--text-secondary));
    cursor: pointer;
}

.mp-verification-status {
    border-radius: 8px;
    padding: 10px 12px;
    font-size: 12px;
    font-weight: 800;
    white-space: nowrap;
}

.mp-verification-status.not_submitted {
    background: #f7efe3;
    color: #6b4321;
}

.mp-verification-status.pending {
    background: rgba(217, 119, 6, 0.12);
    color: #b45309;
}

.mp-verification-status.approved {
    background: rgba(22, 163, 74, 0.12);
    color: #15803d;
}

.mp-verification-status.rejected {
    background: rgba(220, 38, 38, 0.12);
    color: #b91c1c;
}

@media (max-width: 1180px) {
    .mp-manufacturing-market .mp-main {
        --mp-page-max: min(100%, 930px);
    }

    .mp-market-hero,
    .mp-profile-detail {
        grid-template-columns: 1fr;
    }

    .mp-product-grid {
        grid-template-columns: 1fr;
    }

    .mp-product-side-list {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .mp-filter-grid {
        grid-template-columns: repeat(3, minmax(0, 1fr));
    }

    .mp-factory-grid,
    .mp-request-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .mp-card-capacity-grid {
        grid-template-columns: repeat(3, minmax(0, 1fr));
    }
}

@media (max-width: 720px) {
    .mp-verification-form-head {
        display: grid;
    }

    .mp-filter-grid,
    .mp-verification-grid {
        grid-template-columns: 1fr;
    }

    .mp-filter-footer {
        align-items: flex-start;
        flex-direction: column;
    }

    .mp-verification-status {
        width: fit-content;
        white-space: normal;
    }
}

@media (max-width: 720px) {
    .mp-factory-grid,
    .mp-request-grid,
    .mp-factory-image-preview-grid,

```
