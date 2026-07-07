# Knowledge Document: Marketplace.css (Chunk 3/44)

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
  "chunk_index": 2,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
var(--text-secondary);
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
    background: rgba(63, 185, 80, 0.15);
    color: var(--success);
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    font-size: 0.7rem;
    font-weight: 600;
    margin-left: 0.5rem;
}

.mp-unpub-btn {
    background: transparent;
    border: 1px solid var(--danger);
    color: var(--danger);
    padding: 0.25rem 0.6rem;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
}

.mp-edit-pub-btn {
    border: 1px solid var(--mp-outline, var(--border));
    border-radius: 6px;
    padding: 0.25rem 0.6rem;
    background: var(--mp-surface-high, var(--bg-tertiary));
    color: var(--mp-text, var(--text-primary));
    font-size: 0.75rem;
    font-weight: 700;
    cursor: pointer;
}

.mp-edit-pub-btn:hover {
    border-color: var(--mp-primary-strong, var(--accent-primary));
}

.mp-unpub-btn:hover {
    background: var(--danger);
    color: #fff;
}

/* Section */
.mp-section {
    padding: 2.5rem 4rem;
}

.mp-section-header {
    margin-bottom: 1.5rem;
}

.mp-section-header h2 {
    font-size: 1.3rem;
    font-weight: 700;
}

.mp-error {
    background: rgba(226, 75, 75, 0.1);
    border: 1px solid rgba(226, 75, 75, 0.3);
    color: var(--danger);
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 1.5rem;
    font-size: 0.9rem;
}

.mp-empty {
    text-align: center;
    padding: 4rem 2rem;
    background: var(--bg-card);
    border-radius: 16px;
    border: 1px dashed var(--border);
}

.mp-empty h3 {
    margin: 1rem 0 0.5rem;
    font-size: 1.15rem;
}

.mp-empty p {
    color: var(--text-secondary);
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

```
