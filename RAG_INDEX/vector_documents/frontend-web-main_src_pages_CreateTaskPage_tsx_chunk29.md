# Knowledge Document: CreateTaskPage.tsx (Chunk 30/66)

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
  "chunk_index": 29,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
28);
                    transition: transform 180ms ease, box-shadow 180ms ease, opacity 180ms ease;
                }
                .task-studio-cta:disabled {
                    opacity: 0.5;
                    cursor: not-allowed;
                    box-shadow: none;
                }
                .task-studio-cta:not(:disabled):hover {
                    transform: translateY(-1px);
                    box-shadow: 0 22px 38px rgba(255, 176, 111, 0.34);
                }
                .task-studio-note {
                    margin: 0;
                    color: #b6a79a;
                    font-size: 11px;
                    font-weight: 600;
                }
                .task-studio-thread {
                    width: min(1080px, 100%);
                    display: grid;
                    gap: 14px;
                    margin-top: 10px;
                }
                .task-studio-message {
                    padding: 16px 18px;
                    border: 1px solid #eadfd4;
                    border-radius: 8px;
                    background: rgba(255, 255, 255, 0.72);
                    color: #4d3928;
                    line-height: 1.65;
                    box-shadow: 0 10px 24px rgba(83, 58, 37, 0.06);
                }
                .task-studio-message.user {
                    background: rgba(255, 176, 111, 0.18);
                    border-color: rgba(255, 176, 111, 0.42);
                }
                .task-studio-message.assistant {
                    background: rgba(255, 255, 255, 0.86);
                }
                .task-studio-loading {
                    color: #8a5a2f;
                    font-weight: 800;
                }
                .task-studio-token {
                    display: inline-block;
                    margin-top: 8px;
                    color: #a49487;
                    font-size: 11px;
                    font-weight: 800;
                }
                .task-studio-result {
                    margin-top: 14px;
                }
                .task-studio-result .ai-refine-card {
                    box-shadow: none !important;
                }
                @media (max-width: 900px) {
                    .task-studio-page {
                        padding: 26px 18px;
                    }
                    .task-studio-top {

```
