# Knowledge Document: App.css (Chunk 24/43)

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
  "chunk_index": 23,
  "total_chunks": 43
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, admin, inventory, security, notification

## Source Code Chunk
```css
 clamp(20px, 5vw, 28px);
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
}

.page-subtitle {
  font-size: clamp(11px, 2.5vw, 14px);
  color: var(--text-secondary);
  margin-top: 4px;
}

.btn-add {
  white-space: nowrap;
  padding: clamp(8px, 2vw, 10px) clamp(14px, 3vw, 20px);
  font-size: clamp(12px, 2.5vw, 14px);
}

/* Data Table */
.table-container {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow-x: auto;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table thead {
  background: rgba(255, 255, 255, 0.03);
}

/* Data Table - Responsive */
.data-table th {
  text-align: left;
  padding: clamp(10px, 2vw, 14px) clamp(10px, 2vw, 16px);
  font-size: clamp(10px, 2vw, 12px);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--text-muted);
  border-bottom: 1px solid var(--border);
}

.data-table td {
  padding: clamp(10px, 2vw, 14px) clamp(10px, 2vw, 16px);
  font-size: clamp(12px, 2.5vw, 14px);
  color: var(--text-primary);
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}

.data-table tbody tr {
  transition: var(--transition);
}

.data-table tbody tr:hover {
  background: rgba(212, 165, 116, 0.04);
}

.data-table tbody tr:last-child td {
  border-bottom: none;
}

.td-name {
  font-weight: 500;
}

.td-desc {
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.td-actions {
  display: flex;
  gap: 6px;
}

/* Badges */
.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.badge-info {
  background: rgba(212, 156, 87, 0.15);
  color: var(--accent-primary);
}

.badge-success {
  background: rgba(34, 197, 94, 0.15);
  color: #4ade80;
}

.badge-danger {
  background: rgba(239, 68, 68, 0.15);
  color: #f87171;
}

.badge-warning {
  background: rgba(245, 158, 11, 0.15);
  color: #fbbf24;
}

/* Status Select (inline dropdown) */
.status-select {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  color: var(--text-primary);
  padding: 4px 8px;
  font-size: 12px;
  cursor: pointer;
  transition: var(--transition);
}

.status-select:hover {
  border-color: rgba(212, 165, 116, 0.5);
}

.status-select:focus {
  outline: none;
  border-color: var(--primary);

```
