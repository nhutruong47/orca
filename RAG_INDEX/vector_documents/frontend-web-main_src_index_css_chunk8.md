# Knowledge Document: index.css (Chunk 9/10)

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
  "chunk_index": 8,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, dashboard

## Source Code Chunk
```css
min stats cards */
body.theme-light .admin-stat-value {
  color: var(--text-primary) !important;
}

body.theme-light .admin-stat-label,
body.theme-light .admin-stat-icon {
  color: var(--text-secondary) !important;
}

body.theme-light .admin-stat-hint {
  color: var(--text-muted) !important;
}

/* Modal and overlay */
body.theme-light .modal-overlay {
  background: rgba(0,0,0,0.25) !important;
}

body.theme-light .modal,
body.theme-light .modal-content {
  background: var(--bg-card) !important;
  border-color: var(--border) !important;
}

body.theme-light .modal-header,
body.theme-light .modal-header h2 {
  color: var(--text-primary) !important;
  border-bottom: 1px solid var(--border) !important;
}

body.theme-light .modal-close-btn {
  color: var(--text-secondary) !important;
}

/* Data grid and tables */
body.theme-light .data-grid,
body.theme-light .table-wrapper {
  background: var(--bg-card) !important;
  border-color: var(--border) !important;
}

body.theme-light tr {
  border-color: var(--border) !important;
}

/* Badges and tags */
body.theme-light .badge,
body.theme-light .status-badge,
body.theme-light .role-badge {
  background: rgba(50,34,20,0.08) !important;
  color: var(--accent-primary) !important;
}

body.theme-light .role-badge.manager {
  background: rgba(210,153,34,0.10) !important;
  color: #d97706 !important;
}

body.theme-light .role-badge.member {
  background: rgba(50,34,20,0.10) !important;
  color: var(--accent-primary) !important;
}

/* Search input */
body.theme-light .search-input,
body.theme-light input[type="search"],
body.theme-light input[type="text"],
body.theme-light input[type="email"],
body.theme-light input[type="password"],
body.theme-light select {
  background: rgba(50,34,20,0.02) !important;
  color: var(--text-primary) !important;
  border-color: var(--border) !important;
}

body.theme-light input:focus,
body.theme-light select:focus,
body.theme-light textarea:focus {
  border-color: var(--accent-primary) !important;
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


```
