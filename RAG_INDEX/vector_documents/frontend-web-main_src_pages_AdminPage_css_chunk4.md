# Knowledge Document: AdminPage.css (Chunk 5/7)

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
  "chunk_index": 4,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin

## Source Code Chunk
```css
(--bg-input);
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
  padding: 0 12px;
  flex: 1;
  min-width: 240px;
  height: 40px;
}

.admin-search-input input {
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-primary);
  width: 100%;
  font-size: 14px;
}

.admin-search-input input::placeholder {
  color: var(--text-muted);
}

.admin-search-input svg {
  color: var(--text-muted);
}

.admin-select {
  height: 40px;
  padding: 0 36px 0 12px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--bg-input);
  color: var(--text-primary);
  font-size: 14px;
  font-weight: 500;
  appearance: none;
  cursor: pointer;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%236b7280' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-position: right 12px center;
}

.admin-select option {
  background-color: var(--bg-card, #1e1e2e);
  color: var(--text-primary, #ffffff);
}

.admin-row-actions {
  display: flex;
  gap: 8px;
}

.btn-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  border: 1px solid transparent;
  background: transparent;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s;
}

.btn-icon:hover {
  background: var(--bg-input);
  color: var(--text-primary);
}

.btn-icon.danger:hover {
  background: rgba(244, 63, 94, 0.1);
  color: #f43f5e;
}

.btn-icon.success:hover {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

/* Date Range */
.admin-date-range {
  display: flex;
  align-items: center;
  gap: 12px;
}

.admin-date-picker {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.admin-date-picker span {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--text-muted);
  letter-spacing: 0.05em;
}

.admin-date-picker input {
  height: 40px;

```
