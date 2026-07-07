# Knowledge Document: App.css (Chunk 25/43)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/App.css",
  "language": "css",
  "module": "src",
  "business_domain": "dashboard",
  "tags": [
    "dashboard",
    "admin",
    "inventory",
    "security",
    "notification"
  ],
  "logical_type": "Generic",
  "chunk_index": 24,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
own) */
.status-select {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  color: var(--text-primary);
  padding: 4px 8px;
  font-size: 12px;
  cursor: pointer;
  transition: var(--transition);
}

.status-select:hover {
  border-color: rgba(212, 165, 116, 0.5);
}

.status-select:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(212, 165, 116, 0.15);
}

/* Selected Row */
.row-selected {
  background: rgba(212, 165, 116, 0.08) !important;
  border-left: 3px solid var(--primary);
}

/* Action Buttons */
.btn-icon {
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  background: transparent;
  cursor: pointer;
  font-size: 14px;
  transition: var(--transition);
}

.btn-edit:hover {
  background: rgba(212, 156, 87, 0.08);
  border-color: rgba(212, 156, 87, 0.3);
}

.btn-delete:hover {
  background: rgba(239, 68, 68, 0.1);
  border-color: rgba(239, 68, 68, 0.3);
}

/* Empty State */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 60px 20px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  text-align: center;
}

.empty-icon {
  font-size: 56px;
  margin-bottom: 16px;
  opacity: 0.6;
}

.empty-state p {
  color: var(--text-secondary);
  font-size: 16px;
  margin-bottom: 20px;
}

/* Modal */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: var(--bg-card);
  /* Less aggressive than pure black for overlay */
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.15s ease;
}

.modal-content,
.modal {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  width: 90%;
  max-width: 800px;
  max-height: 90vh;
  overflow-y: auto;
  animation: slideUp 0.2s ease;
  padding: 28px 24px;
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.5);
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

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;

```
