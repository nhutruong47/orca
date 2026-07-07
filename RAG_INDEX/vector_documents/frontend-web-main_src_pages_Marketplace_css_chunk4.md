# Knowledge Document: Marketplace.css (Chunk 5/44)

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
  "chunk_index": 4,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
.85rem;
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
    padding: 2rem 4rem;
    border-top: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 0.8rem;
}

/* Modal */
.mp-modal-overlay {
    position: fixed;
    inset: 0;
    background: var(--bg-card);
    backdrop-filter: blur(4px);
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: fadeIn 0.2s;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.mp-modal {
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: 16px;
    width: 90%;
    max-width: 520px;
    max-height: 90vh;
    overflow-y: auto;
    padding: 1.5rem;
    box-shadow: var(--shadow-lg);
    animation: slideUp 0.25s ease;
}

@keyframes slideUp {
    from {
        transform: translateY(20px);
        opacity: 0;
    }

    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.mp-modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    padding-bottom: 0.8rem;
    border-bottom: 1px solid var(--border);
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

```
