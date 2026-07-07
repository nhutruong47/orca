# Knowledge Document: index.css (Chunk 8/10)

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
  "chunk_index": 7,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, dashboard

## Source Code Chunk
```css
m-input::placeholder {
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
  background: rgba(50, 34, 20, 0.06) !important;
  border: 1px solid rgba(50, 34, 20, 0.10) !important;
}

/* ===== Additional comprehensive light-theme overrides for better alignment ===== */
/* Force all dark-colored components to use light palette */
body.theme-light .admin-panel,
body.theme-light .page-header,
body.theme-light .admin-stat,
body.theme-light .dashboard-wrapper,
body.theme-light .inventory-page,
body.theme-light .empty-state {
  background: var(--bg-card) !important;
  color: var(--text-primary) !important;
  border-color: var(--border) !important;
}

/* Topbar and header elements */
body.theme-light .topbar {
  background: var(--bg-card) !important;
  border-bottom: 1px solid var(--border) !important;
}

body.theme-light .topbar-greeting,
body.theme-light .topbar-username {
  color: var(--text-primary) !important;
}

body.theme-light .topbar-logout {
  color: var(--text-secondary) !important;
  border-color: var(--border) !important;
}

/* Sidebar elements */
body.theme-light .sidebar-logo {
  border-bottom: 1px solid var(--border) !important;
}

body.theme-light .logo-text {
  color: var(--accent-primary) !important;
}

body.theme-light .sidebar-username {
  color: var(--text-primary) !important;
}

/* Tab and filter buttons */
body.theme-light .tab-btn,
body.theme-light .admin-tab-btn {
  background: transparent !important;
  color: var(--text-secondary) !important;
  border-color: var(--border) !important;
}

body.theme-light .tab-btn:hover,
body.theme-light .admin-tab-btn:hover {
  background: rgba(50,34,20,0.04) !important;
}

/* Admin stats cards */
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


```
