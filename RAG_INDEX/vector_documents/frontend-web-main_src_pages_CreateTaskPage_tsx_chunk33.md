# Knowledge Document: CreateTaskPage.tsx (Chunk 34/66)

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
  "chunk_index": 33,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
            <ion-icon name="arrow-forward-outline"></ion-icon>
                </button>
                <p className="task-studio-note">⊙ ORCA sẽ tự động phân loại và giao việc cho các thành viên liên quan.</p>

                {(messages.length > 0 || loading) && (
                    <section className="task-studio-thread" aria-label="Kết quả AI">
                        {messages.map(msg => (
                            <article key={msg.id} className={`task-studio-message ${msg.role}`}>
                                <div className="markdown-content">
                                    <ReactMarkdown remarkPlugins={[remarkGfm]}>{friendlyTaskError(msg.content)}</ReactMarkdown>
                                </div>
                                {msg.result && !msg.result.needsClarification && (
                                    <div className="task-studio-result">
                                            <AiResultRefinementForm
                                                result={msg.result}
                                                members={team?.members || []}
                                                onConfirm={(finalData) => handleCreateGoal(finalData)}
                                                onAsk={(question) => {
                                                    setInput(question);
                                                chatInputRef.current?.focus();
                                            }}
                                        />
                                    </div>
                                )}
                                {showTokens && <span className="task-studio-token">{formatTokenCount(estimateTokens(msg.content))} token</span>}
                            </article>
                        ))}
                        {loading && <div className="task-studio-message assistant task-studio-loading">Đang phân tích...</div>}
                        <div ref={messagesEndRef} />
                    </section>
                )}

                <div style={{ display: 'flex', gap: 12, minHeight: 28 }}>
                    {messages.length > 0 && (
                        <button className="task-studio-ghost" onClick={clearHistory}>
                            <ion-icon name="trash-outline"></ion-icon>
                            Xóa lịch sử
                        </button>

```
