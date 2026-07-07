# Knowledge Document: CreateTaskPage.tsx (Chunk 7/66)

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
  "chunk_index": 6,
  "total_chunks": 66
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: analytics, payment, chat

## Source Code Chunk
```tsx
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
                const localRevision = applyDeterministicRevision(userMsg.content, currentDraft);
                const apiDraft = localRevision
                    || await aiWorkflowService.revise(teamId || '', userMsg.content, currentDraft);
                const revisedDraft = localRevision
                    || ensureRequestedRevision(userMsg.content, currentDraft, apiDraft);
                const res = draftToResult(revisedDraft);
                const removedTaskIndex = getRequestedRemovedTaskIndex(userMsg.content, currentDraft.tasks.length);
                const changeSummary = removedTaskIndex !== null
                    ? `Đã xóa công việc số ${removedTaskIndex + 1}.`
                    : 'Tôi đã sửa draft theo yêu cầu.';
                const aiMsg: ChatMessage = {
                    id: Date.now().toString() + '-ai',
                    role: 'assistant',
                    content: `${changeSummary} Bản mới có ${revisedDraft.tasks.length} công việc.`,
                    result: res,
                    timestamp: new Date()
                };
                setMessages(prev => [
                    ...prev.map(message =>
                        message.id === activeDraftMessage?.id
                            ? { ...message, isArchived: true }
                            : message
                    ),
                    aiMsg
                ]);
                return;
            }

            const extracted = await aiWorkflowService.extract(teamId || '', userMsg.content);

            if (extracted.intent === 'UNKNOWN' || extracted.missingFields?.length > 0) {
                const aiMsg: ChatMessage = {
                    id: Date.now().toString() + '-ai',
                    role: 'assistant',
                    content: extracted.clarifyingQuestion || 'Tôi cần thêm thông tin trước khi tạo công việc.',
                    timestamp: new Date()
                };
                setMessages(prev => [...prev, aiMsg]);

```
