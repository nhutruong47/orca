# Knowledge Document: CreateTaskPage.tsx (Chunk 6/66)

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
  "chunk_index": 5,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
    document.body.classList.add('task-studio-mode');
        return () => document.body.classList.remove('task-studio-mode');
    }, []);

    useEffect(() => {
        if (!categoryOpen) return;

        const handlePointerDown = (event: PointerEvent) => {
            if (!categoryMenuRef.current?.contains(event.target as Node)) {
                setCategoryOpen(false);
            }
        };

        document.addEventListener('pointerdown', handlePointerDown);
        return () => document.removeEventListener('pointerdown', handlePointerDown);
    }, [categoryOpen]);

    useEffect(() => {
        if (!teamId) return;
        if (messages.length > 0) {
            localStorage.setItem(`ai_task_chat_${teamId}`, JSON.stringify(messages));
        } else {
            localStorage.removeItem(`ai_task_chat_${teamId}`);
        }
    }, [messages, teamId]);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, loading]);

    const clearHistory = () => {
        if (window.confirm('Bạn có chắc chắn muốn xóa toàn bộ lịch sử trò chuyện này?')) {
            setMessages([]);
            if (teamId) {
                localStorage.removeItem(`ai_task_chat_${teamId}`);
            }
        }
    };

    const findActiveDraftMessage = (items: ChatMessage[]) =>
        [...items].reverse().find(msg =>
            msg.result
            && !msg.result.needsClarification
            && !msg.isConfirmed
            && !msg.isCancelled
            && !msg.isArchived
        );

    const isStoredDraft = (message: ChatMessage) =>
        Boolean(message.result && !message.result.needsClarification);

    const handleSend = async () => {
        if (!input.trim() || !trialActive || loading) return;
        const activeDraftMessage = findActiveDraftMessage(messages);
        const activeDraft = activeDraftMessage?.result;

        const userMsg: ChatMessage = {
            id: Date.now().toString() + '-user',
            role: 'user',
            content: input.trim(),
            timestamp: new Date()
        };

        setMessages(prev => [...prev, userMsg]);
        setInput('');
        setLoading(true);

        try {
            if (activeDraft) {
                const currentDraft = resultToDraft(activeDraft);

```
