# Knowledge Document: CreateTaskPage.tsx (Chunk 23/66)

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
  "chunk_index": 22,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
                                     />
                                            </div>
                                        )}
                                        {msg.result && msg.isArchived && (
                                            <div style={{
                                                marginTop: 12,
                                                padding: '10px 12px',
                                                borderRadius: 10,
                                                background: '#f5f3ff',
                                                color: '#6d28d9',
                                                fontSize: 13,
                                                fontWeight: 600
                                            }}>
                                                Bản trước gồm {msg.result.tasks?.length || 0} công việc đã được chuyển vào lịch sử.
                                            </div>
                                        )}
                                        {msg.role === 'assistant' && (
                                            <div className="task-gpt-message-actions">
                                                <ion-icon name="copy-outline" onClick={() => handleCopyMessage(msg.content)} style={{ cursor: 'pointer' }} title="Copy"></ion-icon>
                                                <ion-icon name="thumbs-up-outline" onClick={() => alert('Cảm ơn bạn đã đánh giá!')} style={{ cursor: 'pointer' }} title="Hữu ích"></ion-icon>
                                                <ion-icon name="thumbs-down-outline" onClick={() => alert('Cảm ơn bạn đã đánh giá!')} style={{ cursor: 'pointer' }} title="Chưa tốt"></ion-icon>
                                                <ion-icon name="refresh-outline" style={{ cursor: 'pointer' }} title="Thử lại"></ion-icon>
                                                <ion-icon name="trash-outline" onClick={() => handleDeleteMessage(msg.id)} style={{ cursor: 'pointer', color: '#ef4444' }} title="Xóa đoạn chat này"></ion-icon>
                                                {showTokens && <span className="task-gpt-token">{formatTokenCount(estimateTokens(msg.content))} token</span>}
                                            </div>
                                        )}
                                    </article>

```
