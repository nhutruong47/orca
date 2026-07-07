# Knowledge Document: Marketplace.css (Chunk 1/44)

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
  "chunk_index": 0,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&family=Montserrat:wght@400;500;600;700;800;900&family=Work+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@500&display=swap');

/* === Marketplace Professional === */

.mp-body {
    background: var(--bg-primary);
    color: var(--text-primary);
    font-family: 'Inter', sans-serif;
    display: flex;
    height: 100vh;
    width: 100%;
    overflow: hidden;
    transition: background 0.3s, color 0.3s;
}

/* Header */
.mp-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.8rem 4rem;
    background: var(--bg-secondary);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 20;
    backdrop-filter: blur(12px);
}

.mp-logo {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 800;
    font-size: 1rem;
    letter-spacing: 1.5px;
    color: var(--accent-primary);
}

.mp-actions {
    display: flex;
    align-items: center;
    gap: 0.8rem;
}

.mp-publish-btn {
    background: var(--accent-gradient);
    color: #fff;
    border: none;
    padding: 0.5rem 1.2rem;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.85rem;
    cursor: pointer;
    transition: all 0.2s;
    box-shadow: var(--shadow-sm);
}

.mp-publish-btn:hover {
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.mp-back-btn {
    background: var(--bg-tertiary);
    color: var(--text-primary);
    border: 1px solid var(--border);
    padding: 0.5rem 1.2rem;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.85rem;
    cursor: pointer;
    text-decoration: none;
    transition: all 0.2s;
}

.mp-back-btn:hover {
    border-color: var(--accent-primary);
}

/* Hero */
.mp-hero {
    padding: 4rem 4rem 3rem;
    background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
    border-bottom: 1px solid var(--border);
}

.mp-hero-content {
    max-width: 700px;
}

.mp-hero h1 {
    font-size: 2.5rem;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 0.8rem;
    background: var(--accent-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.mp-hero p {
    font-size: 1rem;
    color: var(--text-secondary);
    line-height: 1.6;

```
