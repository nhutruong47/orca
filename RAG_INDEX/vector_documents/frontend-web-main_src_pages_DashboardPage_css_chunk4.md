# Knowledge Document: DashboardPage.css (Chunk 5/6)

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
  "chunk_index": 4,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, dashboard

## Source Code Chunk
```css
.3;
}

.dashboard-team-card p,
.dashboard-task-row p {
  margin-top: 6px;
}

.dashboard-team-card dl {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 8px;
  margin: 0;
}

.dashboard-team-card dl div {
  min-width: 0;
  padding: 9px 10px;
  border: 1px solid var(--shell-border);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.03);
}

.dashboard-team-card dt {
  color: var(--shell-text-muted);
  font-size: 10px;
  font-weight: 800;
  text-transform: uppercase;
}

.dashboard-team-card dd {
  margin: 3px 0 0;
  color: var(--shell-text);
  font-size: 13px;
  font-weight: 800;
  overflow-wrap: anywhere;
}

.dashboard-task-list {
  display: grid;
  gap: 10px;
}

.dashboard-task-row {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border: 1px solid var(--shell-border);
  border-radius: 8px;
  background: var(--shell-surface-soft);
}

.dashboard-task-mark {
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  background: rgba(212, 165, 116, 0.15);
  color: #d4a574;
}

.dashboard-task-copy {
  min-width: 0;
}

.dashboard-task-status {
  flex: 0 0 auto;
  padding: 7px 10px;
  border-radius: 999px;
  background: rgba(245, 177, 94, 0.16);
  color: #f5b15e;
  font-size: 11px;
  font-weight: 850;
  text-transform: uppercase;
  white-space: nowrap;
}

.dashboard-task-status.completed {
  background: rgba(120, 79, 43, 0.20);
  color: #c28a52;
}

.dashboard-task-status.in-progress {
  background: rgba(212, 165, 116, 0.16);
  color: #d4a574;
}

.dashboard-empty {
  display: grid;
  justify-items: start;
  gap: 10px;
  padding: 24px;
  color: var(--shell-text-soft);
}

.dashboard-empty svg {
  color: var(--shell-accent);
}

.dashboard-empty p {
  max-width: 520px;
}

.dashboard-empty button {
  margin-top: 4px;
}

.dashboard-empty-compact {
  min-height: 212px;
  align-content: center;
}

.dashboard-loading {
  min-height: 70vh;
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


```
