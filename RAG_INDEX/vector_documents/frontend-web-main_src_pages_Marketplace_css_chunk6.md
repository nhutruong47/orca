# Knowledge Document: Marketplace.css (Chunk 7/44)

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
  "chunk_index": 6,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
h: 100%;
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
    border-radius: 20px;
    width: 94%;
    max-width: 780px;
    max-height: 92vh;
    overflow-y: auto;
    padding: 2rem 2.5rem;
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
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--border);
}

.mp-modal-header h2 {
    font-size: 1.35rem;
    font-weight: 700;
}

.mp-modal-close {
    background: none;
    border: none;
    font-size: 1.8rem;
    cursor: pointer;
    color: var(--text-muted);
    transition: color 0.2s;
    line-height: 1;
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
}

.mp-modal-close:hover {
    color: var(--danger);
    background: rgba(239, 68, 68, 0.1);
}

.mp-modal-seller {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: 0.8rem 1.2rem;
    border-radius: 10px;
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
    color: var(--text-secondary);
}

.mp-modal-seller strong {
    color: var(--accent-primary);
}

.mp-form-group {
    margin-bottom: 1.2rem;
}

.mp-form-group label {
    display: block;

```
