# Knowledge Document: App.css (Chunk 27/43)

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
  "chunk_index": 26,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
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
  min-height: 80px;
  resize: vertical;
}

/* Secondary Button */
.btn-secondary {
  padding: 12px 24px;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text-secondary);
  border-radius: var(--radius-md);
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
}

.btn-secondary:hover {
  background: var(--bg-tertiary);
  color: var(--text-primary);
}

/* Responsive Inventory */
@media (max-width: 768px) {
  .page-header {
    flex-direction: column;
    gap: 12px;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  .form-row-3 {
    grid-template-columns: 1fr;
  }

  .modal-content {
    width: 95%;
  }
}

/* ============================================
   NEW UI ENHANCEMENTS (Glass, Glow, Icons)
   ============================================ */

/* Glass Panel */
.glass-panel {
  background: var(--bg-glass);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  transition: var(--transition);
}

.glass-panel:hover {
  background: var(--bg-glass-hover);
  border-color: var(--border-focus);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
}

/* Icon Container */
.icon-container {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-md);
  background: rgba(212, 165, 116, 0.1);
  color: var(--accent-primary);
  border: 1px solid rgba(212, 165, 116, 0.2);
  transition: var(--transition);
}

body.theme-light .icon-container {
  background: rgba(122, 79, 43, 0.1);
  border: 1px solid rgba(122, 79, 43, 0.2);
}

.icon-container.glow {
  box-shadow: var(--shadow-glow);
}

/* Hover Lift */
.hover-lift {
  transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.25s ease;
}

.hover-lift:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
  border-color: var(--border-focus);
}


```
