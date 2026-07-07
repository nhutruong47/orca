# Knowledge Document: App.css (Chunk 14/43)

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
  "chunk_index": 13,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
ion-icon {
  font-size: 22px;
}

.topbar-avatar:hover {
  transform: scale(1.05);
  box-shadow: 0 0 12px rgba(88, 166, 255, 0.3);
}

.topbar-logout {
  padding: 7px 14px;
  border: 1px solid var(--danger);
  border-radius: 8px;
  background: transparent;
  color: var(--danger);
  font-size: 12px;
  font-weight: 600;
  font-family: var(--font);
  cursor: pointer;
  transition: var(--transition);
}

.topbar-logout:hover {
  background: rgba(248, 81, 73, 0.12);
  border-color: rgba(248, 81, 73, 0.4);
}

.goal-roadmap-markdown {
  width: 100%;
  max-width: 100%;
  overflow-x: auto;
  scrollbar-width: thin;
}

.goal-roadmap-markdown > *:first-child {
  margin-top: 0;
}

.goal-roadmap-markdown > *:last-child {
  margin-bottom: 0;
}

.goal-roadmap-markdown h1,
.goal-roadmap-markdown h2,
.goal-roadmap-markdown h3,
.goal-roadmap-markdown h4 {
  margin: 14px 0 10px;
  color: #172033;
  font-size: 1rem;
  line-height: 1.35;
}

.goal-roadmap-markdown p {
  margin: 0 0 10px;
  color: #24324a;
}

.goal-roadmap-markdown table {
  min-width: 760px;
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  overflow: hidden;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  background: #fff;
}

.goal-roadmap-markdown thead th {
  background: #f8fafc;
  color: #334155;
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.goal-roadmap-markdown th,
.goal-roadmap-markdown td {
  padding: 12px 14px;
  border-bottom: 1px solid #eef2f7;
  color: #24324a;
  font-size: 0.86rem;
  line-height: 1.55;
  vertical-align: middle;
  text-align: left;
}

.goal-roadmap-markdown tbody tr:last-child td {
  border-bottom: 0;
}

.goal-roadmap-markdown tbody tr:nth-child(even) td {
  background: #fcfdff;
}

.goal-roadmap-markdown strong {
  color: #172033;
  font-weight: 800;
}

/* ============================================
   TABS (Order Management, etc.)
   ============================================ */
.tabs-container {
  margin-bottom: 20px;
}

.tabs-header {
  display: flex;
  gap: 4px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 4px;
}

.tab-btn {
  flex: 1;
  padding: 10px 20px;
  border: none;
  border-radius: 10px;
  background: transparent;
  color: var(--text-secondary);
  font-size: 13px;
  font-weight: 600;
  font-family: var(--font);
  cursor: pointer;

```
