# Knowledge Document: AiAssistantPanel.tsx (Chunk 6/10)

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
  "chunk_index": 5,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, chat

## Source Code Chunk
```tsx
          </div>
                ) : (
                    messages.map((msg) => (
                        <div key={msg.id} style={{
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: msg.role === 'user' ? 'flex-end' : 'flex-start',
                        }}>
                            {/* Message Bubble */}
                            <div className={`chat-bubble ${msg.role}`} style={{
                                maxWidth: '85%',
                                padding: '10px 14px',
                                borderRadius: '16px',
                                borderBottomRightRadius: msg.role === 'user' ? '2px' : '16px',
                                borderBottomLeftRadius: msg.role === 'assistant' ? '2px' : '16px',
                                background: msg.role === 'user' ? 'rgba(99,102,241,0.2)' : 'rgba(255,255,255,0.05)',
                                border: `1px solid ${msg.role === 'user' ? 'rgba(99,102,241,0.4)' : 'rgba(255,255,255,0.1)'}`,
                                color: 'var(--text-primary)',
                                fontSize: '13px',
                                lineHeight: '1.5',
                            }}>
                                {msg.content}
                            </div>
                            <span style={{ fontSize: '10px', color: 'var(--text-secondary)', marginTop: '4px', padding: '0 4px' }}>
                                {msg.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                                {showTokens && ` • ${formatTokenCount(estimateTokens(msg.content))} token`}
                            </span>

                            {/* AI Parsed Result UI */}
                            {msg.result && (
                                <div style={{
                                    marginTop: '8px',
                                    width: '100%',
                                    maxWidth: '90%',
                                    background: 'rgba(0,0,0,0.2)',
                                    border: '1px solid rgba(99,102,241,0.2)',
                                    borderRadius: '12px',
                                    padding: '14px 18px',
                                    alignSelf: 'flex-start',

```
