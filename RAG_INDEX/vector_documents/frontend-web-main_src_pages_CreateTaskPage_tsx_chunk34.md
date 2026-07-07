# Knowledge Document: CreateTaskPage.tsx (Chunk 35/66)

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
  "chunk_index": 34,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
                  </section>
                )}

                <div style={{ display: 'flex', gap: 12, minHeight: 28 }}>
                    {messages.length > 0 && (
                        <button className="task-studio-ghost" onClick={clearHistory}>
                            <ion-icon name="trash-outline"></ion-icon>
                            Xóa lịch sử
                        </button>
                    )}
                    <button className="task-studio-ghost" onClick={() => setShowTokens(prev => !prev)}>
                        <ion-icon name="analytics-outline"></ion-icon>
                        {showTokens ? `${formatTokenCount(totalTokens)} token` : 'Xem token'}
                    </button>
                </div>
            </div>
        </div>
    );

    return (
        <div style={{
            minHeight: '100vh',
            background: 'var(--bg-primary)',
            padding: '32px 24px', // Reduced side padding
            fontFamily: "'Inter', sans-serif",
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center' // Center the content
        }}>
            <style>{`
                .main-content-layout {
                    width: 100%;
                    max-width: 1440px;
                    display: grid;
                    grid-template-columns: minmax(260px, 300px) minmax(0, 1fr);
                    gap: 32px;
                    align-items: start;
                }
                .task-select-trigger {
                    width: 100%;
                    min-height: 46px;
                    padding: 0 42px 0 14px;
                    border-radius: 10px;
                    border: 1px solid var(--border);
                    background: rgba(255, 255, 255, 0.03);
                    color: var(--text-primary);
                    font: 500 14px/1 var(--font);
                    text-align: left;
                    cursor: pointer;
                    transition: border-color 0.2s, background 0.2s, box-shadow 0.2s;
                }
                .task-select-trigger:hover,
                .task-select-trigger[aria-expanded="true"] {
                    background: rgba(255, 255, 255, 0.055);
                    border-color: rgba(212, 165, 116, 0.5);
                    box-shadow: 0 0 0 3px rgba(212, 165, 116, 0.12);
                }

```
