# Knowledge Document: DashboardPage.css (Chunk 4/6)

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
  "chunk_index": 3,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, dashboard

## Source Code Chunk
```css
);
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
  display: grid;
  grid-template-columns: minmax(0, 1.28fr) minmax(340px, 0.72fr);
  gap: 18px;
  align-items: start;
}

.dashboard-panel {
  padding: 20px;
}

.dashboard-section-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 14px;
  margin-bottom: 16px;
}

.dashboard-section-head h2 {
  margin: 5px 0 0;
  color: var(--shell-title);
  font-size: 22px;
  font-weight: 850;
  line-height: 1.2;
}

.dashboard-section-head button {
  min-width: 118px;
}

.dashboard-team-list {
  display: grid;
  gap: 12px;
}

.dashboard-team-card {
  display: grid;
  grid-template-columns: 168px minmax(0, 1fr);
  min-height: 158px;
  overflow: hidden;
  border: 1px solid var(--shell-border);
  border-radius: 8px;
  background: var(--shell-surface-soft);
  cursor: pointer;
  outline: none;
  transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
}

.dashboard-team-card:hover,
.dashboard-team-card:focus-visible {
  border-color: var(--shell-border-strong);
  box-shadow: var(--shell-hover-shadow);
  transform: translateY(-2px);
}

.dashboard-team-card img {
  width: 100%;
  height: 100%;
  min-height: 158px;
  display: block;
  object-fit: cover;
  filter: saturate(0.92) contrast(1.02);
}

.dashboard-team-body {
  min-width: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 14px;
  padding: 16px;
}

.dashboard-team-card h3,
.dashboard-task-row h3,
.dashboard-empty h3 {
  margin: 0;
  color: var(--shell-title);
  font-size: 16px;
  font-weight: 850;
  line-height: 1.3;
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

```
