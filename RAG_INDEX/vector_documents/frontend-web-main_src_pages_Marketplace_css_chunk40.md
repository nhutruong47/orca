# Knowledge Document: Marketplace.css (Chunk 41/44)

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
  "chunk_index": 40,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
 blur(16px);
    transition: all 0.3s ease;
}

.mp-spotlight-search:focus-within {
    border-color: var(--mp-primary);
    box-shadow: 0 4px 32px rgba(245, 158, 11, 0.15);
}

.mp-market-card {
    background: var(--mp-surface);
    border: 1px solid var(--mp-outline);
    border-radius: 16px;
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    overflow: hidden;
    position: relative;
    backdrop-filter: blur(8px);
}

.mp-market-card:hover {
    transform: translateY(-4px);
    border-color: rgba(245, 158, 11, 0.3);
    box-shadow: 0 12px 32px rgba(0,0,0,0.4), 0 0 20px rgba(245, 158, 11, 0.1);
}

.mp-market-card-rfq-btn {
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s ease;
}

.mp-market-card:hover .mp-market-card-rfq-btn {
    opacity: 1;
    transform: translateY(0);
}

/* === Light Theme Overrides for Manufacturing Market === */
body.theme-light .mp-body.mp-manufacturing-market {
    --mp-bg: #fbf9f4;
    --mp-surface: #fffcf8;
    --mp-surface-low: #f0eee9;
    --mp-surface-high: #f6f1e8;
    --mp-outline: rgba(50, 34, 20, 0.12);
    --mp-outline-strong: #735a3a;
    --mp-text: #1b1c19;
    --mp-heading: #3a2414;
    --mp-muted: #6b5344;
    --mp-primary: #322214;
    --mp-primary-strong: #735a3a;
    --mp-success: #16a34a;
}
body.theme-light .mp-manufacturing-market .mp-topbar { background: rgba(251, 249, 244, 0.94); border-bottom-color: var(--mp-outline); }
body.theme-light .mp-manufacturing-market .mp-top-search input { border: 1px solid var(--mp-outline); background: #fffcf8; color: #1b1c19; }
body.theme-light .mp-manufacturing-market .mp-top-search input::placeholder { color: #9b8b7e; }
body.theme-light .mp-manufacturing-market .mp-top-actions button { color: #735a3a; }
body.theme-light .mp-manufacturing-market .mp-user-avatar { border-color: rgba(115, 90, 58, 0.28); background: #fffcf8; color: #322214; }
body.theme-light .mp-manufacturing-market .mp-market-hero {
    background: linear-gradient(90deg, rgba(251, 249, 244, 0.98) 0%, rgba(251, 249, 244, 0.9) 38%, rgba(251, 249, 244, 0.28) 100%), url('/luxury-coffee-hero.png') center / cover;
    border: 1px solid var(--mp-outline);
}
body.theme-light .mp-manufacturing-market .mp-market-hero h1 { color: #1b1c19; }
body.theme-light .mp-manufacturing-market .mp-market-hero h1 em { color: #d97706; }

```
