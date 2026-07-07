# Knowledge Document: Marketplace.css (Chunk 4/44)

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
  "chunk_index": 3,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
r(--text-secondary);
    font-size: 0.9rem;
}

/* Grid */
.mp-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 1.5rem;
}

.mp-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: all 0.25s ease;
}

.mp-card:hover {
    border-color: var(--border-focus);
    transform: translateY(-3px);
    box-shadow: var(--shadow-lg);
}

.mp-card-img-wrapper {
    position: relative;
    height: 180px;
    background: var(--bg-tertiary);
}

.mp-card-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.mp-card-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    padding: 0.8rem;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}

.mp-trust-badge {
    padding: 0.2rem 0.6rem;
    border-radius: 6px;
    font-size: 0.7rem;
    font-weight: 700;
    backdrop-filter: blur(4px);
}

.mp-trust-badge.high {
    background: rgba(63, 185, 80, 0.85);
    color: #fff;
}

.mp-trust-badge.mid {
    background: rgba(212, 156, 87, 0.85);
    color: #fff;
}

.mp-trust-badge.low {
    background: rgba(226, 75, 75, 0.85);
    color: #fff;
}

.mp-member-badge {
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(4px);
    color: #fff;
    padding: 0.2rem 0.6rem;
    border-radius: 6px;
    font-size: 0.7rem;
    font-weight: 600;
}

.mp-card-content {
    padding: 1.2rem 1.4rem;
    flex: 1;
    display: flex;
    flex-direction: column;
}

.mp-card-title {
    font-size: 1.1rem;
    font-weight: 700;
    margin: 0 0 0.5rem;
}

.mp-card-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 0.6rem;
    font-size: 0.78rem;
    color: var(--text-secondary);
}

.mp-card-meta span {
    background: var(--bg-tertiary);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
}

.mp-card-desc {
    font-size: 0.85rem;
    color: var(--text-secondary);
    line-height: 1.5;
    margin-bottom: 0.8rem;
    flex: 1;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.mp-card-orders {
    font-size: 0.78rem;
    color: var(--success);
    font-weight: 600;
    margin-bottom: 0.8rem;
}

.mp-card-actions {
    padding-top: 0.8rem;

```
