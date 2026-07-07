# Knowledge Document: AdminPage.css (Chunk 3/7)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/AdminPage.css",
  "language": "css",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin

## Source Code Chunk
```css
 color: #f59e0b; background: rgba(245, 158, 11, 0.1); }
.admin-kpi-violet .admin-kpi-icon { color: #8b5cf6; background: rgba(139, 92, 246, 0.1); }
.admin-kpi-rose .admin-kpi-icon { color: #f43f5e; background: rgba(244, 63, 94, 0.1); }

.admin-kpi-content {
  flex: 1;
}

.admin-kpi span {
  display: block;
  font-size: 13px;
  font-weight: 600;
  color: var(--text-secondary);
  margin-bottom: 6px;
}

.admin-kpi strong {
  display: block;
  font-size: 26px;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1;
}

.admin-kpi small {
  display: block;
  margin-top: 8px;
  font-size: 12px;
  color: var(--text-muted);
}

.admin-kpi small.positive { color: #10b981; }
.admin-kpi small.negative { color: #f43f5e; }

/* Mini Metric */
.admin-mini-metric {
  padding: 16px;
  align-items: center;
  min-height: 80px;
}

.admin-mini-metric svg {
  color: var(--accent-primary);
  background: rgba(99, 102, 241, 0.1);
  width: 36px;
  height: 36px;
  padding: 8px;
  border-radius: 8px;
}

.admin-mini-metric span {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-secondary);
}

.admin-mini-metric strong {
  font-size: 20px;
  font-weight: 800;
  color: var(--text-primary);
}

/* Charts */
.admin-chart-card {
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.admin-chart-card h3 {
  font-size: 15px;
  font-weight: 700;
  margin: 0 0 20px 0;
  color: var(--text-primary);
}

.admin-chart {
  height: 300px;
  flex: 1;
}

.admin-chart-empty {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  font-size: 13px;
  font-weight: 500;
  background: rgba(148, 163, 184, 0.05);
  border-radius: 8px;
  border: 1px dashed var(--border);
}

/* Tables */
.admin-table-wrap {
  overflow-x: auto;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--bg-card);
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.admin-table th {
  padding: 14px 16px;
  background: rgba(148, 163, 184, 0.04);
  color: var(--text-secondary);
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-bottom: 1px solid var(--border);
  white-space: nowrap;
}

.admin-table td {
  padding: 16px;
  border-bottom: 1px solid var(--border);
  color: var(--text-primary);
  font-size: 14px;
  vertical-align: middle;
}


```
