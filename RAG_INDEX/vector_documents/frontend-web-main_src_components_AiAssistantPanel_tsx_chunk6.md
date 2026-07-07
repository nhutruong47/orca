# Knowledge Document: AiAssistantPanel.tsx (Chunk 7/10)

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
  "chunk_index": 6,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, chat

## Source Code Chunk
```tsx
          width: '100%',
                                    maxWidth: '90%',
                                    background: 'rgba(0,0,0,0.2)',
                                    border: '1px solid rgba(99,102,241,0.2)',
                                    borderRadius: '12px',
                                    padding: '14px 18px',
                                    alignSelf: 'flex-start',
                                }}>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 12 }}>
                                        <span style={{ fontSize: 10, padding: '2px 8px', borderRadius: 8, background: msg.result.source === 'gemini' ? 'rgba(99,102,241,0.15)' : 'rgba(245,158,11,0.15)', color: msg.result.source === 'gemini' ? '#818cf8' : '#f59e0b', fontWeight: 700 }}>
                                            {msg.result.source === 'gemini' ? 'Gemini AI' : 'Regex'}
                                        </span>
                                        {msg.result.needsClarification && (
                                            <span style={{ fontSize: 10, padding: '2px 8px', borderRadius: 8, background: 'rgba(245,158,11,0.1)', color: '#f59e0b' }}>
                                                <ion-icon name="warning-outline" style={{ fontSize: '12px', verticalAlign: 'middle', marginRight: 4 }}></ion-icon> Thiếu thông tin
                                            </span>
                                        )}
                                    </div>

                                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 12px', fontSize: 12 }}>
                                        <div>
                                            <span style={{ color: 'var(--text-secondary)', fontSize: 10 }}><ion-icon name="document-text-outline" style={{ fontSize: '10px' }}></ion-icon> Tiêu đề</span>
                                            <div style={{ fontWeight: 600, color: 'var(--text-primary)' }}>{msg.result.title || '—'}</div>
                                        </div>
                                        <div>
                                            <span style={{ color: 'var(--text-secondary)', fontSize: 10 }}><ion-icon name="cube-outline" style={{ fontSize: '10px' }}></ion-icon> Khối lượng</span>

```
