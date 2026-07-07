# Knowledge Document: App.css (Chunk 23/43)

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
  "chunk_index": 22,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
ogin-hero-title {
    font-size: 22px;
  }

  .login-hero-content {
    padding: 24px 16px;
  }

  .login-form-container {
    max-width: 100%;
  }

  .tabs-header {
    gap: 2px;
    padding: 3px;
  }

  .tab-btn {
    padding: 8px 12px;
    font-size: 12px;
  }

  .role-badge.large {
    font-size: 12px;
    padding: 4px 12px;
  }
}

/* Very Small Mobile (< 320px) */
@media (max-width: 319px) {
  .page-title {
    font-size: 16px;
  }

  .auth-card {
    padding: 16px 12px;
    width: 96%;
  }

  .auth-logo-icon {
    font-size: 32px;
  }

  .auth-logo-text {
    font-size: 18px;
  }

  .layout-content {
    padding: 12px 8px;
  }

  .topbar-greeting {
    font-size: 10px;
  }

  .stats-grid,
  .actions-grid {
    gap: 8px;
  }

  .stat-card {
    padding: 12px;
  }
}

@media (max-width: 768px) {
  .sidebar {
    display: none;
  }

  .layout-content {
    padding: 20px 16px;
  }

  .topbar {
    position: relative;
    padding: 0 16px;
    gap: 12px;
    width: 100%;
  }

  .topbar-greeting {
    max-width: calc(100% - 96px);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .topbar-left {
    min-width: 0;
    padding-right: 0;
  }

  .topbar-right {
    display: none;
  }

  .topbar-logout {
    display: none;
  }

  .welcome-banner {
    flex-direction: column;
    text-align: center;
    padding: 24px 20px;
  }

  .welcome-illustration {
    font-size: 48px;
    margin-top: 16px;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .actions-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }

  .actions-grid {
    grid-template-columns: 1fr;
  }

  .auth-card {
    padding: 32px 24px;
  }
}

/* ============================================
   INVENTORY PAGES
   ============================================ */

.inventory-page {
  animation: fadeIn 0.3s ease;
}

/* Responsive Page Title */
.page-title {
  font-size: clamp(20px, 5vw, 28px);
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
}

.page-subtitle {
  font-size: clamp(11px, 2.5vw, 14px);
  color: var(--text-secondary);
  margin-top: 4px;
}

.btn-add {
  white-space: nowrap;
  padding: clamp(8px, 2vw, 10px) clamp(14px, 3vw, 20px);
  font-size: clamp(12px, 2.5vw, 14px);
}

/* Data Table */
.table-container {
  background: var(--bg-card);

```
