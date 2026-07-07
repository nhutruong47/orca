# Knowledge Document: CreateTaskPage.tsx (Chunk 49/66)

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
  "chunk_index": 48,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
onKeyDown={e => {
                                    if (e.key === 'Enter' && !e.shiftKey) {
                                        e.preventDefault();
                                        handleSend();
                                    }
                                }}
                                placeholder={trialActive ? 'Mô tả công việc cần thực hiện...' : 'Dùng thử đã hết hạn'}
                                disabled={!trialActive || loading}
                                rows={2}
                                style={{
                                    flex: 1, fontSize: 15, fontFamily: 'inherit',
                                    background: 'var(--bg-card)',
                                    border: '2px solid #cbd5e1', // Slightly thicker border as per mockup
                                    borderRadius: '12px',
                                    padding: '14px 16px',
                                    resize: 'none', outline: 'none',
                                    color: 'var(--text-primary)'
                                }}
                            />
                            <button
                                onClick={handleSend}
                                disabled={!trialActive || loading || !input.trim()}
                                style={{
                                    height: 52, padding: '0 24px', borderRadius: '12px',
                                    background: (trialActive && input.trim() && !loading) ? '#a78bfa' : '#e2e8f0',
                                    color: (trialActive && input.trim() && !loading) ? '#ffffff' : '#94a3b8',
                                    border: 'none', fontSize: 16, fontWeight: 600, cursor: (trialActive && input.trim() && !loading) ? 'pointer' : 'not-allowed',
                                    display: 'flex', alignItems: 'center', gap: 6, transition: 'all 0.2s'
                                }}
                            >
                                <div style={{ width: 18, height: 18, border: '2px solid currentColor', borderRadius: '50%', opacity: 0.5 }}></div> Gửi
                            </button>
                        </div>
                        <div style={{ marginTop: 12, fontSize: 12, color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: 4 }}>

```
