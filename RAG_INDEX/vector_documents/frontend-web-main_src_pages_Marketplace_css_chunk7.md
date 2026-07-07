# Knowledge Document: Marketplace.css (Chunk 8/44)

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
  "chunk_index": 7,
  "total_chunks": 44
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, chat

## Source Code Chunk
```css
 68, 68, 0.1);
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
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--text-secondary);
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.mp-form-group input,
.mp-form-group select,
.mp-form-group textarea {
    width: 100%;
    background: var(--bg-input);
    border: 1px solid var(--border);
    color: var(--text-primary);
    padding: 0.75rem 1rem;
    border-radius: 10px;
    font-size: 1rem;
    font-family: inherit;
    transition: border-color 0.2s, box-shadow 0.2s;
}

.mp-form-group input:focus,
.mp-form-group select:focus,
.mp-form-group textarea:focus {
    outline: none;
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 3px rgba(212, 165, 116, 0.15);
}

.mp-form-group textarea {
    min-height: 100px;
    resize: vertical;
}

.mp-form-group select option {
    background: #ffffff !important;
    color: #111827 !important;
}

.mp-form-group select optgroup {
    background: #ffffff !important;
    color: #7a4d1d !important;
    font-weight: 800;
}

.mp-form-row {
    display: flex;
    gap: 1.2rem;
}

.mp-form-row .mp-form-group {
    flex: 1;
}

.mp-modal-actions {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
    padding-top: 1.2rem;
    border-top: 1px solid var(--border);
    justify-content: flex-end;
}

.mp-cancel-btn {
    background: var(--bg-tertiary);
    border: 1px solid var(--border);
    color: var(--text-primary);
    padding: 0.8rem 1.5rem;
    border-radius: 10px;
    font-weight: 600;
    font-size: 0.95rem;
    cursor: pointer;
    transition: all 0.2s;
}

.mp-cancel-btn:hover {
    border-color: var(--accent-primary);
}

.mp-submit-btn {
    flex: 1;
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

.mp-submit-btn:hover:not(:disabled) {
    transform: translateY(-1px);

```
