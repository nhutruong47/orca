# Knowledge Document: CreateTaskPage.tsx (Chunk 11/66)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/CreateTaskPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "analytics",
  "tags": [
    "analytics",
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 10,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
 background: var(--bg-primary);
                }
                body.task-studio-mode .sidebar {
                    background: var(--bg-secondary);
                    border-right: 1px solid var(--border);
                    box-shadow: none;
                }
                body.task-studio-mode .sidebar-logo {
                    border-bottom: 0;
                    margin-bottom: 20px;
                }
                body.task-studio-mode .logo-text {
                    color: var(--accent-primary) !important;
                    -webkit-text-fill-color: var(--accent-primary);
                    letter-spacing: 0.12em;
                }
                body.task-studio-mode .logo-icon {
                    color: var(--accent-primary) !important;
                    background: var(--bg-secondary);
                    box-shadow: inset 0 0 0 1px var(--border);
                }
                body.task-studio-mode .nav-label {
                    color: var(--text-secondary);
                    opacity: 1;
                }
                body.task-studio-mode .nav-item {
                    color: var(--text-primary);
                    background: transparent;
                    border-radius: 10px;
                    font-weight: 520;
                }
                body.task-studio-mode .nav-item.active,
                body.task-studio-mode .nav-item:hover {
                    color: var(--accent-primary);
                    background: rgba(50, 34, 20, 0.04);
                    box-shadow: none;
                    transform: none;
                }
                body.task-studio-mode .nav-item.active::before {
                    display: none;
                }
                .task-gpt-page {
                    min-height: 100vh;
                    display: grid;
                    grid-template-rows: auto minmax(0, 1fr) auto;
                    color: var(--text-primary);
                    background: var(--bg-primary);
                    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
                }
                .task-gpt-topbar {
                    min-height: 56px;
                    display: grid;
                    grid-template-columns: 1fr auto;
                    align-items: center;
                    padding: 0 26px;
                }

```
