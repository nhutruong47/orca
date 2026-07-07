# Knowledge Document: CreateTaskPage.tsx (Chunk 44/66)

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
  "chunk_index": 43,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
rent?.focus(), 0);
                                }}
                                style={{ background: 'none', border: 'none', color: '#d4a574', fontSize: 13, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 4 }}
                            >
                                <ion-icon name="book-outline"></ion-icon> Xem ví dụ
                            </button>
                        </div>
                    </div>

                    {/* Trial Banner */}
                    <div style={{ background: trialActive ? 'rgba(16,185,129,0.1)' : 'rgba(239,68,68,0.1)', padding: '8px 24px', fontSize: 12, fontWeight: 600, color: trialActive ? '#10b981' : '#ef4444', display: 'flex', alignItems: 'center', gap: 6, borderBottom: '1px solid var(--border)' }}>
                        <ion-icon name={trialActive ? "checkmark-circle" : "warning"}></ion-icon> {trialActive ? `Còn ${trialDays} ngày dùng thử API` : 'Hết hạn dùng thử API. Vui lòng nâng cấp.'}
                    </div>

                    {/* Chat Area */}
                    <div style={{
                        flex: 1, minHeight: 0, padding: '24px', overflowY: 'auto',
                        display: 'flex', flexDirection: 'column', gap: 16,
                        background: 'var(--bg-input)' // Slight off-white background to match screenshot
                    }}>
                        {messages.length === 0 ? (
                            <div style={{ margin: 'auto', textAlign: 'center', opacity: 0.5 }}>
                                <ion-icon name="chatbubbles-outline" style={{ fontSize: '48px', marginBottom: '12px' }}></ion-icon>
                                <p style={{ margin: 0, fontSize: '15px' }}>Hãy mô tả công việc của bạn...</p>
                            </div>
                        ) : (
                            messages.map((msg) => (
                                <div key={msg.id} style={{
                                    display: 'flex',
                                    flexDirection: 'column',
                                    alignItems: msg.role === 'user' ? 'flex-end' : 'flex-start',
                                    width: '100%'
                                }}>
                                    {msg.role === 'user' ? (
                                        <div style={{

```
