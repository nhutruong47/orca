# Knowledge Document: App.css (Chunk 31/43)

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
  "chunk_index": 30,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
;
}

.sidebar-avatar-initials {
  background: var(--shell-avatar-bg);
  color: var(--shell-avatar-text);
  font-size: 12px;
  font-weight: 750;
  letter-spacing: 0;
}

.sidebar-avatar,
.topbar-avatar,
.profile-avatar-large {
  background: var(--shell-avatar-bg);
  color: var(--shell-avatar-text);
}

.sidebar-user-wrap .sidebar-avatar.sidebar-avatar-initials {
  background: var(--shell-avatar-bg);
  color: var(--shell-avatar-text);
  width: 44px;
  height: 44px;
  font-size: 16px;
  border: 2px solid var(--shell-border-strong);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.topbar {
  border-bottom: 1px solid var(--shell-border);
  background: var(--shell-topbar-bg);
  backdrop-filter: blur(18px);
}

.topbar-greeting {
  color: var(--shell-text-soft);
}

.topbar-username {
  color: var(--shell-title);
}

.topbar-logout {
  border-color: var(--shell-danger);
  color: var(--shell-danger);
  background: var(--shell-danger-soft);
}

.page-container,
.dashboard-wrapper,
.profile-page,
.settings-page,
.inventory-page {
  color: var(--shell-text);
}

.page-header,
.settings-card,
.profile-section,
.glass-panel,
.table-responsive,
.tabs-container,
.empty-state,
.modal,
.modal-content,
.table-container {
  background: var(--shell-surface) !important;
  border: 1px solid var(--shell-border) !important;
  border-radius: 8px !important;
  box-shadow: var(--shell-shadow);
  backdrop-filter: blur(14px);
}

.glass-panel:hover {
  border-color: var(--shell-border-strong) !important;
  box-shadow: var(--shell-hover-shadow);
}

.page-title,
.settings-title,
.profile-name,
.section-title,
.settings-card-header h2,
.modal-header h2 {
  color: var(--shell-title) !important;
  font-family: 'Inter', system-ui, sans-serif;
  letter-spacing: 0;
}

.text-glow-active,
.text-neon {
  color: var(--shell-title) !important;
  text-shadow: none;
}

.page-subtitle,
.settings-card-desc,
.empty-state p,
.profile-field .field-label,
.settings-row-hint,
.settings-info-item .info-label {
  color: var(--shell-text-soft) !important;
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


```
