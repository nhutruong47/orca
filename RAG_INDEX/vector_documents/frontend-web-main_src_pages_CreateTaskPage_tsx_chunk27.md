# Knowledge Document: CreateTaskPage.tsx (Chunk 28/66)

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
  "chunk_index": 27,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
                 background: currentColor;
                    box-shadow: 0 0 0 4px rgba(88, 201, 156, 0.12);
                }
                .task-studio-input {
                    flex: 1;
                    width: 100%;
                    min-height: clamp(190px, 23vh, 300px);
                    padding: 0;
                    color: #4d3928;
                    background: transparent;
                    border: 0;
                    resize: none;
                    outline: none;
                    font: inherit;
                    font-size: clamp(1.35rem, 2.2vw, 2rem);
                    font-weight: 800;
                    line-height: 1.45;
                }
                .task-studio-input::placeholder {
                    color: rgba(79, 64, 52, 0.16);
                }
                .task-studio-tools {
                    display: flex;
                    justify-content: flex-end;
                    gap: 14px;
                    color: #c8b8a7;
                    font-size: 16px;
                }
                .task-studio-meta {
                    width: min(1080px, 100%);
                    display: grid;
                    grid-template-columns: repeat(3, minmax(0, 1fr));
                    gap: clamp(28px, 4vw, 64px);
                }
                .task-studio-field {
                    min-height: 56px;
                    border-bottom: 1px solid #e8ded3;
                }
                .task-studio-field label {
                    display: block;
                    margin-bottom: 8px;
                    color: #b1a093;
                    font-size: 10px;
                    font-weight: 900;
                    letter-spacing: 0.12em;
                    text-transform: uppercase;
                }
                .task-studio-select,
                .task-studio-time {
                    width: 100%;
                    min-height: 28px;
                    color: #3d2b1d;
                    background: transparent;
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

```
