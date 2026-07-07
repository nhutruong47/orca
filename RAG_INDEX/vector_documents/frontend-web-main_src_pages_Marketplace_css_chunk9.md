# Knowledge Document: Marketplace.css (Chunk 10/44)

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
  "chunk_index": 9,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
mp-market-style > .mp-header,
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
    z-index: 60;
    width: 276px;
    display: flex;
    flex-direction: column;
    gap: 0;
    padding: 26px 18px;
    background: #111316;
    border-right: 1px solid rgba(254, 184, 123, 0.12);
    box-shadow: 18px 0 60px rgba(0, 0, 0, 0.24);
}

.mp-menu-label {
    margin: 0 0 22px 16px;
    color: #feb87b;
    font-family: 'Montserrat', system-ui, sans-serif;
    font-size: 12px;
    font-weight: 850;
    letter-spacing: 0.22em;
}

.mp-brand-block {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 4px 8px 20px;
}

.mp-brand-mark {
    width: 42px;
    height: 42px;
    display: grid;
    place-items: center;
    border-radius: 8px;
    background: var(--mp-primary);
    color: #794713;
}

.mp-brand-name {
    font-family: 'Montserrat', sans-serif;
    font-size: 24px;
    line-height: 1;
    font-weight: 800;
    color: var(--mp-primary);
}

.mp-brand-sub {
    margin-top: 4px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: rgba(226, 226, 229, 0.55);
}

.mp-new-profile {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    border: 0;
    border-radius: 8px;
    padding: 13px 12px;
    background: #ffb87b;
    color: #2e1500;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    cursor: pointer;
    transition: transform 0.2s ease, filter 0.2s ease;
}

.mp-new-profile:hover {
    filter: brightness(1.05);
    transform: translateY(-1px);
}

.mp-side-links {
    display: grid;
    gap: 8px;
}

.mp-side-links a {
    position: relative;
    display: flex;
    align-items: center;
    gap: 16px;
    min-height: 54px;
    padding: 0 18px;
    border-radius: 8px;
    color: rgba(214, 195, 181, 0.72);
    font-family: 'Inter', system-ui, sans-serif;
    font-size: 16px;
    font-weight: 750;
    transition: background-color 0.2s ease, color 0.2s ease, transform 0.2s ease;
}


```
