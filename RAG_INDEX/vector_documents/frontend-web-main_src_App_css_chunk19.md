# Knowledge Document: App.css (Chunk 20/43)

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
  "chunk_index": 19,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
x;
    overflow-y: auto;
    overflow-x: hidden;
  }

  .topbar {
    padding: 0 14px;
    gap: 8px;
  }

  .topbar-left {
    min-width: 0;
    flex: 1;
  }

  .topbar-greeting {
    font-size: 12px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .topbar-right {
    display: flex;
    gap: 8px;
  }

  .topbar-logout {
    display: block;
    padding: 5px 10px;
    font-size: 11px;
  }

  .page-header {
    flex-direction: column;
    align-items: stretch;
    gap: 12px;
    margin-bottom: 20px;
  }

  .btn-add {
    width: 100%;
    padding: 10px 16px;
    font-size: 13px;
  }

  .page-title {
    font-size: 20px;
  }

  .page-subtitle {
    font-size: 12px;
  }

  .section-title {
    font-size: 14px;
  }

  .welcome-banner {
    flex-direction: column;
    text-align: center;
    padding: 24px 16px;
  }

  .welcome-name {
    font-size: 20px;
  }

  .welcome-greeting {
    font-size: 12px;
  }

  .welcome-role {
    font-size: 12px;
  }

  .welcome-illustration {
    font-size: 48px;
    margin-top: 12px;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }

  .actions-grid {
    grid-template-columns: 1fr;
    gap: 10px;
  }

  .stat-card {
    padding: 16px;
    gap: 12px;
  }

  .stat-icon {
    width: 44px;
    height: 44px;
    font-size: 20px;
  }

  .stat-value {
    font-size: 14px;
  }

  .stat-label {
    font-size: 10px;
  }

  .auth-card {
    padding: 28px 20px;
    width: 95%;
  }

  .auth-logo-icon {
    font-size: 40px;
  }

  .auth-logo-text {
    font-size: 24px;
  }

  .auth-form .form-input {
    padding: 12px 12px 12px 40px;
    font-size: 14px;
  }

  .auth-form .btn-primary {
    padding: 14px;
    font-size: 14px;
  }

  .data-table {
    font-size: 12px;
  }

  .data-table th,
  .data-table td {
    padding: 10px 8px;
    font-size: 11px;
  }

  .table-container {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  .td-desc {
    max-width: 80px;
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

```
