# Knowledge Document: AdminPage.css (Chunk 6/7)

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
  "chunk_index": 5,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin

## Source Code Chunk
```css
, 129, 0.1);
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
  padding: 0 12px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--bg-input);
  color: var(--text-primary);
  font-family: inherit;
  font-size: 14px;
}

/* Pagination */
.admin-pagination {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 16px;
  border-top: 1px solid var(--border);
  margin-top: 20px;
}

.admin-pagination span {
  font-size: 13px;
  color: var(--text-secondary);
}

.admin-pagination-buttons {
  display: flex;
  gap: 8px;
}

.admin-pagination-buttons button {
  width: 36px;
  height: 36px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--bg-card);
  color: var(--text-primary);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
}

.admin-pagination-buttons button:hover:not(:disabled) {
  background: var(--bg-input);
}

.admin-pagination-buttons button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.admin-pagination-buttons button.active {
  background: var(--primary-color);
  color: white;
  border-color: var(--primary-color);
}

/* Plans */
.admin-plan-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 32px;
}

.admin-plan {
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
  background: var(--bg-card);
}

.admin-plan h4 {
  font-size: 16px;
  font-weight: 700;
  margin: 0 0 12px 0;
}

.admin-plan .price {
  font-size: 32px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 20px;
}

.admin-plan .price span {
  font-size: 14px;
  font-weight: 500;
  color: var(--text-secondary);
}

.admin-plan-limits {
  background: var(--bg-input);
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 20px;
  display: grid;
  gap: 10px;
}

.admin-plan-limit-item {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
}

.admin-plan-limit-item span {
  color: var(--text-secondary);
}

.admin-plan-limit-item strong {
  color: var(--text-primary);
}


```
