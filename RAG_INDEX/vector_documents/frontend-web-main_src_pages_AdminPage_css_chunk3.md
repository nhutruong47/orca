# Knowledge Document: AdminPage.css (Chunk 4/7)

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
  "chunk_index": 3,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin

## Source Code Chunk
```css
4px 16px;
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

.admin-table tr:last-child td {
  border-bottom: none;
}

.admin-table tr:hover td {
  background: rgba(148, 163, 184, 0.02);
}

.admin-table strong {
  font-weight: 600;
}

.admin-user-cell {
  display: flex;
  align-items: center;
  gap: 12px;
}

.admin-user-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 14px;
}

/* Badges */
.admin-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.admin-badge.success { background: rgba(16, 185, 129, 0.1); color: #10b981; }
.admin-badge.warning { background: rgba(245, 158, 11, 0.1); color: #f59e0b; }
.admin-badge.danger { background: rgba(244, 63, 94, 0.1); color: #f43f5e; }
.admin-badge.neutral { background: rgba(107, 114, 128, 0.1); color: #6b7280; }
.admin-badge.info { background: rgba(59, 130, 246, 0.1); color: #3b82f6; }

/* Buttons & Inputs */
.admin-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  border: 1px solid transparent;
}

.admin-button-primary {
  background: var(--primary-color);
  color: white;
}

.admin-button-primary:hover {
  background: #1d4ed8;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
}

.admin-button-secondary {
  background: var(--bg-input);
  color: var(--text-primary);
  border: 1px solid var(--border);
}

.admin-button-secondary:hover {
  background: var(--border);
}

.admin-toolbar {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.admin-search-input {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--bg-input);
  border: 1px solid var(--border);
  border-radius: 8px;

```
