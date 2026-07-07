# Knowledge Document: AdminPage.css (Chunk 7/7)

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
  "chunk_index": 6,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin

## Source Code Chunk
```css
ar(--text-secondary);
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

/* Responsive */
@media (max-width: 1200px) {
  .admin-kpi-grid, .admin-mini-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .admin-grid-3 {
    grid-template-columns: repeat(2, 1fr);
  }
  .admin-plan-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 900px) {
  .admin-app {
    flex-direction: column;
  }
  .admin-sidebar {
    width: 100%;
    height: auto;
    position: static;
    border-right: none;
    border-bottom: 1px solid var(--border);
  }
  .admin-hero {
    flex-direction: column;
    align-items: flex-start;
  }
  .admin-grid-2, .admin-grid-3, .admin-plan-grid {
    grid-template-columns: 1fr;
  }
}

```
