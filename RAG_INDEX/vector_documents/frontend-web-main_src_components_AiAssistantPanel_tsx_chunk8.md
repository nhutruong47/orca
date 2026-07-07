# Knowledge Document: AiAssistantPanel.tsx (Chunk 9/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/AiAssistantPanel.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "payment",
  "tags": [
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 8,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, chat

## Source Code Chunk
```tsx
                               className="btn btn-primary"
                                            onClick={() => onCreateGoal(msg.result!)}
                                            style={{ marginTop: 12, width: '100%', fontSize: 12, padding: '8px 0', background: 'rgba(99,102,241,0.2)', border: '1px solid rgba(99,102,241,0.4)', color: '#818cf8' }}
                                        >
                                            <ion-icon name="arrow-forward-circle-outline" style={{ fontSize: '14px', verticalAlign: 'middle', marginRight: 4 }}></ion-icon> Tạo mục tiêu
                                        </button>
                                    )}
                                </div>
                            )}
                        </div>
                    ))
                )}

                {loading && (
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start' }}>
                        <div className="chat-bubble assistant" style={{
                            padding: '10px 14px', borderRadius: '16px', borderBottomLeftRadius: '2px',
                            background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)',
                            color: 'var(--text-secondary)', fontSize: '13px', display: 'flex', gap: '6px', alignItems: 'center'
                        }}>
                            <span className="dot-typing"></span> Đang suy nghĩ...
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef} />
            </div>

            {/* Input Form */}
            <div style={{ display: 'flex', gap: 8, marginTop: 'auto' }}>
                <input
                    className="form-input"
                    value={input}
                    onChange={e => setInput(e.target.value)}
                    onKeyDown={e => {
                        if (e.key === 'Enter' && !e.shiftKey) {
                            e.preventDefault();
                            handleSend();
                        }
                    }}
                    placeholder={trialActive ? 'Nhập yêu cầu quản lý xưởng...' : 'Dùng thử đã hết hạn'}
                    disabled={!trialActive || loading}
                    style={{
                        flex: 1, fontSize: 13,

```
