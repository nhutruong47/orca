# Knowledge Document: CreateTaskPage.tsx (Chunk 36/66)

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
  "chunk_index": 35,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
     transition: border-color 0.2s, background 0.2s, box-shadow 0.2s;
                }
                .task-select-trigger:hover,
                .task-select-trigger[aria-expanded="true"] {
                    background: rgba(255, 255, 255, 0.055);
                    border-color: rgba(212, 165, 116, 0.5);
                    box-shadow: 0 0 0 3px rgba(212, 165, 116, 0.12);
                }
                .task-select-menu {
                    position: absolute;
                    z-index: 30;
                    top: calc(100% + 8px);
                    left: 0;
                    right: 0;
                    padding: 6px;
                    margin: 0;
                    list-style: none;
                    border-radius: 12px;
                    border: 1px solid rgba(212, 165, 116, 0.24);
                    background: #0c1322;
                    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.35);
                    overflow: hidden;
                }
                .task-select-option {
                    width: 100%;
                    min-height: 38px;
                    padding: 0 12px;
                    border: 0;
                    border-radius: 8px;
                    background: transparent;
                    color: #d1bfae;
                    font: 500 14px/1 var(--font);
                    text-align: left;
                    cursor: pointer;
                    transition: background 0.18s, color 0.18s, box-shadow 0.18s;
                }
                .task-select-option:hover {
                    background: rgba(212, 165, 116, 0.12);
                    color: #fdf8f4;
                }
                .task-select-option.active {
                    background: rgba(212, 165, 116, 0.16);
                    color: #fdf8f4;
                    box-shadow: inset 3px 0 0 #d4a574;
                    font-weight: 700;
                }
                @media (max-width: 980px) {
                    .main-content-layout {
                        grid-template-columns: 1fr;
                    }
                }
            `}</style>

            {/* Navigation Header */}
            <div style={{ width: '100%', maxWidth: 1440, marginBottom: 32 }}>
                <button
                    onClick={() => navigate(`/groups/${teamId}`)}
                    style={{

```
