# Knowledge Document: index.css (Chunk 10/10)

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
  "chunk_index": 9,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, dashboard

## Source Code Chunk
```css
-primary) !important;
  box-shadow: 0 0 0 2px rgba(50,34,20,0.08) !important;
}

/* Dropdown and select menus */
body.theme-light .dropdown,
body.theme-light .select-menu,
body.theme-light .options-menu {
  background: var(--bg-card) !important;
  border-color: var(--border) !important;
}

body.theme-light .dropdown-item,
body.theme-light .option-item {
  color: var(--text-primary) !important;
}

body.theme-light .dropdown-item:hover,
body.theme-light .option-item:hover {
  background: rgba(50,34,20,0.06) !important;
}

/* Section titles and headers */
body.theme-light .section-title {
  color: var(--text-primary) !important;
}

body.theme-light .section-subtitle {
  color: var(--text-secondary) !important;
}

/* Dialog and panels */
body.theme-light .dialog,
body.theme-light .panel,
body.theme-light .card {
  background: var(--bg-card) !important;
  border: 1px solid var(--border) !important;
}

/* Focus states */
body.theme-light *:focus-visible {
  outline: 2px solid var(--accent-primary) !important;
}

/* Links and text decorations */
body.theme-light a {
  color: var(--accent-primary) !important;
}

body.theme-light a:hover {
  color: var(--accent-secondary) !important;
}

```
