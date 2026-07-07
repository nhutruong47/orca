# Knowledge Document: CreateTaskPage.tsx (Chunk 15/66)

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
  "chunk_index": 14,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
r {
                    width: min(1200px, 100%);
                    min-height: 74px;
                    margin: 0 auto;
                    display: grid;
                    grid-template-columns: auto minmax(0, 1fr) auto auto;
                    align-items: end;
                    gap: 10px;
                    padding: 10px 12px 10px 16px;
                    background: var(--bg-card);
                    border: 1px solid var(--border);
                    border-radius: 28px;
                    box-shadow: 0 10px 34px rgba(0, 0, 0, 0.08);
                }
                .task-gpt-icon-btn,
                .task-gpt-send {
                    width: 42px;
                    height: 42px;
                    display: grid;
                    place-items: center;
                    border: 0;
                    border-radius: 50%;
                    font: inherit;
                    cursor: pointer;
                }
                .task-gpt-icon-btn {
                    color: var(--text-primary);
                    background: transparent;
                    font-size: 24px;
                }
                .task-gpt-textarea {
                    width: 100%;
                    max-height: 170px;
                    min-height: 42px;
                    padding: 9px 4px;
                    color: var(--text-primary);
                    background: transparent;
                    border: 0;
                    outline: 0;
                    resize: none;
                    font: inherit;
                    font-size: 16px;
                    line-height: 1.5;
                }
                .task-gpt-textarea::placeholder {
                    color: var(--text-muted);
                }
                .task-gpt-mode {
                    min-height: 34px;
                    display: inline-flex;
                    align-items: center;
                    gap: 6px;
                    padding: 0 10px;
                    color: var(--text-secondary);
                    background: transparent;
                    border: 0;
                    font: inherit;
                    font-size: 14px;
                }
                .task-gpt-send {
                    color: var(--bg-primary);
                    background: var(--text-primary);
                    font-size: 18px;
                }

```
