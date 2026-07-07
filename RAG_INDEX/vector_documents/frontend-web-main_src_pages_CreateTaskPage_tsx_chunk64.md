# Knowledge Document: CreateTaskPage.tsx (Chunk 65/66)

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
  "chunk_index": 64,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
n>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>

                {/* Suggested Questions */}
                {editedResult.suggestedQuestions && editedResult.suggestedQuestions.length > 0 && (
                    <div style={{ marginTop: 24, borderTop: '1px solid #f1f5f9', paddingTop: 20 }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 12, color: '#d4a574', fontSize: 13, fontWeight: 700 }}>
                            <ion-icon name="bulb-outline"></ion-icon> Gợi ý từ AI để tối ưu kế hoạch:
                        </div>
                        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10 }}>
                            {editedResult.suggestedQuestions.map((q, idx) => (
                                <button
                                    key={idx}
                                    onClick={() => onAsk(q)}
                                    style={{
                                        background: 'var(--bg-card)', border: '1px solid var(--border)',
                                        color: '#4f46e5', padding: '8px 16px', borderRadius: '12px',
                                        fontSize: 13, fontWeight: 600, cursor: 'pointer',
                                        transition: 'all 0.2s', boxShadow: '0 2px 4px rgba(0,0,0,0.02)'
                                    }}
                                    onMouseOver={e => { e.currentTarget.style.background = '#f5f3ff'; e.currentTarget.style.borderColor = '#c7d2fe'; }}
                                    onMouseOut={e => { e.currentTarget.style.background = '#fff'; e.currentTarget.style.borderColor = '#e0e7ff'; }}
                                >
                                    {q}
                                </button>
                            ))}
                        </div>
                    </div>
                )}

                {/* Footer Buttons */}
                {!isConfirmed && !isCancelled && !isArchived && (
                    <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 12, marginTop: 32 }}>
                        <button
                            onClick={onCancel}

```
