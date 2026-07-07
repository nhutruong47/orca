# Knowledge Document: index.css (Chunk 7/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/index.css",
  "language": "css",
  "module": "src",
  "business_domain": "admin",
  "tags": [
    "admin",
    "inventory",
    "dashboard"
  ],
  "logical_type": "Generic",
  "chunk_index": 6,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, dashboard

## Source Code Chunk
```css
rtant;
}

/* Headings and titles */
body.theme-light h1,
body.theme-light h2,
body.theme-light h3,
body.theme-light .page-title,
body.theme-light .settings-title,
body.theme-light .settings-card-header h2,
body.theme-light .text-glow-active {
  color: var(--text-primary) !important;
  text-shadow: none !important;
}

/* Tables */
body.theme-light .goals-table th,
body.theme-light .data-table th {
  color: var(--text-primary) !important;
  background: rgba(50, 34, 20, 0.03) !important;
  border-bottom: 1px solid var(--border) !important;
  font-weight: 600 !important;
}

body.theme-light .goals-table td,
body.theme-light .data-table td {
  color: var(--text-primary) !important;
  border-bottom: 1px solid rgba(50, 34, 20, 0.04) !important;
}

body.theme-light .goals-table tbody tr:hover,
body.theme-light .data-table tbody tr:hover {
  background: rgba(50, 34, 20, 0.03) !important;
}

/* Buttons and form elements */
body.theme-light .btn-primary,
body.theme-light .auth-form .btn-primary {
  background: linear-gradient(135deg, #322214 0%, #735a3a 100%) !important;
  color: #fbf9f4 !important;
  border-color: var(--accent-primary) !important;
}

body.theme-light .btn-secondary,
body.theme-light .tab-btn {
  background: rgba(50, 34, 20, 0.05) !important;
  color: var(--text-primary) !important;
  border-color: var(--border) !important;
}

body.theme-light .tab-btn.active,
body.theme-light .theme-preview-card.selected {
  background: rgba(50, 34, 20, 0.10) !important;
  color: var(--accent-primary) !important;
  border-color: var(--accent-primary) !important;
}

/* Form elements */
body.theme-light input,
body.theme-light textarea,
body.theme-light .form-input,
body.theme-light .form-select,
body.theme-light .card,
body.theme-light .auth-form .form-input {
  background: rgba(50, 34, 20, 0.02) !important;
  color: var(--text-primary) !important;
  border-color: var(--border) !important;
}

body.theme-light input::placeholder,
body.theme-light .form-input::placeholder {
  color: var(--text-muted) !important;
}

/* Text utilities */
body.theme-light .text-glow-active,
body.theme-light .text-neon {
  color: var(--accent-primary) !important;
}

body.theme-light .page-subtitle,
body.theme-light .settings-card-desc,
body.theme-light .settings-row-hint {
  color: var(--text-secondary) !important;
}

/* Icons */
body.theme-light .icon-container {

```
