# Knowledge Document: Marketplace.css (Chunk 9/44)

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
  "chunk_index": 8,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
ver {
    border-color: var(--accent-primary);
}

.mp-submit-btn {
    flex: 1;
    background: var(--accent-gradient);
    color: #fff;
    border: none;
    padding: 0.6rem;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.2s;
    box-shadow: var(--shadow-sm);
}

.mp-submit-btn:hover:not(:disabled) {
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.mp-submit-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

/* Responsive */
@media (max-width: 768px) {
    .mp-header {
        padding: 0.8rem 1.5rem;
    }

    .mp-hero {
        padding: 3rem 1.5rem 2rem;
    }

    .mp-hero h1 {
        font-size: 1.8rem;
    }

    .mp-search-section {
        padding: 1rem 1.5rem;
    }

    .mp-my-published {
        padding: 1rem 1.5rem;
    }

    .mp-section {
        padding: 1.5rem;
    }

    .mp-grid {
        grid-template-columns: 1fr;
    }

    .mp-form-row {
        flex-direction: column;
    }
}

/* === Marketplace Showcase Style === */
.mp-market-style {
    --mp-bg: #fbf9f4;
    --mp-surface-low: #f0eee9;
    --mp-surface: #fffcf8;
    --mp-surface-high: #f6f1e8;
    --mp-surface-highest: #ebe4d7;
    --mp-outline: rgba(50, 34, 20, 0.12);
    --mp-outline-strong: #735a3a;
    --mp-text: #1b1c19;
    --mp-heading: #3a2414;
    --mp-muted: #6b5344;
    --mp-primary: #322214;
    --mp-primary-strong: #735a3a;
    --mp-success: #16a34a;
    background: var(--mp-bg);
    color: var(--mp-text);
    font-family: 'Work Sans', system-ui, sans-serif;
}

body.theme-dark .mp-market-style {
    --mp-bg: #121416;
    --mp-surface-low: #1a1c1e;
    --mp-surface: #1e2022;
    --mp-surface-high: #282a2c;
    --mp-surface-highest: #333537;
    --mp-outline: rgba(164, 140, 122, 0.12);
    --mp-outline-strong: #52443a;
    --mp-text: #e2e2e5;
    --mp-heading: #fff1df;
    --mp-muted: #d6c3b5;
    --mp-primary: #ffddc3;
    --mp-primary-strong: #feb87b;
    --mp-success: #4ade80;
}

.mp-market-style > .mp-header,
.mp-market-style > .mp-hero,
.mp-market-style > .mp-search-section,
.mp-market-style > .mp-my-published,
.mp-market-style > .mp-section,
.mp-market-style > .mp-footer {
    display: none;
}

.mp-market-style .material-symbols-outlined {
    font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}

.mp-sidenav {
    position: fixed;
    inset: 0 auto 0 0;

```
