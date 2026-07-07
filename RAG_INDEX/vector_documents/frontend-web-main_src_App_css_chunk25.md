# Knowledge Document: App.css (Chunk 26/43)

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
  "chunk_index": 25,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css

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
  border-bottom: 1px solid var(--border);
}

.modal-header h2 {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
}

.modal-close {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  background: transparent;
  color: var(--text-muted);
  font-size: 18px;
  cursor: pointer;
  border-radius: var(--radius-md);
  transition: var(--transition);
}

.modal-close:hover {
  background: var(--bg-input);
  color: var(--text-primary);
}

.modal-form {
  padding: 24px;
}

.modal-form .form-group {
  margin-bottom: 16px;
}

.modal-form .form-input {
  padding: 12px 14px;
  padding-left: 14px;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 24px;
}

.upgrade-required-modal {
  width: min(92vw, 440px);
  max-width: 440px;
  text-align: center;
  overflow: visible;
}

.upgrade-required-actions {
  display: flex;
  justify-content: center;
  gap: 12px;
  width: 100%;
}

.upgrade-required-button {
  min-width: 132px;
  min-height: 46px;
  padding: 11px 20px;
  border-radius: 10px;
  border: 1px solid var(--border);
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  line-height: 1.2;
  white-space: nowrap;
  cursor: pointer;
}

.upgrade-required-primary {
  border-color: transparent;
}

@media (max-width: 420px) {
  .upgrade-required-actions {
    flex-direction: column-reverse;
  }

  .upgrade-required-button {
    width: 100%;
  }
}

/* Form Row */
.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.form-row-3 {
  grid-template-columns: 1fr 1fr 1fr;
}

/* Form Extras */
.form-select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%239ca3af' d='M2 4l4 4 4-4'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  padding-right: 32px;
}

.form-textarea {

```
