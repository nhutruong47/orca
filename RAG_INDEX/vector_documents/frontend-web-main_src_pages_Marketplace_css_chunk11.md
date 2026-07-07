# Knowledge Document: Marketplace.css (Chunk 12/44)

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
  "chunk_index": 11,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
soft, var(--mp-surface-high));
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
    background: transparent;
    color: var(--mp-muted);
    cursor: pointer;
}

.mp-top-actions button:hover {
    background: var(--shell-surface-hover, var(--mp-surface-high));
    color: var(--mp-primary);
}

.mp-user-avatar {
    width: 36px;
    height: 36px;
    display: grid;
    place-items: center;
    border-radius: 50%;
    border: 1px solid var(--mp-outline);
    background: var(--shell-avatar-bg, var(--mp-surface-highest));
    color: var(--shell-avatar-text, var(--mp-primary));
    font-weight: 800;
}

.mp-main {
    --mp-page-max: 1680px;
    min-height: 100vh;
    flex: 1;
    min-width: 0;
    margin-left: 0;
    padding: 96px clamp(16px, 2.75vw, 48px) 40px;
    overflow-y: auto;
    overflow-x: hidden;
}

.mp-showcase-hero {
    position: relative;
    min-height: 380px;
    overflow: hidden;
    border: 1px solid var(--mp-outline);
    border-radius: 8px;
    margin: 0 auto 36px;
    max-width: var(--mp-page-max);
    background: var(--mp-surface-low);
}

.mp-showcase-hero > img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: grayscale(0.55) brightness(0.8);
    transition: transform 0.8s ease;
}

.mp-showcase-hero:hover > img {
    transform: scale(1.04);
}

.mp-showcase-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg, rgba(255, 252, 248, 0.94), rgba(255, 252, 248, 0.72) 48%, rgba(255, 252, 248, 0.08));
}

.mp-showcase-content {
    position: relative;
    z-index: 2;
    max-width: 720px;
    padding: clamp(32px, 5vw, 54px);
}

.mp-verified {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 18px;
    border-radius: 999px;
    padding: 7px 12px;
    background: rgba(255, 221, 195, 0.1);
    color: var(--mp-primary-strong);
    font-family: 'Montserrat', sans-serif;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

.mp-showcase-content h1 {

```
