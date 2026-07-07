# Knowledge Document: CreateTaskPage.tsx (Chunk 31/66)

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
  "chunk_index": 30,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
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
                        grid-template-columns: 1fr;
                        justify-items: center;
                    }
                    .task-studio-back,
                    .task-studio-ghost {
                        justify-self: stretch;
                    }
                    .task-studio-meta {
                        grid-template-columns: 1fr;
                        gap: 18px;
                    }
                    .task-studio-card {
                        padding: 22px;
                        min-height: 300px;
                    }
                    .task-studio-input {
                        min-height: 180px;
                        font-size: 1.25rem;
                    }
                    .task-studio-cta {
                        width: 100%;
                    }
                }
            `}</style>

            <div className="task-studio-shell">
                <div className="task-studio-top">
                    <button className="task-studio-back" onClick={() => navigate(`/groups/${teamId}`)}>
                        <ion-icon name="arrow-back-outline"></ion-icon>
                        Tổng quan
                    </button>
                    <div className="task-studio-title">
                        <h1>Thiết lập Công việc</h1>
                        <p>Studio Minimalist · Quy trình Vận hành Cao cấp</p>
                    </div>
                    <button className="task-studio-ghost" onClick={() => {
                        setInput('Rang 120kg Arabica Cầu Đất trước 17:00 hôm nay, chia việc cho rang, QC và đóng gói.');
                        window.setTimeout(() => chatInputRef.current?.focus(), 0);
                    }}>
                        Xem ví dụ
                    </button>
                </div>

                <section className="task-studio-card" aria-label="Trợ lý AI ORCA">
                    <div className="task-studio-card-head">
                        <span>✦ Trợ lý AI ORCA</span>

```
