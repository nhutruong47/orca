# Knowledge Document: index.css (Chunk 5/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/index.css",
  "language": "css",
  "module": "src",
  "business_domain": "admin",
  "tags": [
    "admin",
    "inventory",
    "dashboard"
  ],
  "logical_type": "Generic",
  "chunk_index": 4,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in src.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, inventory, dashboard

## Source Code Chunk
```css
ary);
  color: var(--text-primary);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#root {
  height: 100%;
}

a {
  text-decoration: none;
  color: inherit;
}

/* ===== Scrollbar ===== */
::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: var(--bg-tertiary);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--text-muted);
}

/* ===== Animations ===== */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }

  100% {
    background-position: 200% 0;
  }
}

@keyframes pulse-glow {

  0%,
  100% {
    box-shadow: 0 0 0 0 rgba(88, 166, 255, 0.2);
  }

  50% {
    box-shadow: 0 0 0 8px rgba(88, 166, 255, 0);
  }
}

/* ===== Markdown Styles ===== */
.markdown-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  font-size: 13px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.markdown-body th {
  background-color: #f8fafc;
  color: #334155;
  font-weight: 700;
  text-align: left;
  padding: 12px 16px;
  border-bottom: 2px solid #e2e8f0;
}

.markdown-body td {
  padding: 12px 16px;
  border-bottom: 1px solid #f1f5f9;
  color: #475569;
  font-weight: 500;
}

.markdown-body tr:last-child td {
  border-bottom: none;
}

.markdown-body tr:hover td {
  background-color: #f8fafc;
}

.markdown-content table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  font-size: 13px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.markdown-content th {
  background-color: #f8fafc;
  color: #334155;
  font-weight: 700;
  text-align: left;
  padding: 12px 16px;
  border-bottom: 2px solid #e2e8f0;
}

.markdown-content td {
  padding: 12px 16px;
  border-bottom: 1px solid #f1f5f9;
  color: #475569;
  font-weight: 500;
}

/* ===== Force-light overrides (higher specificity) ===== */
body.theme-light .layout,
body.theme-light .layout-main,
body.theme-light .layout-content {
  background: var(--bg-primary) !important;
  color: var(--text-primary) !important;
}

body.theme-light .sidebar {
  background: var(--bg-secondary) !important;

```
