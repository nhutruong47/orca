# Knowledge Document: DashboardPage.css (Chunk 3/6)

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
  "chunk_index": 2,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, dashboard

## Source Code Chunk
```css
border-radius: 8px;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.035), transparent),
    var(--shell-surface-soft);
}

.dashboard-ops-card.overloaded {
  border-color: rgba(239, 68, 68, 0.3);
  background:
    linear-gradient(180deg, rgba(239, 68, 68, 0.08), transparent),
    var(--shell-surface-soft);
}

.dashboard-ops-card.overloaded .dashboard-ops-head {
  color: #ef4444;
}

.dashboard-ops-card.overachieving {
  border-color: rgba(34, 197, 94, 0.3);
  background:
    linear-gradient(180deg, rgba(34, 197, 94, 0.08), transparent),
    var(--shell-surface-soft);
}

.dashboard-ops-card.overachieving .dashboard-ops-head {
  color: #22c55e;
}

.dashboard-ops-head {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--shell-accent);
  font-size: 12px;
  font-weight: 850;
  text-transform: uppercase;
}

.dashboard-ops-card strong {
  color: var(--shell-title);
  font-size: 22px;
  line-height: 1.2;
}

.dashboard-progress-track {
  width: 100%;
  height: 8px;
  overflow: hidden;
  border-radius: 999px;
  background: rgba(148, 163, 184, 0.18);
}

.dashboard-progress-track span {
  display: block;
  min-width: 8px;
  height: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg, #8b5e3c, #f5b15e);
}

.dashboard-ops-card small {
  color: var(--shell-text-muted);
  font-size: 12px;
  font-weight: 700;
}

.dashboard-stat-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
}

.dashboard-stat-card {
  min-height: 126px;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 14px;
  padding: 18px;
}

.dashboard-stat-icon {
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  background: rgba(212, 165, 116, 0.15);
  color: #d4a574;
}

.dashboard-stat-card.amber .dashboard-stat-icon {
  background: rgba(245, 177, 94, 0.16);
  color: #f5b15e;
}

.dashboard-stat-card.green .dashboard-stat-icon {
  background: rgba(139, 94, 60, 0.22);
  color: #c28a52;
}

.dashboard-stat-card.blue .dashboard-stat-icon {
  background: rgba(120, 79, 43, 0.24);
  color: #b97832;
}

.dashboard-stat-card strong {
  display: block;
  margin-top: 9px;
  color: var(--shell-title);
  font-size: clamp(1.45rem, 2.6vw, 2.25rem);
  line-height: 1.06;
  overflow-wrap: anywhere;
}

.dashboard-stat-card p {
  margin-top: 6px;
}

.dashboard-workspace-grid {

```
