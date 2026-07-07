# Knowledge Document: GroupDetailPage.tsx (Chunk 67/136)

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
  "chunk_index": 66,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
: '2-digit' })}
                                                        {showChatTokens && ` • ${formatTokenCount(estimateTokens(msg.content))} token`}
                                                    </div>
                                                </div>
                                            </div>
                                        );
                                    })}
                                    <div ref={chatEndRef} />
                                </div>

                                {/* Attachment preview */}
                                {chatAttachment && (
                                    <div style={{ padding: '10px 16px', background: 'var(--bg-input, #f0f2f5)', borderTop: '1px solid var(--border, #e4e6eb)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                                        <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 13, color: 'var(--text-primary, #050505)' }}>
                                            <ion-icon name="document-text" style={{ color: '#d4a574', fontSize: 20 }}></ion-icon>
                                            <span style={{ maxWidth: 240, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{chatAttachment.name}</span>
                                        </div>
                                        <button onClick={() => setChatAttachment(null)} style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-secondary, #65676b)', display: 'flex' }}><ion-icon name="close-circle" style={{ fontSize: 20 }}></ion-icon></button>
                                    </div>
                                )}

                                {/* Chat input (Messenger-style) */}
                                <div style={{ padding: '12px 16px', borderTop: '1px solid var(--border, #e4e6eb)', background: 'var(--bg-card, #fff)', display: 'flex', alignItems: 'center', gap: 8 }}>
                                    <input type="file" ref={fileInputRef} style={{ display: 'none' }} onChange={e => { if(e.target.files && e.target.files[0]) setChatAttachment(e.target.files[0]) }} />

```
