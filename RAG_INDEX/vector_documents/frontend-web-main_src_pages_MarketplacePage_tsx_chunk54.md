# Knowledge Document: MarketplacePage.tsx (Chunk 55/70)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/MarketplacePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "notification",
    "factory",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 54,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
 }}>
                                <span className="material-symbols-outlined" style={{fontSize: 20}}>videocam</span>
                            </button>
                            <button className="fb-chat-close" onClick={(e) => { e.stopPropagation(); setShowChatModal(false); }}>
                                <span className="material-symbols-outlined" style={{fontSize: 20}}>close</span>
                            </button>
                        </div>
                    </div>
                    <div className="fb-chat-body">
                        {chatMessages.map((msg, i) => (
                            <div key={i} className={`fb-msg-row ${msg.sender === 'me' ? 'sent' : 'received'}`}>
                                <div className="fb-msg-bubble">
                                    {msg.text}
                                </div>
                            </div>
                        ))}
                    </div>
                    <div className="fb-chat-footer">
                        <span className="material-symbols-outlined" style={{color: '#d4a574', cursor: 'pointer', fontSize: 24}} onClick={() => alert('Tính năng gửi file đang được phát triển')}>attach_file</span>
                        <span className="material-symbols-outlined" style={{color: '#d4a574', cursor: 'pointer', fontSize: 24}} onClick={() => alert('Tính năng gửi ảnh đang được phát triển')}>image</span>
                        <input
                            className="fb-chat-input"
                            placeholder="Nhập tin nhắn..."
                            value={chatDraft}
                            onChange={event => setChatDraft(event.target.value)}
                            onKeyDown={e => {
                                if (e.key === 'Enter' && chatDraft.trim()) {
                                    handleSaveChatDraft();
                                }
                            }}
                        />
                        <button className="fb-chat-send" onClick={() => { if(chatDraft.trim()) handleSaveChatDraft(); }} disabled={!chatDraft.trim()}>
                            <span className="material-symbols-outlined" style={{fontSize: 24}}>send</span>
                        </button>
                    </div>
                </div>
            )}

            {showOrderModal && (

```
