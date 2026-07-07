# Knowledge Document: Marketplace.css (Chunk 11/44)

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
  "chunk_index": 10,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
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

.mp-side-links a .material-symbols-outlined {
    width: 28px;
    color: currentColor;
    font-size: 23px;
    font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 24;
}

.mp-side-links a:hover,
.mp-side-links a.active {
    background: linear-gradient(90deg, rgba(66, 48, 39, 0.92), rgba(27, 28, 30, 0.35) 72%, transparent);
    color: #feb87b;
}

.mp-side-links a.active {
    box-shadow: inset 4px 0 0 #feb87b;
    transform: translateX(0);
}

.mp-side-links a.active::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 4px;
    height: 100%;
    border-radius: 999px;
    background: #feb87b;
}

.mp-side-links a:hover:not(.active) {
    color: rgba(255, 221, 195, 0.92);
    transform: translateX(2px);
}

.mp-topbar {
    position: fixed;
    top: 0;
    right: 0;
    left: var(--sidebar-width);
    z-index: 55;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    padding: 0 clamp(20px, 4vw, 48px);
    background: var(--shell-topbar-bg, rgba(255, 252, 248, 0.9));
    border-bottom: 1px solid var(--mp-outline);
    backdrop-filter: blur(18px);
}

.mp-top-search {
    position: relative;
    width: min(460px, 100%);
}

.mp-top-search .material-symbols-outlined {
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--shell-text-muted, rgba(91, 74, 59, 0.58));
}

.mp-top-search input {
    width: 100%;
    border: 0;
    border-radius: 999px;
    padding: 11px 16px 11px 46px;
    background: var(--shell-surface-soft, var(--mp-surface-high));
    color: var(--mp-text);
    font-size: 14px;
    outline: none;
}

.mp-top-search input:focus {
    box-shadow: 0 0 0 1px var(--mp-primary);
}

.mp-top-actions {
    display: flex;
    align-items: center;
    gap: 8px;
}

.mp-top-actions button {
    width: 40px;
    height: 40px;
    display: grid;
    place-items: center;
    border: 0;
    border-radius: 50%;

```
