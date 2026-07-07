# Knowledge Document: App.css (Chunk 19/43)

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
  "chunk_index": 18,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
) */
@media (max-width: 1439px) and (min-width: 1024px) {
  .layout-content {
    padding: 28px 32px;
  }

  .page-title {
    font-size: 26px;
  }

  .section-title {
    font-size: 16px;
  }

  .stats-grid {
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 14px;
  }

  .actions-grid {
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 12px;
  }
}

/* Tablet Landscape (768px - 1023px) */
@media (max-width: 1023px) and (min-width: 768px) {
  .sidebar {
    display: none;
  }

  .layout {
    width: 100%;
  }

  .layout-main {
    width: 100%;
  }

  .layout-content {
    padding: 24px 20px;
    overflow-y: auto;
    overflow-x: hidden;
  }

  .topbar {
    padding: 0 16px;
    gap: 12px;
  }

  .topbar-right {
    display: flex !important;
  }

  .topbar-logout {
    display: block !important;
    padding: 6px 12px;
    font-size: 12px;
  }

  .topbar-greeting {
    font-size: 13px;
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
    margin-bottom: 24px;
  }

  .btn-add {
    width: 100%;
  }

  .page-title {
    font-size: 24px;
  }

  .section-title {
    font-size: 16px;
  }

  .welcome-banner {
    flex-direction: column;
    text-align: center;
    padding: 28px 20px;
  }

  .welcome-name {
    font-size: 24px;
  }

  .welcome-illustration {
    font-size: 56px;
    margin-top: 16px;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }

  .actions-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }

  .auth-card {
    padding: 32px 24px;
    width: 90%;
  }

  .data-table th,
  .data-table td {
    padding: 12px 12px;
    font-size: 12px;
  }

  .td-desc {
    max-width: 120px;
  }
}

/* Tablet Portrait (481px - 767px) */
@media (max-width: 767px) and (min-width: 481px) {
  .sidebar {
    display: none;
  }

  .layout {
    width: 100%;
  }

  .layout-main {
    width: 100%;
  }

  .layout-content {
    padding: 20px 16px;
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

```
