# Knowledge Document: Marketplace.css (Chunk 2/44)

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
  "chunk_index": 1,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
order);
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
    margin-bottom: 1.5rem;
}

.mp-hero-stats {
    display: flex;
    gap: 2.5rem;
}

.mp-hero-stat {
    display: flex;
    flex-direction: column;
}

.stat-num {
    font-size: 1.8rem;
    font-weight: 800;
    color: var(--accent-primary);
}

.stat-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
}

/* Search */
.mp-search-section {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem 4rem;
    background: var(--bg-secondary);
    border-bottom: 1px solid var(--border);
}

.mp-search-wrapper {
    flex: 1;
    position: relative;
}

.mp-search-icon {
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 0.9rem;
}

.mp-search-input {
    width: 100%;
    background: var(--bg-input);
    border: 1px solid var(--border);
    color: var(--text-primary);
    padding: 0.7rem 1rem 0.7rem 2.5rem;
    border-radius: 10px;
    font-size: 0.9rem;
    transition: border-color 0.2s;
}

.mp-search-input:focus {
    outline: none;
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 3px var(--accent-glow);
}

.mp-search-input::placeholder {
    color: var(--text-muted);
}

.mp-result-count {
    font-size: 0.8rem;
    color: var(--text-muted);
    white-space: nowrap;
    font-weight: 600;
}

/* My Published */
.mp-my-published {
    padding: 1rem 4rem;
    background: var(--bg-secondary);
    border-bottom: 1px solid var(--border);
}

.mp-my-published h3 {
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-bottom: 0.6rem;
    font-weight: 600;
}

.mp-my-published-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
}

.mp-my-pub-item {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: 0.5rem 1rem;
    border-radius: 8px;
    font-size: 0.85rem;
}

.mp-pub-badge {

```
