# Knowledge Document: CreateTaskPage.tsx (Chunk 13/66)

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
  "chunk_index": 12,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
h1 {
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
                    font-size: 16px;
                    line-height: 1.6;
                }
                .task-gpt-suggestions {
                    margin-top: 28px;
                    display: grid;
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                    gap: 12px;
                    width: min(880px, 100%);
                }
                .task-gpt-suggestion {
                    min-height: 54px;
                    padding: 0 16px;
                    color: var(--text-primary);
                    background: var(--bg-card);
                    border: 1px solid var(--border);
                    border-radius: 14px;
                    font: inherit;
                    font-size: 14px;
                    font-weight: 520;
                    text-align: left;
                    cursor: pointer;
                }
                .task-gpt-suggestion:hover {
                    background: var(--bg-card-hover);
                }
                .task-gpt-message-row {
                    display: flex;
                    width: 100%;
                }
                .task-gpt-message-row.user {
                    justify-content: flex-end;
                }
                .task-gpt-message-row.assistant {
                    justify-content: flex-start;
                }
                .task-gpt-bubble {
                    max-width: min(960px, 90%);
                    color: var(--text-primary);
                    font-size: 16px;
                    line-height: 1.72;
                }
                .task-gpt-message-row.user .task-gpt-bubble {
                    max-width: min(720px, 75%);
                    padding: 11px 18px;
                    background: var(--bg-secondary);
                    border-radius: 22px;
                }
                .task-gpt-message-row.assistant .task-gpt-bubble {
                    padding: 0;
                    background: transparent;
                }

```
