# Knowledge Document: App.css (Chunk 32/43)

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
  "chunk_index": 31,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
lor: var(--shell-text-soft) !important;
}

.icon-container {
  background: var(--shell-accent-soft);
  border: 1px solid var(--shell-border-strong);
  color: var(--shell-accent);
  border-radius: 8px;
}

.btn,
.btn-secondary,
.tab-btn,
.form-input,
.form-select,
.form-textarea,
.status-select,
.profile-field,
.settings-row,
.settings-info-item,
.security-item {
  border-radius: 8px !important;
}

.btn-primary,
.auth-form .btn-primary {
  background: var(--accent-gradient) !important;
  color: var(--shell-button-text) !important;
}

.btn-secondary,
.tab-btn,
.form-input,
.form-select,
.form-textarea,
.status-select,
.profile-field,
.settings-info-item,
.security-item {
  background: var(--shell-surface-soft) !important;
  border-color: var(--shell-border) !important;
  color: var(--shell-text) !important;
}

.tab-btn.active {
  background: var(--shell-accent-soft) !important;
  color: var(--shell-accent) !important;
  box-shadow: inset 0 0 0 1px var(--shell-border-strong);
}

.goals-table,
.data-table {
  background: transparent !important;
  border: 0 !important;
}

.goals-table th,
.data-table th {
  color: var(--shell-text-soft) !important;
  background: var(--shell-surface-soft);
  border-bottom: 1px solid var(--shell-border) !important;
}

.goals-table td,
.data-table td {
  color: var(--shell-text) !important;
  border-bottom: 1px solid var(--shell-border) !important;
}

.goals-table tbody tr:hover,
.data-table tbody tr:hover {
  background: var(--shell-surface-hover);
}

.status-badge,
.badge {
  border-radius: 999px;
  border: 1px solid var(--shell-border);
}

.profile-header {
  position: relative;
  overflow: hidden;
  border: 1px solid var(--shell-border);
  border-radius: 8px;
  background:
    var(--shell-profile-overlay),
    url('/coffee-hero.png') center / cover no-repeat;
}

.profile-avatar-large {
  margin-inline: auto;
  box-shadow: var(--shell-shadow);
}

.settings-card {
  padding: clamp(20px, 3vw, 28px);
}

.theme-preview-card {
  border-radius: 8px !important;
  border-color: var(--shell-border) !important;
  background: var(--shell-surface-soft) !important;
}

.theme-preview-card.selected {
  border-color: var(--shell-accent) !important;
  box-shadow: 0 0 0 1px var(--shell-border-strong);
}

@media (max-width: 768px) {
  .layout-content {
    padding: 20px 16px;
  }

  .topbar {
    border-radius: 0;
  }
}


```
