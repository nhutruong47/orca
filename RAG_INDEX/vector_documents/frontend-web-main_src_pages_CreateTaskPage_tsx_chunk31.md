# Knowledge Document: CreateTaskPage.tsx (Chunk 32/66)

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
  "chunk_index": 31,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
gói.');
                        window.setTimeout(() => chatInputRef.current?.focus(), 0);
                    }}>
                        Xem ví dụ
                    </button>
                </div>

                <section className="task-studio-card" aria-label="Trợ lý AI ORCA">
                    <div className="task-studio-card-head">
                        <span>✦ Trợ lý AI ORCA</span>
                        {trialActive ? (
                            <span className="task-studio-status">Sẵn sàng</span>
                        ) : (
                            <button
                                type="button"
                                className="task-studio-status"
                                onClick={() => navigate('/upgrade')}
                                style={{ cursor: 'pointer', border: 0 }}
                            >
                                Nâng cấp gói
                            </button>
                        )}
                    </div>
                    <textarea
                        ref={chatInputRef}
                        className="task-studio-input"
                        value={input}
                        onChange={e => setInput(e.target.value)}
                        onKeyDown={e => {
                            if (e.key === 'Enter' && !e.shiftKey) {
                                e.preventDefault();
                                handleSend();
                            }
                        }}
                        placeholder={trialActive ? 'Mô tả nhiệm vụ hoặc kế hoạch rang xay của bạn tại đây...' : 'Dùng thử đã hết hạn'}
                        disabled={!trialActive || loading}
                    />
                    <div className="task-studio-tools" aria-hidden="true">
                        <ion-icon name="mic-outline"></ion-icon>
                        <ion-icon name="attach-outline"></ion-icon>
                    </div>
                </section>

                <section className="task-studio-meta" aria-label="Thông tin công việc">
                    <div className="task-studio-field">
                        <label>Nhóm công tác</label>
                        <select className="task-studio-select" value={category} onChange={event => setCategory(event.target.value)}>
                            {categoryOptions.map(option => (

```
