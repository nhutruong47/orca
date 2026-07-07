# Knowledge Document: CreateTaskPage.tsx (Chunk 64/66)

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
  "chunk_index": 63,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
ld('deadline', e.target.value)}
                                style={{
                                    width: '100%', padding: '12px 16px', borderRadius: '12px',
                                    border: '1px solid var(--border)', background: 'var(--bg-card)',
                                    color: 'var(--text-primary)', fontSize: 14, outline: 'none'
                                }}
                            />
                        </div>
                        <div>
                            <label style={{ display: 'block', fontSize: 13, fontWeight: 700, color: 'var(--text-secondary)', marginBottom: 8 }}>Ưu tiên</label>
                            <div style={{ display: 'flex', borderRadius: '12px', border: '1px solid var(--border)', overflow: 'hidden', background: 'var(--bg-card)' }}>
                                {['Low', 'Medium', 'High'].map((p) => (
                                    <button
                                        key={p}
                                        onClick={() => updateField('priority', p)}
                                        style={{
                                            flex: 1, padding: '12px 0', fontSize: 13, fontWeight: 700,
                                            border: 'none', borderRight: p !== 'High' ? '1px solid #f1f5f9' : 'none',
                                            background: (editedResult.priority?.toLowerCase() || 'medium') === p.toLowerCase() ? '#d4a574' : 'transparent',
                                            color: (editedResult.priority?.toLowerCase() || 'medium') === p.toLowerCase() ? '#fff' : '#64748b',
                                            cursor: 'pointer', transition: 'all 0.2s'
                                        }}
                                    >
                                        {p}
                                    </button>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>

                {/* Suggested Questions */}
                {editedResult.suggestedQuestions && editedResult.suggestedQuestions.length > 0 && (
                    <div style={{ marginTop: 24, borderTop: '1px solid #f1f5f9', paddingTop: 20 }}>

```
