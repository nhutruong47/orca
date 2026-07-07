# Knowledge Document: CreateTaskPage.tsx (Chunk 33/66)

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
  "chunk_index": 32,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
ection>

                <section className="task-studio-meta" aria-label="Thông tin công việc">
                    <div className="task-studio-field">
                        <label>Nhóm công tác</label>
                        <select className="task-studio-select" value={category} onChange={event => setCategory(event.target.value)}>
                            {categoryOptions.map(option => (
                                <option key={option} value={option}>{option}</option>
                            ))}
                        </select>
                    </div>
                    <div className="task-studio-field">
                        <label>Mức độ ưu tiên</label>
                        <div className="task-studio-priority">
                            {['Thấp', 'Trung bình', 'Cao'].map(level => (
                                <button
                                    key={level}
                                    type="button"
                                    className={priority === level ? 'active' : ''}
                                    onClick={() => setPriority(level)}
                                >
                                    {level}
                                </button>
                            ))}
                        </div>
                    </div>
                    <div className="task-studio-field">
                        <label>Thời hạn</label>
                        <button className="task-studio-time" type="button">
                            Hôm nay, 17:00
                        </button>
                    </div>
                </section>

                <button
                    className="task-studio-cta"
                    onClick={handleSend}
                    disabled={!trialActive || loading || !input.trim()}
                >
                    {loading ? 'Đang phân tích...' : 'Khởi tạo Nhiệm vụ'}
                    <ion-icon name="arrow-forward-outline"></ion-icon>
                </button>
                <p className="task-studio-note">⊙ ORCA sẽ tự động phân loại và giao việc cho các thành viên liên quan.</p>

                {(messages.length > 0 || loading) && (
                    <section className="task-studio-thread" aria-label="Kết quả AI">
                        {messages.map(msg => (

```
