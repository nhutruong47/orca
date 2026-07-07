# Knowledge Document: CreateTaskPage.tsx (Chunk 16/66)

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
  "chunk_index": 15,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
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
                .task-gpt-send:disabled {
                    background: var(--border);
                    color: var(--text-muted);
                    cursor: not-allowed;
                }
                .task-gpt-disclaimer {
                    width: min(880px, 100%);
                    margin: 8px auto 0;
                    color: var(--text-muted);
                    font-size: 12px;
                    text-align: center;
                }
                .markdown-content p {
                    margin: 0 0 12px;
                }
                .markdown-content p:last-child {
                    margin-bottom: 0;
                }
                .markdown-content table {
                    border-collapse: collapse;
                    width: 100%;
                    margin: 12px 0;
                    font-size: 13px;
                    background: var(--bg-card);
                }
                .markdown-content th,
                .markdown-content td {
                    border: 1px solid var(--border);
                    padding: 10px;
                    text-align: left;
                }
                .markdown-content th {
                    background: var(--bg-secondary);
                    font-weight: 700;
                }
                @media (max-width: 760px) {
                    .task-gpt-topbar {
                        padding-inline: 16px;
                    }
                    .task-gpt-chat {
                        padding-inline: 16px;
                    }
                    .task-gpt-suggestions {
                        grid-template-columns: 1fr;
                    }
                    .task-gpt-message-row.user .task-gpt-bubble,
                    .task-gpt-bubble {
                        max-width: 92%;
                    }
                    .task-gpt-mode {
                        display: none;
                    }
                    .task-gpt-composer {

```
