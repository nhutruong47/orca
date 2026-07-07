# Knowledge Document: GroupDetailPage.tsx (Chunk 66/136)

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
  "chunk_index": 65,
  "total_chunks": 136
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, analytics, dashboard, admin, production, attendance, inventory, employee, chat

## Source Code Chunk
```tsx
                             <div style={{ width: 28, flexShrink: 0 }} />
                                                )}
                                                <div style={{ maxWidth: '65%', display: 'flex', flexDirection: 'column', alignItems: isMe ? 'flex-end' : 'flex-start' }}>
                                                    {isFirstOfGroup && !isMe && chatTab === 'group' && (
                                                        <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-secondary, #65676b)', marginBottom: 2, paddingLeft: 10 }}>{msg.senderName}</div>
                                                    )}
                                                    <div style={{
                                                        background: isMe ? '#d4a574' : 'var(--bg-input, #f0f2f5)',
                                                        color: isMe ? '#fff' : 'var(--text-primary, #050505)',
                                                        borderRadius: isMe ? '18px 18px 4px 18px' : '18px 18px 18px 4px',
                                                        padding: '8px 12px',
                                                        fontSize: 14,
                                                        lineHeight: 1.4,
                                                        wordBreak: 'break-word',
                                                        whiteSpace: 'pre-wrap',
                                                        boxShadow: 'none'
                                                    }}>
                                                        {msg.content}
                                                    </div>
                                                    <div style={{ fontSize: 11, color: 'var(--text-muted, #65676b)', marginTop: 2, padding: '0 6px' }}>
                                                        {new Date(msg.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                                                        {showChatTokens && ` • ${formatTokenCount(estimateTokens(msg.content))} token`}
                                                    </div>
                                                </div>
                                            </div>
                                        );
                                    })}

```
