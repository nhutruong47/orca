# Knowledge Document: CreateTaskPage.tsx (Chunk 25/66)

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
  "chunk_index": 24,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
          rows={1}
                    />
                    <button className="task-gpt-mode" type="button">
                        {hasActiveDraft ? 'Sửa draft' : 'Tạo draft'}
                        <ion-icon name="chevron-down-outline"></ion-icon>
                    </button>
                    <button
                        className="task-gpt-send"
                        type="button"
                        onClick={handleSend}
                        disabled={loading || !input.trim()}
                        aria-label="Gửi"
                    >
                        <ion-icon name={loading ? 'hourglass-outline' : 'arrow-up-outline'}></ion-icon>
                    </button>
                </div>
                <p className="task-gpt-disclaimer">Luồng AI v2: tạo draft, sửa trực tiếp trong ô chat, rồi lưu sau khi xem trước.</p>
            </footer>
        </div>
    );

    return (
        <div className="task-studio-page">
            <style>{`
                body.task-studio-mode .topbar {
                    display: none;
                }
                body.task-studio-mode .layout-content {
                    padding: 0;
                    background: #f7f3ed;
                }
                body.task-studio-mode .layout-main {
                    background: #f7f3ed;
                }
                body.task-studio-mode .sidebar {
                    background: #f4f0e8;
                    border-right: 1px solid #e4d9ca;
                    box-shadow: none;
                }
                body.task-studio-mode .sidebar-logo,
                body.task-studio-mode .nav-label,
                body.task-studio-mode .nav-text,
                body.task-studio-mode .nav-icon {
                    color: #5b3a1f !important;
                }
                body.task-studio-mode .nav-item {
                    color: #5b3a1f;
                    background: transparent;
                    border-radius: 0;
                }
                body.task-studio-mode .nav-item.active,
                body.task-studio-mode .nav-item:hover {
                    background: rgba(255, 171, 102, 0.18);
                    color: #8a4f22;
                }
                body.task-studio-mode .sidebar-user {
                    border-top-color: #e4d9ca;
                }
                .task-studio-page {

```
