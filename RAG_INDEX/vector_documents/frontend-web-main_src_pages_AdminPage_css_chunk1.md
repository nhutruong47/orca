# Knowledge Document: AdminPage.css (Chunk 2/7)

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
  "chunk_index": 1,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin

## Source Code Chunk
```css
en;
  gap: 20px;
}

.admin-hero h1 {
  font-size: 28px;
  font-weight: 800;
  margin: 0 0 8px 0;
  letter-spacing: -0.02em;
  color: var(--text-primary);
}

.admin-hero p {
  margin: 0;
  color: var(--text-secondary);
  font-size: 15px;
  max-width: 600px;
  line-height: 1.5;
}

.admin-hero-actions {
  display: flex;
  gap: 10px;
}

/* Cards & Layout */
.admin-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05), 0 1px 2px rgba(0,0,0,0.03);
  margin-bottom: 24px;
}

.admin-card-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 20px;
  gap: 16px;
}

.admin-card-head h3 {
  margin: 0 0 4px 0;
  font-size: 18px;
  font-weight: 700;
  color: var(--text-primary);
}

.admin-card-head p {
  margin: 0;
  color: var(--text-secondary);
  font-size: 13px;
}

.admin-kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 24px;
}

.admin-mini-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.admin-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-bottom: 24px;
}

.admin-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 24px;
}

/* KPI Elements */
.admin-kpi, .admin-mini-metric {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  display: flex;
  align-items: flex-start;
  gap: 16px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}

.admin-kpi-icon {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.admin-kpi-blue .admin-kpi-icon { color: #3b82f6; background: rgba(59, 130, 246, 0.1); }
.admin-kpi-green .admin-kpi-icon { color: #10b981; background: rgba(16, 185, 129, 0.1); }
.admin-kpi-amber .admin-kpi-icon { color: #f59e0b; background: rgba(245, 158, 11, 0.1); }
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

```
