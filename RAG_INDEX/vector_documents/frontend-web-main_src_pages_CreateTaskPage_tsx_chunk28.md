# Knowledge Document: CreateTaskPage.tsx (Chunk 29/66)

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
  "chunk_index": 28,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
ackground: transparent;
                    border: 0;
                    outline: 0;
                    font: inherit;
                    font-size: 13px;
                    font-weight: 850;
                }
                .task-studio-priority {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                    min-height: 28px;
                }
                .task-studio-priority button {
                    padding: 0;
                    color: #8b6f58;
                    background: transparent;
                    border: 0;
                    font: inherit;
                    font-size: 13px;
                    font-weight: 850;
                    cursor: pointer;
                }
                .task-studio-priority button.active {
                    color: #3d2b1d;
                }
                .task-studio-priority button.active::before {
                    content: "";
                    display: inline-block;
                    width: 22px;
                    height: 2px;
                    margin-right: 7px;
                    vertical-align: middle;
                    background: #b87536;
                    box-shadow: 10px 0 0 #b87536;
                }
                .task-studio-cta {
                    min-width: 340px;
                    min-height: 64px;
                    margin-top: 6px;
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    gap: 12px;
                    color: #704018;
                    background: #ffb06f;
                    border: 0;
                    border-radius: 8px;
                    font: inherit;
                    font-size: 16px;
                    font-weight: 900;
                    cursor: pointer;
                    box-shadow: 0 18px 32px rgba(255, 176, 111, 0.28);
                    transition: transform 180ms ease, box-shadow 180ms ease, opacity 180ms ease;
                }
                .task-studio-cta:disabled {
                    opacity: 0.5;
                    cursor: not-allowed;
                    box-shadow: none;
                }
                .task-studio-cta:not(:disabled):hover {
                    transform: translateY(-1px);

```
