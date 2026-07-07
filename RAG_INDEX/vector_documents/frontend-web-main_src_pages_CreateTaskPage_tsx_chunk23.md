# Knowledge Document: CreateTaskPage.tsx (Chunk 24/66)

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
  "chunk_index": 23,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
ssage(msg.id)} style={{ cursor: 'pointer', color: '#ef4444' }} title="Xóa đoạn chat này"></ion-icon>
                                                {showTokens && <span className="task-gpt-token">{formatTokenCount(estimateTokens(msg.content))} token</span>}
                                            </div>
                                        )}
                                    </article>
                                </div>
                            ))}
                            {loading && (
                                <div className="task-gpt-message-row assistant">
                                    <article className="task-gpt-bubble task-gpt-loading">ORCA đang phân tích kế hoạch...</article>
                                </div>
                            )}
                            <div ref={messagesEndRef} />
                        </>
                    )}
                </div>
            </main>

            <footer className="task-gpt-composer-wrap">
                <div className="task-gpt-composer">
                    <button className="task-gpt-icon-btn" type="button" aria-label="Thêm nội dung">
                        <ion-icon name="add-outline"></ion-icon>
                    </button>
                    <textarea
                        ref={chatInputRef}
                        className="task-gpt-textarea"
                        value={input}
                        onChange={e => setInput(e.target.value)}
                        onKeyDown={e => {
                            if (e.key === 'Enter' && !e.shiftKey) {
                                e.preventDefault();
                                handleSend();
                            }
                        }}
                        placeholder={hasActiveDraft ? 'Nhập yêu cầu sửa draft, ví dụ: Rút gọn còn 2 task' : 'Nhập yêu cầu, ví dụ: Rang 120kg Arabica trước 17:00 hôm nay'}
                        disabled={loading}
                        rows={1}
                    />
                    <button className="task-gpt-mode" type="button">
                        {hasActiveDraft ? 'Sửa draft' : 'Tạo draft'}
                        <ion-icon name="chevron-down-outline"></ion-icon>
                    </button>
                    <button
                        className="task-gpt-send"
                        type="button"

```
