# Knowledge Document: CreateTaskPage.tsx (Chunk 9/66)

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
  "chunk_index": 8,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
ruction: result.description || '',
                deadline: result.deadline || undefined,
                priority: priorityNumber(result.priority),
                useAi: false,
                chatLog: JSON.stringify(messages),
                tasks: result.tasks || []
            } as any);

            // Stay on the page and show success message
            const successMsg: ChatMessage = {
                id: Date.now().toString() + '-success',
                role: 'assistant',
                content: '🎉 **Tuyệt vời!** Công việc đã được phân bổ thành công vào nhóm. Vui lòng bấm vào "Quay lại tổng quan" để xem chi tiết, hoặc bạn có thể tiếp tục tạo mục tiêu mới ở đây.',
                timestamp: new Date()
            };
            setMessages(prev => {
                const activeMessage = findActiveDraftMessage(prev);
                return [
                    ...prev.map(message =>
                        message.id === activeMessage?.id
                            ? { ...message, isConfirmed: true }
                            : message
                    ),
                    successMsg
                ];
            });

        } catch (e: any) {
            const msgStr = e?.response?.data?.error || e?.response?.data?.message || e.message || 'Không thể tạo công việc, vui lòng thử lại';
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

    const handleCancelDraft = (msgId: string) => {
        setMessages(prev => prev.map(m => m.id === msgId ? { ...m, isCancelled: true } : m));
    };

    const handleRevertDraft = (result: AiParseResult) => {
        const revertMsg: ChatMessage = {
            id: Date.now().toString(),
            role: 'assistant',
            content: 'Dưới đây là bản nháp bạn muốn khôi phục. Bạn có thể chỉnh sửa và xác nhận lại:',
            result: { ...result },
            timestamp: new Date()
        };

```
