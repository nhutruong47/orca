# Knowledge Document: index.css (Chunk 6/10)

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
  "chunk_index": 5,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, dashboard

## Source Code Chunk
```css
x 16px;
  border-bottom: 1px solid #f1f5f9;
  color: #475569;
  font-weight: 500;
}

/* ===== Force-light overrides (higher specificity) ===== */
body.theme-light .layout,
body.theme-light .layout-main,
body.theme-light .layout-content {
  background: var(--bg-primary) !important;
  color: var(--text-primary) !important;
}

body.theme-light .sidebar {
  background: var(--bg-secondary) !important;
  border-color: var(--border) !important;
}

body.theme-light .topbar,
body.theme-light .auth-card,
body.theme-light .settings-card,
body.theme-light .glass-panel {
  background: var(--bg-card) !important;
  border-color: var(--border) !important;
  color: var(--text-primary) !important;
}

/* Navigation items */
body.theme-light .nav-item {
  color: var(--text-secondary) !important;
  background: transparent !important;
}

body.theme-light .nav-item:hover {
  background: rgba(50, 34, 20, 0.04) !important;
  color: var(--text-primary) !important;
}

body.theme-light .nav-item.active {
  background: linear-gradient(90deg, rgba(50,34,20,0.12), transparent) !important;
  color: var(--accent-primary) !important;
  box-shadow: inset 3px 0 0 var(--accent-primary) !important;
  font-weight: 600 !important;
}

/* Sidebar and avatars */
body.theme-light .sidebar-avatar,
body.theme-light .topbar-avatar,
body.theme-light .profile-avatar-large {
  background: linear-gradient(135deg, #322214 0%, #735a3a 100%) !important;
  color: #fbf9f4 !important;
}

body.theme-light .sidebar-user {
  background: rgba(50, 34, 20, 0.03) !important;
  border-top: 1px solid var(--border) !important;
}

/* Cards and panels */
body.theme-light .glass-panel,
body.theme-light .page-container,
body.theme-light .profile-section,
body.theme-light .table-responsive,
body.theme-light .tabs-container,
body.theme-light .modal,
body.theme-light .modal-content,
body.theme-light .table-container {
  background: var(--bg-card) !important;
  border: 1px solid var(--border) !important;
  color: var(--text-primary) !important;
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

```
