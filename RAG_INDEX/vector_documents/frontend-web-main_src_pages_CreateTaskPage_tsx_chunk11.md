# Knowledge Document: CreateTaskPage.tsx (Chunk 12/66)

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
  "chunk_index": 11,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
                    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
                }
                .task-gpt-topbar {
                    min-height: 56px;
                    display: grid;
                    grid-template-columns: 1fr auto;
                    align-items: center;
                    padding: 0 26px;
                }
                .task-gpt-model {
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    color: var(--text-primary);
                    font-size: 18px;
                    font-weight: 650;
                }
                .task-gpt-actions {
                    display: inline-flex;
                    align-items: center;
                    gap: 16px;
                    color: var(--text-primary);
                    font-size: 14px;
                    font-weight: 650;
                }
                .task-gpt-action {
                    display: inline-flex;
                    align-items: center;
                    gap: 6px;
                    color: inherit;
                    background: transparent;
                    border: 0;
                    font: inherit;
                    cursor: pointer;
                }
                .task-gpt-chat {
                    min-height: 0;
                    overflow-y: auto;
                    padding: 34px 24px 170px;
                }
                .task-gpt-inner {
                    width: min(1200px, 100%);
                    margin: 0 auto;
                    display: grid;
                    gap: 28px;
                }
                .task-gpt-empty {
                    min-height: min(58vh, 560px);
                    display: grid;
                    align-content: center;
                    justify-items: center;
                    text-align: center;
                }
                .task-gpt-empty h1 {
                    margin: 0 0 14px;
                    color: var(--text-primary);
                    font-size: clamp(1.8rem, 3vw, 2.6rem);
                    font-weight: 650;
                    letter-spacing: 0;
                }
                .task-gpt-empty p {
                    max-width: 620px;
                    margin: 0;
                    color: var(--text-secondary);

```
