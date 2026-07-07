# Knowledge Document: CreateTaskPage.tsx (Chunk 27/66)

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
  "chunk_index": 26,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
           text-align: center;
                }
                .task-studio-title h1 {
                    margin: 0 0 7px;
                    color: #3d2b1d;
                    font-size: 13px;
                    font-weight: 500;
                    letter-spacing: 0;
                }
                .task-studio-title p {
                    margin: 0;
                    color: #a49487;
                    font-family: Georgia, "Times New Roman", serif;
                    font-size: 13px;
                    font-style: italic;
                }
                .task-studio-card {
                    width: min(1080px, 100%);
                    min-height: clamp(300px, 34vh, 430px);
                    display: flex;
                    flex-direction: column;
                    padding: clamp(30px, 3.2vw, 44px);
                    background: rgba(255, 255, 255, 0.82);
                    border: 1px solid rgba(213, 198, 181, 0.78);
                    border-radius: 4px;
                    box-shadow: 0 18px 46px rgba(83, 58, 37, 0.09);
                }
                .task-studio-card-head {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    margin-bottom: 20px;
                    color: #8a4f22;
                    font-size: 11px;
                    font-weight: 900;
                    letter-spacing: 0.08em;
                    text-transform: uppercase;
                }
                .task-studio-status {
                    display: inline-flex;
                    align-items: center;
                    gap: 6px;
                    color: #58c99c;
                    font-size: 10px;
                    font-weight: 900;
                }
                .task-studio-status::before {
                    content: "";
                    width: 7px;
                    height: 7px;
                    border-radius: 50%;
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

```
