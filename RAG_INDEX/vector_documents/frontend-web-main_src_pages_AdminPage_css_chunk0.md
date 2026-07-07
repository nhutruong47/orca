# Knowledge Document: AdminPage.css (Chunk 1/7)

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
  "chunk_index": 0,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin

## Source Code Chunk
```css
.admin-app {
  display: flex;
  min-height: 100vh;
  /* Sync background with global theme */
  background: var(--bg-primary);
  color: var(--text-primary);
}

/* Ensure global app container doesn't restrict it */
:root {
  --admin-sidebar-width: 260px;
}

/* Sidebar */
.admin-sidebar {
  width: var(--admin-sidebar-width);
  background: var(--bg-card);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  flex-shrink: 0;
}

.admin-sidebar-header {
  padding: 0 12px 24px;
  margin-bottom: 12px;
  border-bottom: 1px solid var(--border);
}

.admin-sidebar-header h2 {
  font-size: 18px;
  font-weight: 800;
  margin: 0;
  color: var(--text-primary);
  letter-spacing: -0.02em;
}

.admin-sidebar-header p {
  font-size: 12px;
  color: var(--text-secondary);
  margin: 4px 0 0;
}

.admin-nav {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.admin-nav button {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border: none;
  background: transparent;
  color: var(--text-secondary);
  font-size: 14px;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  text-align: left;
  transition: all 0.2s ease;
}

.admin-nav button:hover {
  background: var(--bg-input);
  color: var(--text-primary);
}

.admin-nav button.active {
  background: rgba(37, 99, 235, 0.1);
  color: var(--primary-color);
}

.admin-nav-section {
  margin-top: 16px;
  margin-bottom: 4px;
  padding: 0 12px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
}

/* Main Content */
.admin-main {
  flex: 1;
  padding: 32px 40px;
  overflow-y: auto;
  max-width: 100%;
}

.admin-main-inner {
  width: 100%;
  max-width: none;
  margin: 0;
}

/* Hero / Header */
.admin-hero {
  margin-bottom: 32px;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
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

```
