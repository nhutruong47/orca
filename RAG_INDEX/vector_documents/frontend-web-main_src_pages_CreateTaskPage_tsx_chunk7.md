# Knowledge Document: CreateTaskPage.tsx (Chunk 8/66)

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
  "chunk_index": 7,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
ted.missingFields?.length > 0) {
                const aiMsg: ChatMessage = {
                    id: Date.now().toString() + '-ai',
                    role: 'assistant',
                    content: extracted.clarifyingQuestion || 'Tôi cần thêm thông tin trước khi tạo công việc.',
                    timestamp: new Date()
                };
                setMessages(prev => [...prev, aiMsg]);
                return;
            }

            const draft = await aiWorkflowService.plan(teamId || '', extracted.intent, extracted.fields);
            const res = draftToResult(draft);

            const aiMsg: ChatMessage = {
                id: Date.now().toString() + '-ai',
                role: 'assistant',
                content: res.description || 'Tôi đã tạo draft công việc. Vui lòng xác nhận bên dưới.',
                result: res,
                timestamp: new Date()
            };
            setMessages(prev => [...prev, aiMsg]);
        } catch (e: any) {
            const msgStr = e?.response?.data?.message || e?.response?.data?.error || e.message || 'Lỗi kết nối AI. Hãy thử lại!';
            if (isPaymentRequiredError(e)) {
                setTrialActive(false);
                window.dispatchEvent(new CustomEvent('payment-required'));
                return;
            }
            const errorMsg: ChatMessage = {
                id: Date.now().toString() + '-err',
                role: 'assistant',
                content: msgStr,
                timestamp: new Date()
            };
            setMessages(prev => [...prev, errorMsg]);
        } finally {
            setLoading(false);
        }
    };

    const handleCreateGoal = async (result: AiParseResult) => {
        if (!teamId) return;
        setLoading(true);
        try {
            await goalService.create({
                teamId,
                title: result.title || 'Mục tiêu mới',
                outputTarget: result.quantity || result.description || '',
                rawInstruction: result.description || '',
                deadline: result.deadline || undefined,
                priority: priorityNumber(result.priority),
                useAi: false,
                chatLog: JSON.stringify(messages),
                tasks: result.tasks || []
            } as any);

            // Stay on the page and show success message
            const successMsg: ChatMessage = {

```
