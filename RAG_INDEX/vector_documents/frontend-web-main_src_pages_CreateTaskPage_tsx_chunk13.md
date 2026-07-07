# Knowledge Document: CreateTaskPage.tsx (Chunk 14/66)

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
  "chunk_index": 13,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
t-message-row.user .task-gpt-bubble {
                    max-width: min(720px, 75%);
                    padding: 11px 18px;
                    background: var(--bg-secondary);
                    border-radius: 22px;
                }
                .task-gpt-message-row.assistant .task-gpt-bubble {
                    padding: 0;
                    background: transparent;
                }
                .task-gpt-assistant-head {
                    margin-bottom: 8px;
                    color: var(--text-primary);
                    font-size: 15px;
                    font-weight: 650;
                }
                .task-gpt-message-actions {
                    display: flex;
                    align-items: center;
                    gap: 16px;
                    margin-top: 14px;
                    color: var(--text-secondary);
                    font-size: 18px;
                }
                .task-gpt-token {
                    margin-left: auto;
                    color: var(--text-muted);
                    font-size: 12px;
                    font-weight: 650;
                }
                .task-gpt-result {
                    margin-top: 20px;
                    padding: 18px;
                    border: 1px solid var(--border);
                    border-radius: 16px;
                    background: var(--bg-card);
                    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04);
                }
                .task-gpt-loading {
                    color: var(--text-secondary);
                    font-size: 16px;
                    line-height: 1.6;
                }
                .task-gpt-composer-wrap {
                    position: sticky;
                    bottom: 0;
                    z-index: 10;
                    padding: 18px 24px 14px;
                    background: var(--bg-primary);
                    border-top: 1px solid var(--border);
                }
                .task-gpt-composer {
                    width: min(1200px, 100%);
                    min-height: 74px;
                    margin: 0 auto;
                    display: grid;
                    grid-template-columns: auto minmax(0, 1fr) auto auto;
                    align-items: end;
                    gap: 10px;
                    padding: 10px 12px 10px 16px;
                    background: var(--bg-card);

```
