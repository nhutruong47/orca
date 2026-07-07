# Knowledge Document: AiAssistantPanel.tsx (Chunk 2/10)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/AiAssistantPanel.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "payment",
  "tags": [
    "payment",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 10
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: payment, chat

## Source Code Chunk
```tsx
max(280, Math.min(800, resizeStartH.current + delta)));
        };
        const onUp = () => setIsResizing(false);
        window.addEventListener('mousemove', onMove);
        window.addEventListener('mouseup', onUp);
        return () => { window.removeEventListener('mousemove', onMove); window.removeEventListener('mouseup', onUp); };
    }, [isResizing]);

    const handleSend = async () => {
        if (!input.trim() || !trialActive || loading) return;

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
            // For now, the backend only has parseText APIs we use text,
            // but the UX will feel conversational.
            const res = await aiService.parseText(userMsg.content, teamId);

            const aiMsg: ChatMessage = {
                id: Date.now().toString() + '-ai',
                role: 'assistant',
                content: res.description || 'Tôi đã phân tích yêu cầu của bạn:',
                result: res,
                timestamp: new Date()
            };
            setMessages(prev => [...prev, aiMsg]);
        } catch (e: any) {
            if (isPaymentRequiredError(e)) {
                window.dispatchEvent(new CustomEvent('payment-required'));
                return;
            }
            const errorMsg: ChatMessage = {
                id: Date.now().toString() + '-err',
                role: 'assistant',
                content: e?.response?.data?.message || 'Lỗi kết nối AI. Hãy thử lại!',
                timestamp: new Date()
            };
            setMessages(prev => [...prev, errorMsg]);
        } finally {
            setLoading(false);
        }
    };

    const priorityInfo: Record<string, { label: string; color: string; icon: string }> = {
        high: { label: 'Cao', color: '#a0673c', icon: '●' },
        medium: { label: 'Trung bình', color: '#d4a574', icon: '●' },
        low: { label: 'Thấp', color: '#22c55e', icon: '●' },
    };

    return (
        <div style={{
            background: 'linear-gradient(135deg, rgba(99,102,241,0.05) 0%, rgba(168,85,247,0.03) 100%)',
            border: '1px solid rgba(99,102,241,0.2)',

```
