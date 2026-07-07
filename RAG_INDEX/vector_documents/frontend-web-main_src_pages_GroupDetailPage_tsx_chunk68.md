# Knowledge Document: GroupDetailPage.tsx (Chunk 69/136)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/GroupDetailPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "analytics",
    "dashboard",
    "admin",
    "production",
    "attendance",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 68,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                           <input value={chatInput} onChange={e => setChatInput(e.target.value)} onKeyDown={e => e.key === 'Enter' && handleSendChat()} placeholder={chatTab === 'dm' ? "Aa" : "Aa, nhắn cho nhóm..."} style={{ width: '100%', background: 'transparent', border: 'none', outline: 'none', fontSize: 14, color: 'var(--text-primary, #050505)' }} />
                                    </div>
                                    <button onClick={handleSendChat} disabled={!chatInput.trim() && !chatAttachment} style={{ width: 40, height: 40, borderRadius: '50%', background: chatInput.trim() || chatAttachment ? '#d4a574' : 'var(--bg-input, #e4e6eb)', border: 'none', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', cursor: chatInput.trim() || chatAttachment ? 'pointer' : 'default', flexShrink: 0, transition: 'background 0.15s' }} title="Gửi">
                                        <ion-icon name={chatInput.trim() || chatAttachment ? "send" : "thumbs-up"} style={{ fontSize: 18, marginLeft: chatInput.trim() || chatAttachment ? 2 : 0 }}></ion-icon>
                                    </button>
                                </div>
                            </>
                        ) : (
                            <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 32, textAlign: 'center', color: 'var(--text-secondary, #65676b)' }}>
                                <div>
                                    <div style={{ width: 120, height: 120, borderRadius: '50%', background: 'var(--bg-input, #f0f2f5)', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 16px' }}>
                                        <ion-icon name="chatbubbles" style={{ fontSize: 60, color: '#d4a574' }}></ion-icon>
                                    </div>
                                    <div style={{ fontWeight: 800, fontSize: 20, color: 'var(--text-primary, #050505)', marginBottom: 6 }}>Chào mừng bạn đến với đoạn chat</div>
                                    <div style={{ fontSize: 14 }}>Chọn một cuộc trò chuyện bên trái để bắt đầu nhắn tin</div>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* ===== MODALS (preserved) ===== */}

```
