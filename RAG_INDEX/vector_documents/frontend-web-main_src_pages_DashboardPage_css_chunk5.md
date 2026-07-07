# Knowledge Document: DashboardPage.css (Chunk 6/6)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/DashboardPage.css",
  "language": "css",
  "module": "pages",
  "business_domain": "workspace",
  "tags": [
    "workspace",
    "dashboard"
  ],
  "logical_type": "Generic",
  "chunk_index": 5,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, dashboard

## Source Code Chunk
```css
  align-items: center;
  justify-content: center;
  text-align: center;
  color: var(--shell-text-soft);
}

@media (max-width: 1180px) {
  .dashboard-stat-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .dashboard-quick-actions {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .dashboard-workspace-grid,
  .dashboard-command {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 760px) {
  .dashboard-stat-grid {
    grid-template-columns: 1fr;
  }

  .dashboard-quick-actions {
    grid-template-columns: 1fr;
  }

  .dashboard-team-card,
  .dashboard-task-row {
    grid-template-columns: 1fr;
  }

  .dashboard-team-card img {
    height: 190px;
  }

  .dashboard-section-head {
    align-items: stretch;
    flex-direction: column;
  }

  .dashboard-section-head button,
  .dashboard-command-actions button,
  .dashboard-empty button {
    width: 100%;
  }
}

```
