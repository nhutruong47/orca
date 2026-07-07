# Knowledge Document: CreateTaskPage.tsx (Chunk 43/66)

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
  "chunk_index": 42,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
          <ion-icon name="sparkles"></ion-icon>
                            </div>
                            <div>
                                <h3 style={{ margin: 0, fontSize: 16, fontWeight: 700, color: 'var(--text-primary)' }}>AI Xử Lý Công Việc</h3>
                                <p style={{ margin: 0, fontSize: 13, color: 'var(--text-secondary)' }}>Mô tả mục tiêu một cách tự nhiên</p>
                            </div>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                            <button onClick={() => setShowTokens(prev => !prev)} style={{ background: showTokens ? 'rgba(167,139,250,0.12)' : 'none', border: '1px solid var(--border)', color: showTokens ? '#7c3aed' : 'var(--text-secondary)', fontSize: 12, fontWeight: 700, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, padding: '4px 10px', borderRadius: 6 }}>
                                <ion-icon name="analytics-outline"></ion-icon> {showTokens ? `${formatTokenCount(totalTokens)} token` : 'Xem token'}
                            </button>
                            {messages.length > 0 && (
                                <button onClick={clearHistory} style={{ background: 'none', border: '1px solid var(--border)', color: '#ef4444', fontSize: 12, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6, padding: '4px 10px', borderRadius: 6 }}>
                                    <ion-icon name="trash-outline"></ion-icon> Xóa lịch sử
                                </button>
                            )}
                            <button
                                type="button"
                                onClick={() => {
                                    setInput('Rang 120kg Arabica Cầu Đất trước 17:00 ngày mai, ưu tiên cao, cần chia việc cho rang, QC và đóng gói.');
                                    window.setTimeout(() => chatInputRef.current?.focus(), 0);
                                }}
                                style={{ background: 'none', border: 'none', color: '#d4a574', fontSize: 13, fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 4 }}
                            >
                                <ion-icon name="book-outline"></ion-icon> Xem ví dụ
                            </button>

```
