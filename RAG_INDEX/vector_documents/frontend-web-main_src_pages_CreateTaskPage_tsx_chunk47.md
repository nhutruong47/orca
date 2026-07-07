# Knowledge Document: CreateTaskPage.tsx (Chunk 48/66)

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
  "chunk_index": 47,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
  ))}
                                                </div>
                                            )}
                                        </div>
                                    )}
                                    {showTokens && (
                                        <span style={{ marginTop: 6, padding: '0 6px', color: 'var(--text-secondary)', fontSize: 11, fontWeight: 700 }}>
                                            {formatTokenCount(estimateTokens(msg.content))} token
                                        </span>
                                    )}
                                </div>
                            ))
                        )}

                        {loading && (
                            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start' }}>
                                <div style={{
                                    padding: '14px 18px', borderRadius: '20px', borderBottomLeftRadius: '4px',
                                    background: 'var(--bg-secondary)', color: 'var(--text-secondary)', fontSize: '15px', display: 'flex', gap: '8px', alignItems: 'center'
                                }}>
                                    <span className="dot-typing" style={{ background: '#94a3b8' }}></span> Đang phân tích...
                                </div>
                            </div>
                        )}
                        <div ref={messagesEndRef} />
                    </div>

                    {/* Input Area */}
                    <div style={{ padding: '24px', borderTop: '1px solid var(--border)', background: 'var(--bg-card)' }}>
                        <div style={{ display: 'flex', gap: 12, alignItems: 'flex-end' }}>
                            <textarea
                                ref={chatInputRef}
                                value={input}
                                onChange={e => setInput(e.target.value)}
                                onKeyDown={e => {
                                    if (e.key === 'Enter' && !e.shiftKey) {
                                        e.preventDefault();
                                        handleSend();
                                    }
                                }}
                                placeholder={trialActive ? 'Mô tả công việc cần thực hiện...' : 'Dùng thử đã hết hạn'}

```
