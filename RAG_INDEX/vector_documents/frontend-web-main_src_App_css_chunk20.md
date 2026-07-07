# Knowledge Document: App.css (Chunk 21/43)

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
  "chunk_index": 20,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css

  }

  .login-hero-title {
    font-size: 28px;
  }

  .login-hero-content {
    padding: 32px 20px;
  }

  .profile-page {
    max-width: 100%;
  }

  .profile-header {
    padding: 24px 0;
  }

  .profile-avatar-large {
    width: 80px;
    height: 80px;
    font-size: 32px;
  }

  .profile-name {
    font-size: 20px;
  }
}

/* Mobile (320px - 480px) */
@media (max-width: 480px) {
  .sidebar {
    display: none;
  }

  .layout {
    width: 100%;
    overflow: visible;
  }

  .layout-main {
    width: 100%;
    overflow: visible;
  }

  .layout-content {
    padding: 16px 12px;
    overflow-y: auto;
    overflow-x: hidden;
  }

  html,
  body {
    overflow: visible;
  }

  .topbar {
    padding: 0 10px;
    height: var(--topbar-height);
    gap: 6px;
  }

  .topbar-left {
    min-width: 0;
    flex: 1;
  }

  .topbar-greeting {
    font-size: 11px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .topbar-username {
    display: none;
  }

  .topbar-right {
    display: flex;
    gap: 4px;
  }

  .topbar-avatar {
    width: 32px;
    height: 32px;
    font-size: 12px;
  }

  .topbar-logout {
    display: none !important;
  }

  .page-header {
    flex-direction: column;
    align-items: stretch;
    gap: 10px;
    margin-bottom: 16px;
  }

  .page-title {
    font-size: 18px;
  }

  .page-subtitle {
    font-size: 11px;
  }

  .btn-add {
    width: 100%;
    padding: 10px 14px;
    font-size: 12px;
  }

  .section-title {
    font-size: 13px;
  }

  .welcome-banner {
    flex-direction: column;
    text-align: center;
    padding: 20px 12px;
  }

  .welcome-name {
    font-size: 18px;
  }

  .welcome-greeting {
    font-size: 11px;
  }

  .welcome-role {
    font-size: 11px;
  }

  .welcome-illustration {
    font-size: 40px;
    margin-top: 12px;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 10px;
  }

  .actions-grid {
    grid-template-columns: 1fr;
    gap: 10px;
  }

  .stat-card {
    padding: 14px;
    gap: 10px;
  }

  .stat-icon {
    width: 40px;
    height: 40px;
    font-size: 18px;
  }

  .stat-value {
    font-size: 13px;
  }

  .stat-label {
    font-size: 9px;
  }

  .action-card {
    padding: 16px;
  }

  .action-icon {
    font-size: 24px;
  }

  .action-card h3 {
    font-size: 13px;
  }

  .action-card p {
    font-size: 11px;
  }

  .auth-card {
    padding: 24px 16px;
    width: 98%;

```
