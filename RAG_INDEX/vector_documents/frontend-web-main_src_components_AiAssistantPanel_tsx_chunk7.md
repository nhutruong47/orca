# Knowledge Document: AiAssistantPanel.tsx (Chunk 8/10)

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
  "chunk_index": 7,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, chat

## Source Code Chunk
```tsx
                <div style={{ fontWeight: 600, color: 'var(--text-primary)' }}>{msg.result.title || '—'}</div>
                                        </div>
                                        <div>
                                            <span style={{ color: 'var(--text-secondary)', fontSize: 10 }}><ion-icon name="cube-outline" style={{ fontSize: '10px' }}></ion-icon> Khối lượng</span>
                                            <div style={{ fontWeight: 600, color: '#60a5fa' }}>{msg.result.quantity || '—'}</div>
                                        </div>
                                        <div>
                                            <span style={{ color: 'var(--text-secondary)', fontSize: 10 }}><ion-icon name="time-outline" style={{ fontSize: '10px' }}></ion-icon> Hạn chót</span>
                                            <div style={{ fontWeight: 600, color: '#f87171' }}>{msg.result.deadline || '—'}</div>
                                        </div>
                                        <div>
                                            <span style={{ color: 'var(--text-secondary)', fontSize: 10 }}><ion-icon name="options-outline" style={{ fontSize: '10px' }}></ion-icon> Ưu tiên</span>
                                            <div style={{ fontWeight: 600, color: priorityInfo[msg.result.priority]?.color || '#f59e0b' }}>
                                                {priorityInfo[msg.result.priority]?.icon} {priorityInfo[msg.result.priority]?.label || msg.result.priority}
                                            </div>
                                        </div>
                                    </div>

                                    {onCreateGoal && !msg.result.needsClarification && (
                                        <button
                                            className="btn btn-primary"
                                            onClick={() => onCreateGoal(msg.result!)}
                                            style={{ marginTop: 12, width: '100%', fontSize: 12, padding: '8px 0', background: 'rgba(99,102,241,0.2)', border: '1px solid rgba(99,102,241,0.4)', color: '#818cf8' }}
                                        >

```
