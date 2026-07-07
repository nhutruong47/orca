# Knowledge Document: DashboardPage.css (Chunk 1/6)

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
  "chunk_index": 0,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, dashboard

## Source Code Chunk
```css
.dashboard-page {
  display: flex;
  flex-direction: column;
  gap: 18px;
  color: var(--shell-text);
}

.dashboard-command,
.dashboard-stat-card,
.dashboard-panel,
.dashboard-empty {
  border: 1px solid var(--shell-border);
  border-radius: 8px;
  background: var(--shell-surface);
  box-shadow: var(--shell-shadow);
}

.dashboard-command {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(300px, 0.34fr);
  gap: 16px;
  padding: clamp(20px, 3vw, 28px);
  background:
    linear-gradient(135deg, rgba(212, 165, 116, 0.13), transparent 38%),
    linear-gradient(110deg, rgba(139, 94, 60, 0.15), transparent 54%),
    var(--shell-surface);
}

.dashboard-command-main {
  min-width: 0;
}

.dashboard-eyebrow,
.dashboard-section-head span,
.dashboard-stat-card span {
  color: var(--shell-accent);
  font-size: 11px;
  font-weight: 850;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.dashboard-command h1 {
  max-width: 760px;
  margin: 8px 0 8px;
  color: var(--shell-title);
  font-size: clamp(2rem, 4vw, 3.5rem);
  font-weight: 850;
  line-height: 1.03;
}

.dashboard-command p,
.dashboard-stat-card p,
.dashboard-team-card p,
.dashboard-task-row p,
.dashboard-empty p,
.dashboard-ops-card p {
  margin: 0;
  color: var(--shell-text-soft);
  font-size: 13px;
  line-height: 1.58;
}

.dashboard-command-main > p {
  max-width: 600px;
  font-size: 14px;
}

.dashboard-command-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 20px;
}

.dashboard-command-actions button,
.dashboard-section-head button,
.dashboard-empty button {
  min-height: 40px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 0 14px;
  border: 1px solid var(--shell-border);
  border-radius: 8px;
  background: var(--shell-surface-soft);
  color: var(--shell-title);
  font: 800 13px var(--font);
  cursor: pointer;
  transition: transform 0.18s ease, border-color 0.18s ease, background 0.18s ease;
}

.dashboard-command-actions .dashboard-primary-action,
.dashboard-empty button {
  background: var(--shell-accent);
  border-color: transparent;
  color: var(--shell-button-text);
}

.dashboard-command-actions button:hover,
.dashboard-section-head button:hover,
.dashboard-empty button:hover {
  transform: translateY(-1px);
  border-color: var(--shell-border-strong);
  background: var(--shell-surface-hover);
}


```
