# Knowledge Document: CreateTaskPage.tsx (Chunk 21/66)

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
  "chunk_index": 20,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
type="button" onClick={() => setShowHistory(true)}>
                        <ion-icon name="time-outline"></ion-icon>
                        Lịch sử
                    </button>

                    <button className="task-gpt-action" type="button" onClick={() => setShowTokens(prev => !prev)}>
                        <ion-icon name="ellipsis-horizontal"></ion-icon>
                    </button>
                </div>
            </header>



            <main className="task-gpt-chat">
                <div className="task-gpt-inner">
                    {messages.length === 0 && !loading ? (
                        <section className="task-gpt-empty">
                            <h1>Hôm nay bạn muốn tạo công việc gì?</h1>
                            <p>Mô tả kế hoạch rang xay, đóng gói, QC hoặc đơn hàng. ORCA sẽ phân tích và đề xuất task có cấu trúc cho nhóm.</p>
                            <div className="task-gpt-suggestions">
                                {[
                                    'Rang 120kg Arabica trước 17:00 hôm nay',
                                    'Chia việc QC và đóng gói cho đơn hàng mới',
                                    'Tạo kế hoạch sản xuất cho tuần này',
                                    'Phân công nhóm xử lý batch đang trễ',
                                ].map(suggestion => (
                                    <button
                                        key={suggestion}
                                        className="task-gpt-suggestion"
                                        type="button"
                                        onClick={() => {
                                            setInput(suggestion);
                                            window.setTimeout(() => chatInputRef.current?.focus(), 0);
                                        }}
                                    >
                                        {suggestion}
                                    </button>
                                ))}
                            </div>
                        </section>
                    ) : (
                        <>
                            {messages.map(msg => (
                                <div key={msg.id} className={`task-gpt-message-row ${msg.role}`}>
                                    <article className="task-gpt-bubble">

```
