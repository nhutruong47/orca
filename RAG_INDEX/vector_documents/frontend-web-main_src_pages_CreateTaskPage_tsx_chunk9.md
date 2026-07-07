# Knowledge Document: CreateTaskPage.tsx (Chunk 10/66)

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
  "chunk_index": 9,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
d ? { ...m, isCancelled: true } : m));
    };

    const handleRevertDraft = (result: AiParseResult) => {
        const revertMsg: ChatMessage = {
            id: Date.now().toString(),
            role: 'assistant',
            content: 'Dưới đây là bản nháp bạn muốn khôi phục. Bạn có thể chỉnh sửa và xác nhận lại:',
            result: { ...result },
            timestamp: new Date()
        };
        setMessages(prev => {
            const activeMessage = findActiveDraftMessage(prev);
            return [
                ...prev.map(message =>
                    message.id === activeMessage?.id
                        ? { ...message, isArchived: true }
                        : message
                ),
                revertMsg
            ];
        });
        setShowHistory(false);
        setSelectedHistoryId(null);
        setTimeout(() => messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' }), 100);
    };

    const hasActiveDraft = Boolean(findActiveDraftMessage(messages)?.result);
    const draftMessages = messages.filter(isStoredDraft).slice().reverse();

    if (!team) {
        return (
            <div className="page-container" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: 300 }}>
                <div style={{ textAlign: 'center', opacity: 0.5 }}>
                    <div style={{ fontSize: 40, marginBottom: 12 }}><ion-icon name="time-outline" style={{ fontSize: '40px' }}></ion-icon></div>
                    <p>Đang tải dữ liệu...</p>
                </div>
            </div>
        );
    }

    return (
        <div className="task-gpt-page">
            <style>{`
                body.task-studio-mode .topbar {
                    display: none;
                }
                body.task-studio-mode .layout-content {
                    padding: 0;
                    background: var(--bg-primary);
                }
                body.task-studio-mode .layout-main {
                    background: var(--bg-primary);
                }
                body.task-studio-mode .sidebar {
                    background: var(--bg-secondary);
                    border-right: 1px solid var(--border);
                    box-shadow: none;
                }
                body.task-studio-mode .sidebar-logo {
                    border-bottom: 0;
                    margin-bottom: 20px;

```
