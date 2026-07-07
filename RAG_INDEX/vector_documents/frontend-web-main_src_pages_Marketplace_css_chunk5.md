# Knowledge Document: Marketplace.css (Chunk 6/44)

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
  "chunk_index": 5,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
);
}

.mp-modal-header h2 {
    font-size: 1.1rem;
    font-weight: 700;
}

.mp-modal-close {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: var(--text-muted);
    transition: color 0.2s;
    line-height: 1;
}

.mp-modal-close:hover {
    color: var(--danger);
}

.mp-modal-seller {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: 0.6rem 1rem;
    border-radius: 8px;
    font-size: 0.9rem;
    margin-bottom: 1rem;
    color: var(--text-secondary);
}

.mp-modal-seller strong {
    color: var(--accent-primary);
}

.mp-form-group {
    margin-bottom: 1rem;
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
    border-top: 1px solid var(--border);
}

.mp-order-btn {
    width: 100%;
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

.mp-order-btn:hover {
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

/* Footer */
.mp-footer {
    text-align: center;

```
