# Knowledge Document: Marketplace.css (Chunk 27/44)

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
  "chunk_index": 26,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
manufacturing-market .mp-top-search input::placeholder {
    color: #8b837d;
}

.mp-manufacturing-market .mp-top-actions button {
    color: #d6bba5;
}

.mp-manufacturing-market .mp-user-avatar {
    border-color: rgba(255, 181, 121, 0.28);
    background: #24211f;
    color: #ffd8b7;
}

.mp-manufacturing-market .mp-main {
    --mp-page-max: min(1600px, calc(100vw - var(--sidebar-width) - 96px));
    padding: 88px clamp(28px, 4vw, 56px) 48px;
    background: var(--mp-bg);
}

.mp-manufacturing-market .mp-market-hero,
.mp-manufacturing-market .mp-partner-section,
.mp-manufacturing-market .mp-product-section,
.mp-manufacturing-market .mp-cta,
.mp-manufacturing-market .mp-showcase-footer {
    max-width: var(--mp-page-max);
    margin-inline: auto;
}

.mp-manufacturing-market .mp-market-hero {
    position: relative;
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(250px, 320px);
    align-items: center;
    gap: 28px;
    min-height: 285px;
    margin-bottom: 28px;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 32px 30px;
    background:
        linear-gradient(90deg, rgba(17, 20, 21, 0.98) 0%, rgba(17, 20, 21, 0.9) 38%, rgba(17, 20, 21, 0.28) 100%),
        url('/luxury-coffee-hero.png') center / cover;
}

body.theme-dark .mp-manufacturing-market .mp-market-hero {
    background:
        linear-gradient(90deg, rgba(17, 20, 21, 0.98) 0%, rgba(17, 20, 21, 0.9) 38%, rgba(17, 20, 21, 0.28) 100%),
        url('/luxury-coffee-hero.png') center / cover;
}

.mp-market-hero-copy {
    position: relative;
    z-index: 1;
    max-width: 560px;
}

.mp-manufacturing-market .mp-verified {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    margin-bottom: 16px;
    border: 1px solid rgba(255, 181, 121, 0.18);
    border-radius: 999px;
    padding: 5px 10px;
    background: rgba(255, 181, 121, 0.1);
    color: #ffbd83;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.mp-manufacturing-market .mp-verified .material-symbols-outlined {
    font-size: 15px;
}

.mp-manufacturing-market .mp-market-hero h1 {
    max-width: 620px;
    margin: 0 0 16px;
    color: #fff;
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(2.1rem, 4vw, 3.2rem);
    font-weight: 900;

```
