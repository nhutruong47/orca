# Knowledge Document: DashboardPage.css (Chunk 2/6)

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
  "chunk_index": 1,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: workspace, dashboard

## Source Code Chunk
```css
mmand-actions .dashboard-primary-action,
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

.dashboard-command-actions .dashboard-primary-action:hover,
.dashboard-empty button:hover {
  background: var(--shell-accent-strong);
}

.dashboard-quick-actions {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: 10px;
}

.dashboard-quick-actions button {
  min-width: 0;
  min-height: 72px;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px;
  border: 1px solid var(--shell-border);
  border-radius: 8px;
  background: var(--shell-surface);
  color: var(--shell-title);
  text-align: left;
  cursor: pointer;
  box-shadow: var(--shell-shadow);
  transition: transform 0.18s ease, border-color 0.18s ease, background 0.18s ease;
}

.dashboard-quick-actions button:hover {
  transform: translateY(-1px);
  border-color: var(--shell-border-strong);
  background: var(--shell-surface-hover);
}

.dashboard-quick-icon {
  width: 36px;
  height: 36px;
  display: grid;
  flex: 0 0 auto;
  place-items: center;
  border-radius: 8px;
  background: var(--shell-accent-soft);
  color: var(--shell-accent);
}

.dashboard-quick-actions strong,
.dashboard-quick-actions small {
  display: block;
  min-width: 0;
}

.dashboard-quick-actions strong {
  font-size: 13px;
  font-weight: 850;
  line-height: 1.25;
}

.dashboard-quick-actions small {
  margin-top: 3px;
  color: var(--shell-text-muted);
  font-size: 11px;
  font-weight: 650;
  line-height: 1.35;
}

.dashboard-ops-card {
  min-height: 178px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 10px;
  padding: 18px;
  border: 1px solid var(--shell-border);
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


```
